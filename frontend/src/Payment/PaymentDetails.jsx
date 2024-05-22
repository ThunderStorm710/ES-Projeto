import React, {useEffect, useState} from 'react';
import {useLocation, useNavigate} from 'react-router-dom';
import API from "../api";
import './PaymentDetails.css';
import '../static/Loading.css';
import heart from "../static/heart.png";


function PaymentDetails() {
    const location = useLocation();
    const {paymentId} = location.state;
    const [paymentDetails, setPaymentDetails] = useState(null);
    const navigate = useNavigate();
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        async function fetchPaymentDetails() {
            try {
                const data = await API.getPaymentByID(paymentId);
                setPaymentDetails(data);
                setLoading(false);

            } catch (error) {
                console.error('Error fetching payment details:', error);
            }
        }

        fetchPaymentDetails();
    }, [paymentId]);

    const handlePayment = async () => {
        try {
            const data = await API.createPayment(paymentDetails.appointment_id, -1, paymentDetails.value);
            alert('Payment created successfully!');
            navigate('/');
        } catch (error) {
            console.error('Error creating payment:', error);
            alert('Failed to create payment.');
        }
    };

    const handleConsultation = () => {
        navigate('/upload', {state: {appointmentId: paymentDetails.appointment_id}});
    };

    if (!paymentDetails) {
        return <div>Loading...</div>;
    }
    if (loading) {
        return (
            <div className="loading-container">
                <img src={heart} alt="Loading" className="loading-image" />
            </div>
        );
    }
    return (
        <div className="payment-details-page">
            <h1>Payment Details</h1>
            <div className="payment-details-container">
                <p><strong>Doctor:</strong> Dr. {paymentDetails.doctor}</p>
                <p><strong>Specialty:</strong> {paymentDetails.specialty}</p>
                <p><strong>Date:</strong> {paymentDetails.date}</p>
                <p><strong>Hour:</strong> {paymentDetails.start_time}</p>
                <p><strong>Amount:</strong> {paymentDetails.value} €</p>
                <p>
                    <strong>Status:</strong> {paymentDetails.is_canceled ? 'Cancelled' : paymentDetails.is_done ? 'Payment done' : 'Pending'}
                </p>
                {paymentDetails.is_canceled ? (
                    <p className="warning-message">Your appointment has been cancelled. Time has expired.</p>
                ) : (
                    !paymentDetails.is_done ? (
                        <button onClick={handlePayment} className="payment-button">Proceed to Payment</button>
                    ) : (
                        <button onClick={handleConsultation} className="consultation-button">Start Consultation</button>
                    )
                )}
            </div>
        </div>
    );
}

export default PaymentDetails;

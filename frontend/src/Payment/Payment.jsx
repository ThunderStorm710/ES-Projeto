import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './Payment.css';
import API from "../api";

function Payments() {
    const [payments, setPayments] = useState([]);
    const navigate = useNavigate();

    useEffect(() => {
        async function fetchPayments() {
            try {
                const data = await API.getPaymentByPatientID();
                setPayments(data.payments);
                console.log(data.payments);
            } catch (error) {
                console.error('Error fetching payments:', error);
            }
        }

        fetchPayments();
    }, []);

    const getStatus = (payment) => {
        if (payment.is_canceled) {
            return "Cancelled";
        } else if (!payment.is_done) {
            return "Pending";
        } else if (payment.is_done) {
            return "Payment done";
        }
    };

    const handleRowClick = (paymentId) => {
        navigate(`/payment-details`, { state: { paymentId } });
    };

    return (
        <div className="payments-page">
            <h1>My Payments</h1>
            <table className="payments-table">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Doctor</th>
                        <th>Specialty</th>
                        <th>Date</th>
                        <th>Beginning</th>
                        <th>Amount</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {payments.map(payment => (
                        <tr key={payment.id} onClick={() => handleRowClick(payment.id)} className="clickable-row">
                            <td>{payment.id}</td>
                            <td>Dr. {payment.doctor}</td>
                            <td>{payment.specialty}</td>
                            <td>{payment.date}</td>
                            <td>{payment.start_time}</td>
                            <td>{payment.value} €</td>
                            <td>{getStatus(payment)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Payments;

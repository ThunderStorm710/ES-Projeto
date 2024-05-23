import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import './AllPayments.css';
import '../static/Loading.css';
import API from "../api";
import heart from "../static/heart.png";

function AllPayments() {
    const [payments, setPayments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null); // Estado para armazenar a mensagem de erro
    const navigate = useNavigate();

    useEffect(() => {
        async function fetchAllPayments() {
            try {
                const data = await API.getPayments(); // Supondo que este método existe na API
                if (data.payments && data.payments.length > 0) {
                    setPayments(data.payments);
                } else {
                    setError("No payments found.");
                }
            } catch (error) {
                    setError("No payments found.");
            } finally {
                setLoading(false);
            }
        }

        fetchAllPayments();
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

    if (loading) {
        return (
            <div className="loading-container">
                <img src={heart} alt="Loading" className="loading-image" />
            </div>
        );
    }

    return (
        <div className="all-payments-page">
            <h1>All Payments</h1>
            {error ? (
                <p className="error-message">{error}</p>
            ) : (
                <table className="all-payments-table">
                    <thead>
                        <tr>
                            <th>Patient</th>
                            <th>Doctor</th>
                            <th>Specialty</th>
                            <th>Date</th>
                            <th>Hour</th>
                            <th>Amount</th>
                            <th>Status</th>
                        </tr>
                    </thead>
                    <tbody>
                        {payments.map(payment => (
                            <tr key={payment.id} onClick={() => handleRowClick(payment.id)} className="clickable-row">
                                <td>{payment.patient}</td>
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
            )}
        </div>
    );
}

export default AllPayments;

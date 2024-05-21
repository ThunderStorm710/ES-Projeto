import React, {useState, useEffect} from 'react';
import axios from 'axios';
import './Payment.css';
import API from "../api";

function Payments() {
    const [payments, setPayments] = useState([]);

    useEffect(() => {
        async function fetchPayments() {
            try {
                const data = await API.getPaymentByPatientID();
                setPayments(data.payments);
                console.log(data.payments);
            } catch (error) {
                console.error('Error fetching time slots:', error);
            }
        }


        fetchPayments();
    }, []);

    const getStatus = (payment) => {
        if (payment.is_canceled) {
            return "Cancelado";
        } else if (!payment.is_done) {
            return "Pending";
        } else if (payment.is_done) {
            return "Pagamento realizado";
        }
    };

    return (
        <div className="payments-page">
            <h1>My Payments</h1>
            <table>
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
                    <tr key={payment.id}>
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

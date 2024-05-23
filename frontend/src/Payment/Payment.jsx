import React, {useState, useEffect} from 'react';
import {useNavigate} from 'react-router-dom';
import './Payment.css';
import '../static/Loading.css';
import API from "../api";
import heart from "../static/heart.png";
import logo from "../logo.png";
import {FaUser} from "react-icons/fa";
import isLoggedIn from "../utils";

function Payments() {
    const [payments, setPayments] = useState([]);
    const navigate = useNavigate();
    const [loading, setLoading] = useState(true);
    const userLoggedIn = isLoggedIn();

    const onLogout = async () => {
        try {
            await API.logout();
            window.location.reload();
        } catch (error) {
            console.error('Logout failed:', error);
        }
    };

    useEffect(() => {
        async function fetchPayments() {
            try {
                const data = await API.getPaymentByPatientID();
                setPayments(data.payments);
                console.log(data.payments);
                setLoading(false);

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
        navigate(`/payment-details`, {state: {paymentId}});
    };
    if (loading) {
        return (
            <div className="loading-container">
                <img src={heart} alt="Loading" className="loading-image"/>
            </div>
        );
    }
    return (
        <div>
            <nav className="navbar">
                <img src={logo} alt="ClinicPlus" className="navbar-logo"/>
                <div className="navbar-links">
                    <a href="/">Home</a>
                    <a href="/dashboard">Dashboard</a>
                    <a href="/appointment">My appointments</a>
                    <a href="/payments">My payments</a>
                    {userLoggedIn ? (
                        <button onClick={onLogout}><FaUser/> Logout</button>
                    ) : (
                        <a href="/login"><FaUser/> Login</a>
                    )}
                </div>
            </nav>
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
        </div>
    );
}

export default Payments;

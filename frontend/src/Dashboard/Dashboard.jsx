import React from 'react';
import './Dashboard.css'; // Assegure-se de importar o arquivo CSS correto
import { useNavigate } from 'react-router-dom';
import logo from "../logo.png";
import { FaUser } from "react-icons/fa";
import isLoggedIn from "../utils";
import API from "../api"; // Importe a API para usar a função de logout

function Dashboard() {
    const navigate = useNavigate();
    const userLoggedIn = isLoggedIn();

    const onLogout = async () => {
        try {
            await API.logout();
            window.location.reload();
        } catch (error) {
            console.error('Logout failed:', error);
        }
    };

    return (
        <div>
            <nav className="navbar">
                <img src={logo} alt="ClinicPlus" className="navbar-logo" />
                <div className="navbar-links">
                    <a href="/">Home</a>
                    <a href="/dashboard">Dashboard</a>
                    <a href="/appointment">My appointments</a>
                    <a href="/payments">My payments</a>
                    {userLoggedIn ? (
                        <button onClick={onLogout}><FaUser /> Logout</button>
                    ) : (
                        <a href="/login"><FaUser /> Login</a>
                    )}
                </div>
            </nav>

            <div className="dashboard">
                <div className="card" onClick={() => navigate('/newAppointment')}>
                    <h3>Create Appointment</h3>
                    <p>Schedule a new medical appointment.</p>
                </div>
                <div className="card" onClick={() => navigate('/appointment')}>
                    <h3>My Appointments</h3>
                    <p>See all your scheduled appointments.</p>
                </div>
                <div className="card" onClick={() => navigate('/payments')}>
                    <h3>My Payments</h3>
                    <p>Consult all your payments.</p>
                </div>
            </div>
        </div>
    );
}

export default Dashboard;

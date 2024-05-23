import React, {useState, useEffect} from 'react';
import API from '../api';
import './Appointment.css';
import '../static/Loading.css';
import heart from '../static/heart.png';
import isLoggedIn from "../utils";
import logo from "../logo.png";
import {FaUser} from "react-icons/fa"; // Ajuste o caminho para o seu logo

function Appointment() {
    const [appointments, setAppointments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null); // Estado para armazenar a mensagem de erro
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
        async function fetchAppointments() {
            try {
                const data = await API.getAppointmentByPatientID(); // Supondo que este método existe na API
                if (data.appointments && data.appointments.length > 0) {
                    setAppointments(data.appointments);
                } else {
                    setError("No appointments found.");
                }
            } catch (error) {
                setError("No appointments found.");

            } finally {
                setLoading(false);
            }
        }

        fetchAppointments();
    }, []);

    const getStatus = (appointment) => {
        if (!appointment.is_scheduled) {
            return "Awaiting payment";
        } else if (!appointment.is_finished && appointment.is_scheduled) {
            return "Appointment scheduled";
        } else if (appointment.is_finished) {
            return "Appointment concluded";
        }
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
            <div className="appointments-page">
                <h1>My Appointments</h1>
                {error ? (
                    <p className="error-message">{error}</p>
                ) : (
                    <table className="appointments-table">
                        <thead>
                        <tr>
                            <th>Doctor</th>
                            <th>Specialty</th>
                            <th>Date</th>
                            <th>Start Time</th>
                            <th>Status</th>
                        </tr>
                        </thead>
                        <tbody>
                        {appointments.map(appointment => (
                            <tr key={appointment.id}>
                                <td>Dr. {appointment.doctor}</td>
                                <td>{appointment.specialty}</td>
                                <td>{appointment.date}</td>
                                <td>{appointment.start_time}</td>
                                <td>{getStatus(appointment)}</td>
                            </tr>
                        ))}
                        </tbody>
                    </table>
                )}
            </div>
        </div>
    );
}

export default Appointment;

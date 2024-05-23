import React, {useState, useEffect} from 'react';
import axios from 'axios';
import '../Payment/Payment.css';
import isLoggedIn from "../utils";
import API from "../api";
import logo from "../logo.png";
import {FaUser} from "react-icons/fa";

function AppointmentsDetails() {
    const [appointments, setAppointments] = useState([]);

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
        const fetchAppointments = async () => {
            try {
                const response = await axios.get('http://yourapi.com/appointments');
                setAppointments(response.data);
            } catch (error) {
                console.error('Error fetching appointments:', error);
            }
        };

        fetchAppointments();
    }, []);

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
                <table>
                    <thead>
                    <tr>
                        <th>Date</th>
                        <th>Time</th>
                        <th>Doctor</th>
                        <th>Specialty</th>
                    </tr>
                    </thead>
                    <tbody>
                    {appointments.map(appointment => (
                        <tr key={appointment.id}>
                            <td>{appointment.date}</td>
                            <td>{appointment.time}</td>
                            <td>{appointment.doctor}</td>
                            <td>{appointment.specialty}</td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default AppointmentsDetails;

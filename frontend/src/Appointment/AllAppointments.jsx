import React, {useState, useEffect} from 'react';
import {useNavigate} from 'react-router-dom';
import './AllAppointments.css';
import '../static/Loading.css';
import heart from '../static/heart.png'; // Ajuste o caminho para o seu logo
import API from "../api";

function AllAppointments() {
    const [appointments, setAppointments] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null); // Estado para armazenar a mensagem de erro
    const navigate = useNavigate();

    useEffect(() => {
        async function fetchAllAppointments() {
            try {
                const data = await API.getAppointments(); // Supondo que este método existe na API
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

        fetchAllAppointments();
    }, []);

    const getStatus = (appointment) => {
        if (!appointment.is_scheduled) {
            return "Cancelled";
        } else if (!appointment.is_finished && appointment.is_scheduled) {
            return "Appointment scheduled";
        } else if (appointment.is_finished) {
            return "Appointment concluded";
        }
    };

    const handleRowClick = (appointmentId) => {
        navigate(`/appointment-details`, {state: {appointmentId}});
    };

    if (loading) {
        return (
            <div className="loading-container">
                <img src={heart} alt="Loading" className="loading-image"/>
            </div>
        );
    }

    return (
        <div className="all-appointments-page">
            <h1>All Appointments</h1>
            {error ? (
                <p className="error-message">{error}</p>
            ) : (
                <table className="all-appointments-table">
                    <thead>
                    <tr>
                        <th>User</th>
                        <th>Doctor</th>
                        <th>Specialty</th>
                        <th>Date</th>
                        <th>Start Time</th>
                        <th>Status</th>
                    </tr>
                    </thead>
                    <tbody>
                    {appointments.map(appointment => (
                        <tr key={appointment.id} onClick={() => handleRowClick(appointment.id)}
                            className="clickable-row">
                            <td>{appointment.patient}</td>
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
    );
}

export default AllAppointments;

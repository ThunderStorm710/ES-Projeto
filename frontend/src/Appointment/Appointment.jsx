import React, { useState, useEffect } from 'react';
import API from '../api';
import './Appointment.css';

function Appointment() {
    const [appointments, setAppointments] = useState([]);

    useEffect(() => {
        async function fetchAppointments() {
            try {
                const data = await API.getAppointmentByPatientID(); // Supondo que este método existe na API
                setAppointments(data.appointments);
                console.log(data.appointments);
            } catch (error) {
                console.error('Error fetching appointments:', error);
            }
        }

        fetchAppointments();
    }, []);

    const getStatus = (appointment) => {
        if (!appointment.is_scheduled) {
            return "Cancelado";
        } else if (!appointment.is_finished && appointment.is_scheduled) {
            return "Appointment scheduled";
        } else if (appointment.is_finished) {
            return "Appointment concluded";
        }
    };

    return (
        <div className="appointments-page">
            <h1>My Appointments</h1>
            <table>
                <thead>
                    <tr>
                        <th>ID</th>
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
                            <td>{appointment.id}</td>
                            <td>Dr. {appointment.doctor}</td>
                            <td>{appointment.specialty}</td>
                            <td>{appointment.date}</td>
                            <td>{appointment.start_time}</td>
                            <td>{getStatus(appointment)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default Appointment;

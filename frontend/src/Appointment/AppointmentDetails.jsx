import React, { useState, useEffect } from 'react';
import axios from 'axios';
import '../Payment/Payment.css';

function AppointmentsDetails() {
  const [appointments, setAppointments] = useState([]);

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
  );
}

export default AppointmentsDetails;

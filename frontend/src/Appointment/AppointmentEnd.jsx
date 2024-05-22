import React, { useEffect, useState } from 'react';
import { useNavigate, useLocation } from 'react-router-dom';
import API from "../api";
import './AppointmentEnd.css';

function AppointmentEnd() {
    const navigate = useNavigate();
    const location = useLocation();
    const { appointmentId } = location.state;
    const [timeLeft, setTimeLeft] = useState(3600); // 1 hora em segundos

    useEffect(() => {
        if (timeLeft === 0) {
            endConsultation();
        }

        const timer = setInterval(() => {
            setTimeLeft((prevTime) => prevTime - 1);
        }, 1000);

        return () => clearInterval(timer);
    }, [timeLeft]);

    const endConsultation = async () => {
        try {
            const data = await API.finishAppointment(appointmentId, -1);
            console.log('Appointment finished:', data);
            alert('Consultation ended.');
            navigate('/');
        } catch (error) {
            console.error('Error finishing appointment:', error);
            alert('Failed to finish consultation.');
        }
    };

    const handleEndConsultationClick = () => {
        endConsultation();
    };

    const formatTime = (seconds) => {
        const minutes = Math.floor(seconds / 60);
        const remainingSeconds = seconds % 60;
        return `${minutes}:${remainingSeconds < 10 ? '0' : ''}${remainingSeconds}`;
    };

    return (
        <div className="consultation-timer-page">
            <h1>Consultation in Progress</h1>
            <div className="timer-container">
                <p className="timer">{formatTime(timeLeft)}</p>
                <button onClick={handleEndConsultationClick} className="end-button">End Consultation</button>
            </div>
        </div>
    );
}

export default AppointmentEnd;

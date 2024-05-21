import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './CreateAppointment.css';
import API from "../api";

function CreateAppointment() {
    const [formData, setFormData] = useState({
        doctor: '',
        specialty: '',
        timeSlot: '',
        patient: ''
    });

    const [specialties, setSpecialties] = useState([]);
    const [doctors, setDoctors] = useState([]);
    const [timeSlots, setTimeSlots] = useState([]);

    useEffect(() => {
        async function fetchSpecialties() {
            try {
                const data = await API.getSpecialty();
                setSpecialties(data);
                console.log(data);
            } catch (error) {
                console.error('Error fetching specialties:', error);
            }
        }

        fetchSpecialties();
    }, []);

    useEffect(() => {
        async function fetchDoctors() {
            if (formData.specialty) {
                try {
                    const data = await API.getDoctorsBySpecialtyId(formData.specialty);
                    setDoctors(data.doctors);
                    console.log(data);
                    setTimeSlots([]); // Clear time slots when a new specialty is selected
                } catch (error) {
                    console.error('Error fetching doctors:', error);
                }
            } else {
                setDoctors([]);
                setTimeSlots([]);
            }
        }

        fetchDoctors();
    }, [formData.specialty])


    useEffect(() => {
        async function fetchTimeSlots() {
            if (formData.doctor) {
                try {
                    const data = await API.getTimeSlotsByDoctorId(formData.doctor);
                    setTimeSlots(data.slots);
                } catch (error) {
                    console.error('Error fetching time slots:', error);
                }
            } else {
                setTimeSlots([]);
            }
        }

        fetchTimeSlots();
    }, [formData.doctor]);

    const handleChange = (e) => {
        const { name, value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleSpecialtyChange = (e) => {
        const { value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            specialty: value,
            doctor: '', // Clear doctor and timeSlot when specialty changes
            timeSlot: ''
        }));
    };

    const handleDoctorChange = (e) => {
        const { value } = e.target;
        setFormData(prevState => ({
            ...prevState,
            doctor: value,
            timeSlot: '' // Clear timeSlot when doctor changes
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log('Form data:', formData)
        try {
            const { doctor, date, timeSlot } = formData;
            const response = await API.createAppointment(-1, doctor, timeSlot, 50);
            console.log(response.data, "_---");
            alert('Appointment created successfully!');
            console.log(response.data);
        } catch (error) {
            console.error('Error creating appointment:', error);
            alert('Failed to create appointment.');
        }
    };

    return (
        <div className="create-appointment-page">
            <h1>Create Appointment</h1>
            <form onSubmit={handleSubmit}>
                <label>
                    Specialty:
                    <select name="specialty" value={formData.specialty} onChange={handleSpecialtyChange}>
                        <option value="">Select Specialty</option>
                        {specialties.map(specialty => (
                            <option key={specialty.SpecialtyId} value={specialty.SpecialtyId}>{specialty.name}</option>
                        ))}
                    </select>
                </label>
                <label>
                    Doctor:
                    <select name="doctor" value={formData.doctor} onChange={handleDoctorChange}>
                        <option value="">Select Doctor</option>
                        {doctors.map(doctor => (
                            <option key={doctor.DoctorId} value={doctor.DoctorId}>{doctor.DoctorName}</option>
                        ))}
                    </select>
                </label>
                <label>
                    Time Slot:
                    <select name="timeSlot" value={formData.timeSlot} onChange={handleChange}>
                        <option value="">Select Time Slot</option>
                        {timeSlots.map(slot => (
                            <option key={slot.slot_id} value={slot.slot_id}>{slot.start_time}</option>
                        ))}
                    </select>
                </label>
                <button type="submit">Create Appointment</button>
            </form>
        </div>
    );
}

export default CreateAppointment;

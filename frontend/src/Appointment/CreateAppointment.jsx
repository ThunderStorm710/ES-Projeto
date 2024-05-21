import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './CreateAppointment.css';
import API from "../api";

function CreateAppointment() {
  const [formData, setFormData] = useState({
    doctor: '',
    specialty: '',
    date: ''
  });

  const [specialties, setSpecialties] = useState([]);
  const [doctors, setDoctors] = useState([]);
  const [timeSlots, setTimeSlots] = useState([]);



  useEffect(() => {
    async function fetchSpecialties() {
      try {
          API.getSpecialty().then((data) => setSpecialties(data));
      } catch (error) {
        console.error('Error fetching specialties:', error);
      }
    }

    async function fetchDoctors() {
      try {
          API.getDoctorsBySpecialtyId(id).then((data) => setDoctors(data));
      } catch (error) {
        console.error('Error fetching doctors:', error);
      }
    }

    async function fetchTimeSlots() {
      try {
          API.getDoctorsBySpecialtyId(id).then((data) => setDoctors(data));
        setTimeSlots(response.data);
      } catch (error) {
        console.error('Error fetching time slots:', error);
      }
    }

    fetchSpecialties();
    fetchDoctors();
    fetchTimeSlots();
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://yourapi.com/appointments', formData);
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
          <select name="specialty" value={formData.specialty} onChange={handleChange}>
            <option value="">Select Specialty</option>
            {specialties.map(specialty => (
              <option key={specialty.id} value={specialty.name}>{specialty.name}</option>
            ))}
          </select>
        </label>
        <label>
          Doctor:
          <select name="doctor" value={formData.doctor} onChange={handleChange}>
            <option value="">Select Doctor</option>
            {doctors.map(doctor => (
              <option key={doctor.id} value={doctor.name}>{doctor.name}</option>
            ))}
          </select>
        </label>
        <label>
          Date:
          <input type="date" name="date" value={formData.date} onChange={handleChange} />
        </label>
        <label>
          Time Slot:
          <select name="timeSlot" value={formData.timeSlot} onChange={handleChange}>
            <option value="">Select Time Slot</option>
            {timeSlots.map(slot => (
              <option key={slot.id} value={slot.time}>{slot.time}</option>
            ))}
          </select>
        </label>
        <button type="submit">Create Appointment</button>
      </form>
    </div>
  );
}

export default CreateAppointment;

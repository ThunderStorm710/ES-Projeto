import React, { useState } from 'react';
import axios from 'axios';
import './CreateAppointment.css'; // Assegure-se de criar e importar o arquivo CSS correspondente

function CreateAppointment() {
  const [formData, setFormData] = useState({
    doctor: '',
    specialty: '',
    date: ''
  });

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
      console.log(response.data); // Exibe a resposta do backend no console
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
            <option value="Dermatology">Dermatology</option>
            <option value="Cardiology">Cardiology</option>
            <option value="Pediatrics">Pediatrics</option>
            {/* Add more specialties as needed */}
          </select>
        </label>
        <label>
          Doctor:
          <select name="doctor" value={formData.doctor} onChange={handleChange}>
            <option value="">Select Doctor</option>
            <option value="Dr. Smith">Dr. Smith</option>
            <option value="Dr. Johnson">Dr. Johnson</option>
            {/* Add more doctors as needed */}
          </select>
        </label>
        <label>
          Date:
          <input type="date" name="date" value={formData.date} onChange={handleChange} />
        </label>
        <button type="submit">Create Appointment</button>
      </form>
    </div>
  );
}

export default CreateAppointment;

import React from 'react';
import './Appointment.css'; // Garanta que este arquivo CSS esteja corretamente importado

function Appointments() {
  return (
    <div className="appointments-page">
      <h1>My Appointments</h1>
      <section className="my-appointments">
        {/* Lista de consultas marcadas, exemplo estático */}
        <ul>
          <li>Consulta de Dermatologia - Dr. Smith - 25/05/2024</li>
          <li>Consulta de Cardiologia - Dr. Johnson - 30/05/2024</li>
        </ul>
      </section>
      <section className="book-appointment">
        <h2>Book a New Appointment</h2>
        <button>Book Appointment</button>
      </section>
      <section className="clinic-info">
        <h2>Our Specialties</h2>
        <ul>
          <li>Dermatologia</li>
          <li>Cardiologia</li>
          <li>Pediatria</li>
          {/* Adicionar mais especialidades conforme necessário */}
        </ul>
        <h2>Our Doctors</h2>
        <ul>
          <li>Dr. Smith - Dermatologia</li>
          <li>Dr. Johnson - Cardiologia</li>
          {/* Adicionar mais médicos conforme necessário */}
        </ul>
      </section>
    </div>
  );
}

export default Appointments;

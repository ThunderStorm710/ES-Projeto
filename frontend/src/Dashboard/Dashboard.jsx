import React from 'react';
import './Dashboard.css'; // Assegure-se de importar o arquivo CSS correto
import { useNavigate } from 'react-router-dom';

function Dashboard() {
      const navigate = useNavigate();

  return (
    <div className="dashboard">
      <div className="card" onClick={() => navigate('/newAppointment')}>
        <h3>Create Appointment</h3>
        <p>Agende uma nova consulta médica.</p>
      </div>
      <div className="card" onClick={() => navigate('/appointment')}>
          <h3>My Appointments</h3>
          <p>Veja todas as suas consultas marcadas.</p>
      </div>
      <div className="card" onClick={() => navigate('/payments')}>
        <h3>My Payments</h3>
        <p>Consulte todos os seus pagamentos.</p>
      </div>
    </div>
  );
}

export default Dashboard;

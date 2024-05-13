import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate} from 'react-router-dom';
import Login from "./Login/Login";
import Appointment from "./Appointment/Appointment";
import isLoggedIn from "./utils";
import Home from "./Home/Home";
import API from "./api";
import AppointmentsDetails from "./Appointment/AppointmentDetails";
import Payments from "./Payment/Payment";
import CreateAppointment from "./Appointment/CreateAppointment";  // Supondo que o componente Home esteja em ./Home/Home

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const handleLogout = () => {
        API.logout().then(() => {
            setIsAuthenticated(false);
            console.log("2isAuthenticated", isAuthenticated);
            window.location.reload();
        });
    };


  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home onLogout={handleLogout} />} />
        <Route path="/login" element={isLoggedIn() ? <Navigate replace to="/appointment" /> : <Login onLogin={() => setIsAuthenticated(true)} />} />
        <Route path="/appointment" element={isLoggedIn() ? <AppointmentsDetails /> : <Navigate replace to="/" />} />
        <Route path="/newAppointment" element={isLoggedIn() ? <CreateAppointment /> : <Navigate replace to="/" />} />
        <Route path="/payments" element={isLoggedIn() ? <Payments /> : <Navigate replace to="/" />} />
        <Route path="*" element={<Navigate replace to="/" />} />
      </Routes>
    </Router>
  );
}

export default App;

import React, {useState, useEffect} from 'react';
import {BrowserRouter as Router, Routes, Route, Navigate} from 'react-router-dom';
import Login from "./Login/Login";
import Appointment from "./Appointment/Appointment";
import isLoggedIn from "./utils";
import Home from "./Home/Home";
import API from "./api";
import AppointmentsDetails from "./Appointment/AppointmentDetails";
import Payments from "./Payment/Payment";
import CreateAppointment from "./Appointment/CreateAppointment";
import AppointmentBegin from "./Appointment/AppointmentBegin";
import CreatePayment from "./Payment/PaymentDetails";
import AppointmentEnd from "./Appointment/AppointmentEnd";
import AllPayments from "./Payment/AllPayments";
import AllAppointments from "./Appointment/AllAppointments";
import Dashboard from "./Dashboard/Dashboard";  // Supondo que o componente Home esteja em ./Home/Home

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
                <Route path="/" element={<Home onLogout={handleLogout}/>}/>
                <Route path="/dashboard" element={isLoggedIn() ? <Dashboard/> : <Navigate replace to="/"/>}/>
                <Route path="/login" element={isLoggedIn() ? <Navigate replace to="/"/> :
                    <Login onLogin={() => setIsAuthenticated(true)}/>}/>
                <Route path="/appointment" element={isLoggedIn() ? <Appointment/> : <Navigate replace to="/"/>}/>
                <Route path="/newAppointment"
                       element={isLoggedIn() ? <CreateAppointment/> : <Navigate replace to="/"/>}/>
                <Route path="/payments" element={isLoggedIn() ? <Payments/> : <Navigate replace to="/"/>}/>
                <Route path="/upload" element={isLoggedIn() ? <AppointmentBegin/> : <Navigate replace to="/"/>}/>
                <Route path="/payment-details" element={isLoggedIn() ? <CreatePayment/> : <Navigate replace to="/"/>}/>
                <Route path="/appointmentLIVE" element={isLoggedIn() ? <AppointmentEnd/> : <Navigate replace to="/"/>}/>
                <Route path="/AllPayments" element={<AllPayments/>}/>
                <Route path="/AllAppointments" element={<AllAppointments/>}/>
                <Route path="*" element={<Navigate replace to="/"/>}/>
            </Routes>
        </Router>
    );
}

export default App;

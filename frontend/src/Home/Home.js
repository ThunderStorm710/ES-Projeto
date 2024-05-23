import React from "react";
import './Home.css'; // Garanta que este arquivo CSS esteja corretamente importado e ajustado
import {FaUser} from 'react-icons/fa'; // Ícones de pesquisa
import logo from '../logo.png'; // Ajuste o caminho para o seu logo
import isLoggedIn from "../utils"; // Utilitário para verificar o status do login

const Home = ({onLogout}) => {
    const userLoggedIn = isLoggedIn();

    return (
        <div className="homepage">
            <nav className="navbar">
                <img src={logo} alt="ClinicPlus" className="navbar-logo"/>
                <div className="navbar-links">
                    <a href="/">Home</a>
                    <a href="/dashboard">Dashboard</a>
                    <a href="/appointment">My appointments</a>
                    <a href="/payments">My payments</a>
                    {userLoggedIn ? (
                        <button onClick={onLogout}><FaUser/> Logout</button>
                    ) : (
                        <a href="/login"><FaUser/> Login</a>
                    )}
                </div>
            </nav>


            <header className="hero-section">
                <div className="hero-image">
                    <h2>Welcome to ClinicPlus</h2>
                    <p>Your trusted partner in healthcare excellence.</p>
                </div>
            </header>


            <footer className="footer">
                <p>© 2024 ClinicPlus. All rights reserved.</p>
                <p>Contact us: info@clinicplus.com</p>
            </footer>
        </div>
    );
};

export default Home;

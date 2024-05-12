import React from "react";
import './Home.css'; // Garanta que este arquivo CSS esteja corretamente importado e ajustado

const Home = ({ isAuthenticated, onLogout }) => {
  return (
    <div className="homepage">
      <nav className="navbar">
        <h1>ClinicPlus</h1>
        <div className="nav-links">
          {isAuthenticated ? (
            <button onClick={onLogout}>Logout</button>
          ) : (
            <a href="/login">Login</a>
          )}
          <a href="#services">Services</a>
          <a href="#contact">Contact</a>
          <a href="#about">About Us</a>
        </div>
      </nav>
      <header className="hero-section">
        <h2>Welcome to ClinicPlus</h2>
        <p>Your trusted partner in healthcare excellence.</p>
      </header>
      <footer className="footer">
        <p>© 2024 ClinicPlus. All rights reserved.</p>
        <p>Contact us: info@clinicplus.com</p>
      </footer>
    </div>
  );
};

export default Home;

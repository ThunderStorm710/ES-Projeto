import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate, Link } from 'react-router-dom';
import Login from "./Login/Login";
import Appointment from "./Appointment/Appointment";
import isLoggedIn from "./utils";
import Home from "./Home/Home";  // Supondo que o componente Home esteja em ./Home/Home

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  useEffect(() => {
    setIsAuthenticated(isLoggedIn());
  }, []);

  const handleLogout = () => {
    // Aqui você deve adicionar a lógica para remover a sessão ou token de autenticação
    setIsAuthenticated(false);
    // Você pode adicionar também um redirecionamento ou um refresh para limpar o estado da aplicação
  };

  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home isAuthenticated={isAuthenticated} onLogout={handleLogout} />} />
        <Route path="/login" element={isAuthenticated ? <Navigate replace to="/appointment" /> : <Login onLogin={() => setIsAuthenticated(true)} />} />
        <Route path="/appointment" element={isAuthenticated ? <Appointment /> : <Navigate replace to="/" />} />
        <Route path="*" element={<Navigate replace to="/" />} />
      </Routes>
    </Router>
  );
}

export default App;

import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from "./Login/Login";
import Appointment from "./Appointment";
import isLoggedIn from "./utils.js";  // Importando a função

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);



  // Verificar o status do login ao carregar o componente
  useEffect(() => {
    setIsAuthenticated(isLoggedIn());
  }, []);

  return (
    <Router>
      <Routes>
        <Route path="/login" element={isAuthenticated ? <Navigate replace to="/appointment" /> : <Login onLogin={() => setIsAuthenticated(true)} />} />
        <Route path="/appointment" element={isAuthenticated ? <Appointment /> : <Navigate replace to="/login" />} />
        <Route path="*" element={<Navigate replace to="/login" />} />
      </Routes>
    </Router>
  );
}

export default App;

import React, { useState } from 'react';
import axios from 'axios';

function Appointment() {
  const [username, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    axios.post('http://127.0.0.1:8000/api/login/', {
      username: username,
      password: password
    })
    .then(response => {
      console.log("Logged in!");
      // Salvar o token no localStorage ou em um estado de contexto
    })
    .catch(error => {
      console.error("Login error", error);
    });
  };

  const handleLogout = () => {
    // Lógica para logout
    console.log("Logged out!");
  };

  return (
    <div>
      <input type="username" value={username} onChange={e => setEmail(e.target.value)} />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default Appointment;
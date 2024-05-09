import React, { useState } from 'react';
import axios from 'axios';

function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    axios.post('http://your-api-url.com/api/login/', {
      email: email,
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
      <input type="email" value={email} onChange={e => setEmail(e.target.value)} />
      <input type="password" value={password} onChange={e => setPassword(e.target.value)} />
      <button onClick={handleLogin}>Login</button>
      <button onClick={handleLogout}>Logout</button>
    </div>
  );
}

export default Login;
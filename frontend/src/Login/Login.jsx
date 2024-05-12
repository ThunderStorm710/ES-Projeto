import React, { useEffect, useState } from 'react';
import './Login.css';
import { useNavigate } from "react-router-dom";
import isLoggedIn from "../utils";
import API from "../api";

function Login() {
    const [isLoginView, setIsLoginView] = useState(true);
    const [inputs, setInputs] = useState({
        username: "",
        password: "",
        repeat_password: "",
        email: "",
    });

    const [errorLogin, setErrorLogin] = useState("");
    const [errorRegister, setErrorRegister] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        if (isLoggedIn()) {
            navigate("/");
        }
    }, [navigate]); // Inclua dependências no useEffect para evitar comportamentos inesperados.

    function handleChange(event) {
        const { name, value } = event.target; // Extração das propriedades do evento.
        setInputs(inputs => ({
            ...inputs,
            [name]: value,
        }));
    }

    const handleLogin = async (event) => {
        event.preventDefault();
                console.log(inputs);
        try {
            await API.login(inputs.username, inputs.password);
            if (isLoggedIn()) {
                navigate("/");
            } else {
                setErrorLogin("Invalid credentials");
            }
        } catch (error) {
            setErrorLogin("Login failed: " + error.message);
        }
    };

    const handleRegister = async (event) => {
        event.preventDefault();
        console.log(inputs);
        if (inputs.password === inputs.repeat_password) {
            try {
                const data = await API.register(
                    inputs.username,
                    inputs.password,
                    inputs.repeat_password,
                    inputs.email
                );
                if (data.message) {
                    await API.login(inputs.username, inputs.password);
                    if (isLoggedIn()) {
                        navigate("/");
                    } else {
                        setErrorRegister("User already exists");
                    }
                } else {
                    setErrorRegister("Registration failed: " + data.message);
                }
            } catch (error) {
                setErrorRegister("Registration error: " + error.message);
            }
        } else {
            setErrorRegister("Passwords don't match");
        }
    };

    return (
        <div className="login-container">
            <h1>{isLoginView ? 'Login' : 'Sign up'}</h1>
            <form onSubmit={isLoginView ? handleLogin : handleRegister}>
                <input type="text" placeholder="Username" name="username" value={inputs.username} onChange={handleChange}/>
                {!isLoginView && (
                    <input type="email" placeholder="Email" name="email" value={inputs.email} onChange={handleChange}/>
                )}
                <input type="password" placeholder="Password" name="password" value={inputs.password} onChange={handleChange}/>
                {!isLoginView && (
                    <input type="password" placeholder="Repeat Password" name="repeat_password" value={inputs.repeat_password} onChange={handleChange}/>
                )}
                <button type="submit">
                    {isLoginView ? 'Login' : 'Sign up'}
                </button>
                <button type="button" onClick={() => setIsLoginView(!isLoginView)}>
                    {isLoginView ? 'Create an account' : 'Already have an account'}
                </button>
            </form>
            {errorLogin && <div>{errorLogin}</div>}
            {errorRegister && <div>{errorRegister}</div>}
        </div>
    );
}

export default Login;

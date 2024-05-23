import React, {useEffect, useState} from 'react';
import './Login.css';
import {useNavigate} from "react-router-dom";
import isLoggedIn from "../utils";
import API from "../api";
import axios from 'axios'; // Importar axios

function Login() {
    const [isLoginView, setIsLoginView] = useState(true);
    const [inputs, setInputs] = useState({
        username: "",
        password: "",
        repeat_password: "",
        email: "",
    });
    const [image, setImage] = useState(null); // Novo estado para armazenar a imagem
    const [errorLogin, setErrorLogin] = useState("");
    const [errorRegister, setErrorRegister] = useState("");
    const navigate = useNavigate();

    useEffect(() => {
        if (isLoggedIn()) {
            navigate("/");
        }
    }, [navigate]); // Inclua dependências no useEffect para evitar comportamentos inesperados.

    function handleChange(event) {
        const {name, value} = event.target; // Extração das propriedades do evento.
        setInputs(inputs => ({
            ...inputs,
            [name]: value,
        }));
    }

    function handleImageChange(event) {
        setImage(event.target.files[0]); // Define a imagem selecionada
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
                const formData = new FormData();
                formData.append('username', inputs.username);
                formData.append('password', inputs.password);
                formData.append('repeat_password', inputs.repeat_password);
                formData.append('email', inputs.email);
                if (image) {
                    formData.append('image', image); // Adiciona a imagem ao FormData
                }

                const data = await API.register(inputs.username, inputs.password, inputs.repeat_password, inputs.email);
                if (data.message) {
                    console.log(data.id);
                    await API.login(inputs.username, inputs.password);
                    if (isLoggedIn()) {
                        alert('Signed up successfully!');
                        navigate("/");
                        // Nova lógica para fazer upload da imagem
                        const url = 'http://localhost:8000/api/indexFace/';
                        const uploadData = new FormData();
                        uploadData.append('patient_id', data.id);
                        uploadData.append('title', 'Maria'); // Substitua conforme necessário
                        uploadData.append('content', 'Maria'); // Substitua conforme necessário
                        if (image) {
                            uploadData.append('image', image); // Adiciona a imagem ao FormData
                        }

                        try {
                            const res = await axios.post(url, uploadData, {
                                headers: {
                                    'content-type': 'multipart/form-data'
                                }
                            });
                            console.log(res.data);
                            alert('Image uploaded successfully!');
                        } catch (err) {
                            console.log(err);
                            alert('Failed to upload image.');
                        }
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
                <input type="text" placeholder="Username" name="username" value={inputs.username}
                       onChange={handleChange}/>
                {!isLoginView && (
                    <>
                        <input type="email" placeholder="Email" name="email" value={inputs.email}
                               onChange={handleChange}/>
                        <input type="password" placeholder="Repeat Password" name="repeat_password"
                               value={inputs.repeat_password} onChange={handleChange}/>
                        <input type="file" name="image" accept="image/*"
                               onChange={handleImageChange}/> {/* Campo de upload de imagem */}
                    </>
                )}
                <input type="password" placeholder="Password" name="password" value={inputs.password}
                       onChange={handleChange}/>
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

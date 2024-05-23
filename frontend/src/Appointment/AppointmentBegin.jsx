import React, {useState} from 'react';
import {useLocation, useNavigate} from 'react-router-dom';
import API from "../api"; // Certifique-se de criar este arquivo para estilização
import './AppointmentBegin.css';
import logo from "../logo.png";
import {FaUser} from "react-icons/fa";
import isLoggedIn from "../utils";

function AppointmentBegin() {
    const location = useLocation();
    const {appointmentId} = location.state;
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [image, setImage] = useState(null);
    const navigate = useNavigate();
    const userLoggedIn = isLoggedIn();

    const onLogout = async () => {
        try {
            await API.logout();
            window.location.reload();
        } catch (error) {
            console.error('Logout failed:', error);
        }
    };

    const handleTitleChange = (e) => {
        setTitle(e.target.value);
    };

    const handleContentChange = (e) => {
        setContent(e.target.value);
    };

    const handleImageChange = (e) => {
        setImage(e.target.files[0]);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const data = await API.searchFace(appointmentId, '1', '2', image); // Supondo que este método existe na API
            console.log(data); // Verifique se os dados estão corretos
            if (data.dados.match === false) {
                alert('Image not recognized!');
            } else if (data.dados.match === true) {
                alert('Image uploaded successfully!');
                navigate('/appointmentLIVE', {state: {appointmentId}});
            }
        } catch (err) {
            console.log(err);
            alert('Failed to upload image.');
        }
    };

    return (
        <div>
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
            <div className="consultation-page">
                <form onSubmit={handleSubmit} className="consultation-form">
                    <h2>Begin Appointment</h2>
                    <div className="form-group">
                        <label htmlFor="image">Upload Image</label>
                        <input type="file" id="image" accept="image/png, image/jpeg" onChange={handleImageChange}
                               required/>
                    </div>
                    <button type="submit" className="submit-button">Upload</button>
                </form>
            </div>
        </div>
    );
}

export default AppointmentBegin;

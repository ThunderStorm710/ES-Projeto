import React, { useState } from 'react';
import axios from 'axios';
import { useLocation, useNavigate } from 'react-router-dom';
import './AppointmentBegin.css'; // Certifique-se de criar este arquivo para estilização

function AppointmentBegin() {
    const location = useLocation();
    const { appointmentId } = location.state;
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [image, setImage] = useState(null);
    const navigate = useNavigate();

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
        console.log({ title, content, image });
        let form_data = new FormData();
        form_data.append('image', image, image.name);
        form_data.append('title', title);
        form_data.append('content', content);
        form_data.append('appointmentId', appointmentId);

        let url = 'http://localhost:8000/api/upload/';
        try {
            const res = await axios.post(url, form_data, {
                headers: {
                    'content-type': 'multipart/form-data'
                }
            });
            console.log(res.data);
            alert('Image uploaded successfully!');
            navigate('/appointmentLIVE', { state: { appointmentId } });

        } catch (err) {
            console.log(err);
            alert('Failed to upload image.');
        }
    };

    return (
        <div className="consultation-page">
            <form onSubmit={handleSubmit} className="consultation-form">
                <h2>Begin Appointment</h2>
                <div className="form-group">
                    <label htmlFor="title">Title</label>
                    <input type="text" placeholder="Title" id="title" value={title} onChange={handleTitleChange} required />
                </div>
                <div className="form-group">
                    <label htmlFor="content">Content</label>
                    <input type="text" placeholder="Content" id="content" value={content} onChange={handleContentChange} required />
                </div>
                <div className="form-group">
                    <label htmlFor="image">Upload Image</label>
                    <input type="file" id="image" accept="image/png, image/jpeg" onChange={handleImageChange} required />
                </div>
                <button type="submit" className="submit-button">Upload</button>
            </form>
        </div>
    );
}

export default AppointmentBegin;

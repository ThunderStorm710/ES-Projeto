import React, {useState, useEffect} from 'react';
import {useNavigate} from 'react-router-dom';
import API from "../api";
import './CreateAppointment.css';
import logo from "../logo.png";
import {FaUser} from "react-icons/fa";
import isLoggedIn from "../utils";

function CreateAppointment() {
    const [formData, setFormData] = useState({
        doctor: '',
        specialty: '',
        date: '', // Adicionando o campo de data
        timeSlot: '',
        patient: ''
    });

    const [specialties, setSpecialties] = useState([]);
    const [doctors, setDoctors] = useState([]);
    const [timeSlots, setTimeSlots] = useState([]);
    const [loadingSpecialties, setLoadingSpecialties] = useState(true);
    const [loadingDoctors, setLoadingDoctors] = useState(false);
    const [loadingTimeSlots, setLoadingTimeSlots] = useState(false);
    const [error, setError] = useState('');

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

    useEffect(() => {
        async function fetchSpecialties() {
            setLoadingSpecialties(true);
            try {
                const data = await API.getSpecialty();
                setSpecialties(data);
                setLoadingSpecialties(false);
                console.log(data);
            } catch (error) {
                console.error('Error fetching specialties:', error);
                setError('Failed to fetch specialties');
                setLoadingSpecialties(false);
            }
        }

        fetchSpecialties();
    }, []);

    useEffect(() => {
        async function fetchDoctors() {
            if (formData.specialty) {
                setLoadingDoctors(true);
                try {
                    const data = await API.getDoctorsBySpecialtyId(formData.specialty);
                    setDoctors(data.doctors || []);
                    setLoadingDoctors(false);
                    console.log(data);
                    setTimeSlots([]); // Clear time slots when a new specialty is selected
                } catch (error) {
                    console.error('Error fetching doctors:', error);
                    setError('Failed to fetch doctors');
                    setLoadingDoctors(false);
                }
            } else {
                setDoctors([]);
                setTimeSlots([]);
            }
        }

        fetchDoctors();
    }, [formData.specialty]);

    useEffect(() => {
        async function fetchTimeSlots() {
            if (formData.doctor) {
                console.log(formData.doctor)
                setLoadingTimeSlots(true);
                try {
                    const data = await API.getTimeSlotsByDoctorId(formData.doctor);
                    setTimeSlots(data.slots || []);
                    setLoadingTimeSlots(false);
                } catch (error) {
                    console.error('Error fetching time slots:', error);
                    setError('Failed to fetch time slots');
                    setLoadingTimeSlots(false);
                }
            } else {
                setTimeSlots([]);
            }
        }

        fetchTimeSlots();
    }, [formData.doctor]);

    const handleChange = (e) => {
        const {name, value} = e.target;
        console.log(name, value, "--")
        setFormData(prevState => ({
            ...prevState,
            [name]: value
        }));
    };

    const handleSpecialtyChange = (e) => {
        const {value} = e.target;
        setFormData(prevState => ({
            ...prevState,
            specialty: value,
            doctor: '', // Clear doctor and timeSlot when specialty changes
            timeSlot: ''
        }));
    };

    const handleDoctorChange = (e) => {
        const {value} = e.target;
        setFormData(prevState => ({
            ...prevState,
            doctor: value,
            timeSlot: '' // Clear timeSlot when doctor changes
        }));
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        console.log('Form data:', formData);
        try {
            const {doctor, date, timeSlot} = formData;
            const response = await API.createAppointment(-1, doctor, timeSlot, 50);
            alert('Appointment created successfully!');
            // Redirecionar para a página de pagamento e passar o objeto appointment
            navigate('/');
        } catch (error) {
            console.error('Error creating appointment:', error);
            alert('Failed to create appointment.');
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
            <div className="create-appointment-page">
                <h1>Create Appointment</h1>
                <form onSubmit={handleSubmit}>
                    <label>
                        Specialty:
                        <select name="specialty" value={formData.specialty} onChange={handleSpecialtyChange}
                                disabled={loadingSpecialties}>
                            <option value="">Select Specialty</option>
                            {loadingSpecialties ? (
                                <option>Loading...</option>
                            ) : specialties.length > 0 ? (
                                specialties.map(specialty => (
                                    <option key={specialty.SpecialtyId}
                                            value={specialty.SpecialtyId}>{specialty.name}</option>
                                ))
                            ) : (
                                <option>No specialties available</option>
                            )}
                        </select>
                    </label>
                    <label>
                        Doctor:
                        <select name="doctor" value={formData.doctor} onChange={handleDoctorChange}
                                disabled={loadingDoctors}>
                            <option value="">Select Doctor</option>
                            {loadingDoctors ? (
                                <option>Loading...</option>
                            ) : doctors.length > 0 ? (
                                doctors.map(doctor => (
                                    <option key={doctor.DoctorId} value={doctor.DoctorId}>{doctor.DoctorName}</option>
                                ))
                            ) : (
                                <option>No doctors available</option>
                            )}
                        </select>
                    </label>
                    <label>
                        Time Slot:
                        <select name="timeSlot" value={formData.timeSlot} onChange={handleChange}
                                disabled={loadingTimeSlots}>
                            <option value="">Select Time Slot</option>
                            {loadingTimeSlots ? (
                                <option>Loading...</option>
                            ) : timeSlots.length > 0 ? (
                                timeSlots.map(slot => (
                                    <option key={slot.slot_id}
                                            value={slot.slot_id}>{slot.date} {slot.start_time}</option>
                                ))
                            ) : (
                                <option>No time slots available</option>
                            )}
                        </select>
                    </label>
                    <button type="submit" disabled={loadingSpecialties || loadingDoctors || loadingTimeSlots}>Create
                        Appointment
                    </button>
                </form>
                {error && <p className="error-message">{error}</p>}
            </div>
        </div>
    );
}

export default CreateAppointment;

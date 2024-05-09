import React, { useState, useEffect } from 'react';
import axios from 'axios';

function AppointmentDetails() {
  const [details, setDetails] = useState({});

  useEffect(() => {
    axios.get('http://your-api-url.com/api/appointment-details/')
    .then(response => {
      setDetails(response.data);
    })
    .catch(error => {
      console.error("Error fetching appointment details", error);
    });
  }, []);

  return (
    <div>
      <p>Time: {details.time}</p>
      <p>Room: {details.room}</p>
      <p>Other Information: {details.otherInfo}</p>
    </div>
  );
}

export default AppointmentDetails;

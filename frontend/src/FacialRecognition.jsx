import React from 'react';
import axios from 'axios';

function FacialRecognition() {
  const handleRecognition = (imageData) => {
    axios.post('http://127.0.0.1:8000/api/facial-recognition/', {
      image: imageData
    })
    .then(response => {
      console.log("Face recognized!");
    })
    .catch(error => {
      console.error("Recognition error", error);
    });
  };

  return (
    <div>
      <input type="file" onChange={(e) => handleRecognition(e.target.files[0])} />
    </div>
  );
}

export default FacialRecognition;

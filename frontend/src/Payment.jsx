import React from 'react';
import axios from 'axios';

function Payment() {
  const handlePayment = () => {
    axios.post('http://your-api-url.com/api/payment/', {
      // Informações do pagamento
    })
    .then(response => {
      console.log("Payment successful!");
    })
    .catch(error => {
      console.error("Payment error", error);
    });
  };

  return (
    <button onClick={handlePayment}>Pay</button>
  );
}

export default Payment;

import { useState } from 'react';
import './Text.css';

function Text() {
  // State to store the value of the textbox
  const [inputValue, setInputValue] = useState('');
  // State to store the prediction result
  const [predictionResult, setPredictionResult] = useState('');

  // Function to handle changes in the textbox
  const handleChange = (event) => {
    setInputValue(event.target.value);
  };

  // Function to handle button click
  const handlePrediction = async () => {
    try {
      const response = await fetch('http://localhost:5000/predicciones', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ resena: inputValue }),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch prediction');
      }

      const data = await response.json();
      setPredictionResult(`Predicción: ${data.prediccion}, Probabilidad: ${data.probabilidad}`);
    } catch (error) {
      console.error('Error predicting:', error);
    }
  };

  return (
    <div>
        {/* Header */}
      <header className="header">
        <img src="/flight.png" alt="Flight" />
        <span>Tourify</span>
      </header>

      {/* Imágenes */}
      <div className="image-container">
        <img src="/trip1.jpg" alt="Trip 1" className="image" />
        <img src="/trip2.jpg" alt="Trip 2" className="image" />
        <img src="/trip3.jpg" alt="Trip 3" className="image" />
      </div>
       
      <div className="textbox-container">
        {/* Textbox */}
        <input
          type="text"
          value={inputValue}
          onChange={handleChange}
          placeholder="Ingrese la reseña aquí..."
          className="textbox"
        />
        
        {/* Button */}
        <button onClick={handlePrediction} className="button">Predecir</button>
      </div>

      {/* Display prediction result */}
      <div>{predictionResult}</div>
    </div>
  );
}

export default Text;

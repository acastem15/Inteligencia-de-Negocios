import { useState } from 'react';

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
        body: JSON.stringify({ text: inputValue }),
      });

      if (!response.ok) {
        throw new Error('Failed to fetch prediction');
      }

      const data = await response.json();
      // Assuming your backend returns an object with keys "prediction" and "probability"
      setPredictionResult(`Prediction: ${data.clasificacion}, Probability: ${data.probabilidad}`);
    } catch (error) {
      console.error('Error predicting:', error);
    }
  };

  return (
    <div>
      {/* Textbox */}
      <input
        type="text"
        value={inputValue}
        onChange={handleChange}
        placeholder="Enter text here..."
      />
      
      {/* Button */}
      <button onClick={handlePrediction}>Predecir</button>

      {/* Display prediction result */}
      <div>{predictionResult}</div>
    </div>
  );
}

export default Text;

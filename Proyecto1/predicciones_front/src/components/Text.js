import { useState } from 'react';
import './Text.css';

function Text() {

  const [inputValue, setInputValue] = useState('');
  const [predictionResult, setPredictionResult] = useState('');
  const [pingStatus, setPingStatus] = useState('');

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

      setPredictionResult(`Predicción(1-peor y 5-mejor): ${data.prediccion}`);

    } catch (error) {
      console.error('Error predicting:', error);
    }
  };

  const checkAppStatus = async () => {
    try {
      const response = await fetch('http://localhost:5000/predicciones/ping');

      if (!response.ok) {
        throw new Error('Failed to ping the application');
      }

      const data = await response.text();

      if (data === 'Pong!') {
        setPingStatus('La aplicación está funcionando bien!');
      } else {
        setPingStatus('La aplicación está funcionando bien!');
      }
    } catch (error) {
      console.error('Error checking app status:', error);
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

      {/* Texto */}

      <div style={{width: "100%",height: "700px"}}>
        <div style={{width: "70%", height: "100px",float: "left" }}> 
          <h1 className="title">Bienvenido a Tourify</h1>
          <p className="subtitle">¡Descubre los secretos para tener a un turista feliz!</p>
            {/* Descripción */}
          <div className="description-container">
            <div className="description">
              <p><strong>¿Te interesa impulsar el turismo en Colombia?</strong></p>
              <p>Nuestra aplicación está diseñada para ayudarte a explorar y promover los destinos turísticos más increíbles de nuestro país.</p>
              
              <p><strong>¿Quiénes pueden beneficiarse de esta aplicación?</strong></p>
              <p>Principalmente, el personal del Ministerio de Comercio, Industria y Turismo de Colombia, así como miembros de la Asociación Hotelera y Turística de Colombia (COTELCO), y gerentes y propietarios de cadenas hoteleras como Hilton, Hoteles Estelar, Holiday Inn, y hoteles más pequeños ubicados en varios municipios de Colombia.</p>
              
              <p><strong>¿Qué puedes hacer con nuestra aplicación?</strong></p>
              <p>Podrás analizar las características de los sitios turísticos que influyen en su atractivo para los turistas. ¿Quieres comparar estos sitios con otros que han recibido bajas recomendaciones? ¡Puedes hacerlo aquí también! Además, nuestra aplicación te ayudará a determinar la calificación potencial de un sitio por parte de los turistas.</p>
              
              <p><strong>¿Por qué es importante esta aplicación para ti?</strong></p>
              <p>Porque te proporcionará información valiosa y análisis predictivos que pueden utilizarse para identificar oportunidades de mejora. ¿Quieres aumentar la popularidad de los sitios turísticos y fomentar el turismo en Colombia? ¡Entonces esta aplicación es tu aliado perfecto!</p>
              
              <p><strong>¡Únete a nosotros y comienza a descubrir las maravillas de Colombia hoy mismo!</strong></p>
            </div>
          </div>
        </div>
        <div style={{marginLeft: '30%', height: '100px'}}> 
          <div className="review-container">
            <h2>Escribe tu reseña y nuestro modelo predecirá que tan contento esta tu cliente:</h2>
            <div className="review-box">
              {/* Cuadro de texto */}
              <input
                  type="text"
                  value={inputValue}
                  onChange={handleChange}
                  placeholder="Ingrese la reseña aquí..."
                  className="textbox"
                />
                {/* Botón de predicción */}
              <button onClick={handlePrediction} className="button">Predecir</button>
              {/* Resultado de la predicción */}
               {predictionResult}
              
              </div>
              
              
            
          </div>
        </div>

      </div>

      
      <div>
      <div style={{width: "100%",height: "800px"}}>
      <h1 className="title">Características relevantes por clase</h1>
        <div style={{width: "50%", height: "100px",float: "left" }}> 
        <h1 className="title">Calificación 1</h1>
          <img src="/clase1.png" alt="" />
        </div>
        <div style={{marginLeft: '50%', height: '100px'}}> 
        <h1 className="title">Calificación 2</h1>
          <img src="/clase 2.png" alt="" />
        </div>
    </div>
    <div style={{width: "100%",height: "800px"}}>
      <div style={{width: "50%", height: "100px",float: "left" }}> 
        <h1 className="title">Calificación 3</h1>
          <img src="/clase 3.png" alt="" />
        </div>
        <div style={{marginLeft: '50%', height: '100px'}}> 
        <h1 className="title">Calificación 4</h1>
          <img src="/clase4.png" alt="" />
        </div>
    </div>
    <div style={{width: "100%",height: "800px"}}>
    <h1 className="title">Calificación 5</h1>
          <img src="/clase5.png" alt=""  />
    </div>
    </div>

      {/* Cuadro de texto y botón de predicción */}
      <div className="textbox-container">
         {/* Botón de verificación de estado de la aplicación */}
         <button onClick={checkAppStatus} className="button">Verificar estado de la aplicación</button>
        {/* Estado de la aplicación */}
      <div>{pingStatus}</div>
      </div>
    </div>
  );
}

export default Text;


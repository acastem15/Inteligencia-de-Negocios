import React from 'react';
import './App.css';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Text from './components/Text';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Text />}/>
        </Routes>
      </ BrowserRouter>
    </div>
  );
}

export default App;
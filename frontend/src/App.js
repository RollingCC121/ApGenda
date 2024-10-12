import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import './App.css';
import Login from './login';
import Register from './register';
import Panel from './panel';
import { AuthProvider } from './Authcontext';
import PrivateRoute from './PrivateRoute';

function App() {
  return (
    <Router>
      <AuthProvider>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/panel" element={<PrivateRoute><Panel /></PrivateRoute>} />
          <Route path="/" element={<Login />} />
        </Routes>
      </AuthProvider>
    </Router>
  );
}

export default App;


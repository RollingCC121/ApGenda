import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from './Authcontext';
import { TextField, Button, Container, Typography, Box } from '@mui/material';

const Login = () => {
    const [correo, setCorreo] = useState('');
    const [password, setPassword] = useState('');
    const [errors, setErrors] = useState({});
    const { login } = useAuth();
    const navigate = useNavigate();

    const validate = () => {
        const errors = {};
        if (!correo) {
            errors.correo = 'El correo es obligatorio';
        } else if (!/\S+@\S+\.\S+/.test(correo)) {
            errors.correo = 'El correo no es válido';
        }
        if (!password) {
            errors.password = 'La contraseña es obligatoria';
        }
        return errors;
    };

    const handleLogin = async () => {
        const validationErrors = validate();
        if (Object.keys(validationErrors).length > 0) {
            setErrors(validationErrors);
            return;
        }

        try {
            const response = await fetch('http://localhost:8001/api/login', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ correo, password })
            });

            if (response.ok) {
                const data = await response.json();
                login(data.user); // Actualiza el estado de autenticación
                navigate('/panel'); // Redirige al panel
            } else {
                alert('Credenciales incorrectas');
            }
        } catch (error) {
            console.error('Error al realizar la solicitud:', error);
            alert('Error al conectar con el servidor');
        }
    };

    return (
        <Container maxWidth="xs">
            <Box
                display="flex"
                flexDirection="column"
                alignItems="center"
                justifyContent="center"
                minHeight="100vh"
            >
                <Typography variant="h4" component="h1" gutterBottom>
                    Login
                </Typography>
                <TextField
                    label="Correo"
                    variant="outlined"
                    margin="normal"
                    fullWidth
                    value={correo}
                    onChange={(e) => setCorreo(e.target.value)}
                    error={!!errors.correo}
                    helperText={errors.correo}
                />
                <TextField
                    label="Password"
                    type="password"
                    variant="outlined"
                    margin="normal"
                    fullWidth
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    error={!!errors.password}
                    helperText={errors.password}
                />
                <Button
                    variant="contained"
                    color="primary"
                    fullWidth
                    onClick={handleLogin}
                    sx={{ mt: 2 }}
                >
                    Login
                </Button>
                <Button
                    variant="text"
                    color="secondary"
                    fullWidth
                    onClick={() => navigate('/register')}
                    sx={{ mt: 1 }}
                >
                    Register
                </Button>
            </Box>
        </Container>
    );
};

export default Login;

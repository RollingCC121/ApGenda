import React from 'react';
import { useAuth } from './Authcontext';

const Panel = () => {
    const { logout } = useAuth();

    return (
        <div>
            <h2>Panel</h2>
            <p>Bienvenido al panel de usuario</p>
            <button onClick={logout}>Logout</button>
        </div>
    );
};

export default Panel;
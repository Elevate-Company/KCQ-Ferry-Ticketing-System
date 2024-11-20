import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import '../css/login.css';
import logo from '../assets/logo.png';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const navigate = useNavigate();

    const handleSubmit = (event) => {
        event.preventDefault();

        console.log('Username:', username);
        console.log('Password:', password);

        if (username && password) {
            navigate('/dashboard');
        }
    };

    return (
        <div className="login-container">
            <img src={logo} alt="Logo" className="logo" />
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    placeholder="Username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    required
                />
                <input
                    type="password"
                    placeholder="Password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                />
                <button type="submit">Login</button>
            </form>
            <p>
                <a href="/forgot-password">Forgot Password?</a>
            </p>
        </div>
    );
}

export default Login;

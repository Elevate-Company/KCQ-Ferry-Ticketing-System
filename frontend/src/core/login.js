import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Import useNavigate from react-router-dom
import '../css/login.css'; // Ensure your CSS file is imported
import logo from '../assets/logo.png'; // Updated path

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate(); // Initialize the navigate function

  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle login logic here
    console.log('Username:', username);
    console.log('Password:', password);
    
    // Simulate successful login and route to dashboard
    // You can replace this with actual authentication logic
    if (username && password) {
      navigate('/dashboard'); // Redirect to Dashboard
    }
  };

  return (
    <div className="login-container">
      <img src={logo} alt="Logo" className="logo" /> {/* Display logo above the form */}
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
        <a href="/forgot-password">Forgot Password?</a> {/* Link to the forgot password page */}
      </p>
    </div>
  );
}

export default Login;

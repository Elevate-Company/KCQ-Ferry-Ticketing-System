import React from 'react';
import Navbar from './navbar'; // Import Navbar

function DashboardScreen() {
  return (
    <div>
      <Navbar /> {/* Navbar included here */}
      <h1>Welcome to the Dashboard!</h1>
      <p>Your content goes here.</p>
    </div>
  );
}

export default DashboardScreen;

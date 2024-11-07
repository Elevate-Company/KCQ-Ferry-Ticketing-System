import React from 'react';
import Navbar from './navbar'; // Import Navbar
import DashCard from './dashcard'; // Import DashCard component
import '../css/dashboard.css'; // Import custom CSS if needed

function DashboardScreen() {
  return (
    <>
      <Navbar /> {/* Navbar included here */}
      <DashCard /> {/* This will render the DashCard component without additional wrappers */}
    </>
  );
}

export default DashboardScreen;

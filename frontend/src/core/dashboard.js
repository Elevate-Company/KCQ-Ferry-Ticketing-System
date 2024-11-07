import React from 'react';
import Navbar from './navbar'; // Import Navbar
import DashCard from './dashcard'; // Import DashCard component

function DashboardScreen() {
  return (
    <div>
      <Navbar /> {/* Navbar included here */}
     
      
      {/* Add DashCard component here */}
      <DashCard /> {/* This will render your DashCard component */}
    </div>
  );
}
                              
export default DashboardScreen;

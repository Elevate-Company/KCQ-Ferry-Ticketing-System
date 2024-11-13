import React from 'react';
import '../../css/dashboard.css';  // Corrected path to dashboard.css
import DashCard from './dashcard'; // Corrected import path for DashCard
import Navbar from '../navbar';  // Import the Navbar component

function Dashboard() {
  return (
    <div>
      <Navbar />  {/* Add Navbar here */}
      <DashCard />  {/* Keep your DashCard here */}
    </div>
  );
}

export default Dashboard;

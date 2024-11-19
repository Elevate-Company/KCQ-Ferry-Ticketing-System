// frontend/src/core/Settings.js
import React from 'react';
import Navbar from '../navbar';  // Import the Navbar component
import ProfileCard from './profilecard';  // Ensure correct case and path


function Settings() {
  return (
    <div>
      <Navbar />
      <ProfileCard />  {/* Render the ProfileCard component here */}
    </div>
  );
}

export default Settings;

// frontend/src/core/Profile.js
import React from 'react';
import Navbar from './navbar'; 

function Profile() {
  return (
    <div>
      <Navbar /> {/* Navbar included here */}
      <h1>User Profile</h1>
      <p>This is the Profile page content.</p>
    </div>
  );
}

export default Profile;

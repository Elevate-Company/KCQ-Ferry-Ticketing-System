// src/core/navbar.js

import React from 'react';
import '../css/navbar.css'; // Ensure this path points to your CSS file
import profileImage from '../assets/profile.png'; // Replace with the actual path to your profile image

function Navbar() {
  return (
    <div className="navbar-card">
      <div className="search-container">
        <i className="fas fa-search search-icon"></i> {/* Font Awesome search icon */}
        <input type="text" placeholder="Search..." className="search-input" />
      </div>
      <div className="notification-profile">
        <i className="fas fa-bell notification-icon"></i> {/* Font Awesome bell icon */}
        <div className="profile-avatar">
          <img src={profileImage} alt="Profile" className="avatar" />
        </div>
      </div>
    </div>
  );
}

export default Navbar;

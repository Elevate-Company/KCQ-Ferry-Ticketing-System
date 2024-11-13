import React from 'react';
import '../css/navbar.css';
import profileImage from '../assets/avatar.png';

function Navbar() {
  return (
    <div className="navbar-card1">
      <div className="search-container">
        <i className="fas fa-search search-icon"></i> {}
        <input type="text" placeholder="Search..." className="search-input" />
      </div>
      <div className="notification-profile">
        <i className="fas fa-bell notification-icon"></i> {}
        <div className="profile-avatar">
          <img src={profileImage} alt="Profile" className="avatar" />
        </div>
      </div>
    </div>
  );
}

export default Navbar;

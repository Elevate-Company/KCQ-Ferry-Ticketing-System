import React from 'react';
import '../css/tripcard.css';

function Tripcard({ from, destination, boatImage }) {
  return (
    <div className="navbar-card">
      {/* Profile avatar (boat image) */}
      <div className="profile-avatar">
        <img src={boatImage} alt="Boat" className="avatar" />
      </div>

      {/* "From" Section */}
      <div className="text-content">
        <p>From</p>
        <div className="h6-container">
          <h6>{from}</h6>
        </div>
      </div>

      {/* Horizontal Dashed Line Separator */}
      <div className="separator"></div>

      {/* "To" Section */}
      <div className="text-content">
        <p>To</p>
        <div className="h6-container">
          <h6>{destination}</h6>
        </div>
      </div>
    </div>
  );
}

export default Tripcard;

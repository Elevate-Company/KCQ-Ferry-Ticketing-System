import React from 'react';
import '../../css/dashboard/tripcard.css';

function Tripcard({ from, destination, boatImage, date = "12/25/2024", boatNumber = "PBO-1234" }) {
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

      {/* Date, Boat Number, and Pumboat Express Section */}
      <div className="date-content">
        <p>Date</p>
        <div className="date-boat-container">
          <h6>{date}</h6>
          <div className="boat-info">
            <p className="boat-number">{boatNumber}</p>
            <p className="boat-name">Pumboat Express</p> {/* New text added here */}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Tripcard;

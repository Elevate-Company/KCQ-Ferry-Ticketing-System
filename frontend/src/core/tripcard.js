import React from 'react';
import '../css/tripcard.css';

function Tripcard({ from, destination, boatImage }) {
  return (
    <div className="navbar-card">
      <div className="notification-profile">
        {/* Profile avatar (boat logo image) */}
        <div className="profile-avatar">
          <img src={boatImage} alt="Boat" className="avatar" />
        </div>

        {/* Text content on the right of the image */}
        <div className="text-content">
          <p>From</p>  {/* 'From' text above destination */}

          <div className="h6-container">
            <h6>{from}</h6>  {/* From destination text */}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Tripcard;

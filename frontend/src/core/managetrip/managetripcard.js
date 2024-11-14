import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'; // Ensure Bootstrap is loaded
import '../../css/managetripcard.css'; // Import the custom CSS
import boatLogo from '../../assets/boatlogo.png'; // Import your logo

function ManageTripCard() {
  return (
    <div className="card empty-card">
      <div className="card-body">
        {/* Checkbox on the left */}
        <input type="checkbox" className="card-checkbox" />

        {/* Boat logo */}
        <img src={boatLogo} alt="Boat Logo" className="boat-logo" />

        {/* From component with text on the left */}
        <div className="from-component">
          <p className="from-text">From</p>
          <h4 className="destination">Cebu</h4>
        </div>
      </div>
    </div>
  );
}

export default ManageTripCard;

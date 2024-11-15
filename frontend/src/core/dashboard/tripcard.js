import React from 'react';
import '../../css/dashboard/tripcard.css';

function Tripcard({ from, destination, boatImage, date = "12/25/2024", boatNumber = "PBO-1234" }) {
  return (
    <div className="card empty-card-tripcard">
      <div className="card-body1">
        {/* Checkbox on the left */}
        <input type="checkbox" className="card-checkbox-tripcard" />

        {/* Boat logo */}
        <img src={boatImage} alt="Boat Logo" className="boat-logo-tripcard" />

        {/* From component with text on the left */}
        <div className="from-component-tripcard">
          <p className="from-text-tripcard">From</p>
          <h4 className="from-destination-tripcard">Cebu</h4>
        </div>

        {/* Horizontal dashed line separator */}
        <div className="separator-tripcard" />

        {/* To component with text on the left */}
        <div className="to-component-tripcard">
          <p className="to-text">To</p>
          <h4 className="to-destination">Cebu</h4>
        </div>

        {/* Departure date component with ID */}
        <div className="departure-date-component-tripcard mt-3">
          <h4 className="departure-date-tripcard">January 15, 2024</h4>
          <h4 className="departure-id-tripcard">PBO-1234</h4>
          <h4 className="departure-text-tripcard">Pumboat Express</h4>
          <h4 className="departure-capacity-tripcard">150</h4>
        </div>

        {/* Vertical separator, trash icon, and View Details button */}
        <div>
          <button type="button" className="view-details-button-tripcard">
            View Details
          </button>
        </div>
      </div>
    </div>
  );
}

export default Tripcard;

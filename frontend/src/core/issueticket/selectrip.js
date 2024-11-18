import React from 'react';
import '../../css/selectrip.css'; // Import the CSS file for styling
import boatLogo from '../../assets/boatlogo.png'; // Import the image

function SelectTrip() {
  return (
    <div className="select-trip-container">
      {/* Empty Card */}
      <div className="card-select-empty">
        {/* Round Checkbox */}
        <input type="checkbox" className="round-checkbox" />

        <div className="card-content-selecttrip">
          {/* Boat Logo and From/To Content in a single row */}
          <div className="boat-from-to-container">
            {/* Boat Logo Section */}
            <img src={boatLogo} alt="Boat Logo" className="selectriplogo" />

            {/* From/To Content Section */}
            <div className="from-to-component">
              {/* From Section */}
              <div className="from-section">
                <p>From</p>
                <h4>Cebu</h4>
              </div>

              {/* Dashed Separator */}
              <div className="dashed-separator mt-4"></div>

              {/* To Section */}
              <div className="to-section">
                <p>To</p>
                <h4>Bantayan</h4>
              </div>
            </div>
          </div>

          {/* Additional Information Below */}
          <div className="additional-info mt-4">
            <div className="date-section">
              <h4>January 15, 2024</h4>
            </div>
             <p></p>
            <div className="boat-number-section">
              <h4>PBO-1234</h4>
            </div>

            <div className="boat-type-section">
              <h4>Pumboat Express</h4>
            </div>

            <div className="price-section">
              <h4 className="price">PHP 1,999</h4>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default SelectTrip;

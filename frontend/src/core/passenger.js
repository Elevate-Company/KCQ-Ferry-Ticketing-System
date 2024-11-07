import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'; // Ensure Bootstrap is imported
import '../css/passenger.css'; // Import the custom CSS
import personImage from '../assets/person.png'; // Import the image

function Passenger() {
  return (
    <div className="card passenger-card border-0 mb-4 col-12 col-md-6 col-lg-4 position-relative">
      {/* Image positioned in the top-left corner */}
      <img 
        src={personImage} 
        alt="Person Icon" 
        className="passenger-image" 
      />
      
      {/* Card body for passenger information */}
      <div className="card-body passenger-card-body">
        <h4 className="passenger-title">Number of Passengers</h4>
      </div>
    </div>
  );
}

export default Passenger;

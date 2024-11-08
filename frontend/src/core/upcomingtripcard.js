import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';  // Import Bootstrap

function UpcomingTripCard() {
  return (
    <div className="card shadow-sm border-0 mb-4 col-12 col-md-6 col-lg-4">
      <div className="card-body">
        {/* Add title text "Upcoming Trips" */}
        <h5 className="card-title">Upcoming Trips</h5>
        {/* You can add more content here */}
      </div>
    </div>
  );
}

export default UpcomingTripCard;

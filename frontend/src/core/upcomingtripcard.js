import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';  // Import Bootstrap
import '../css/upcomingtripcard.css';  // Import the CSS file for custom styles

function UpcomingTripCard() {
  return (
    <div className="container">
      <div className="row">
        {/* Render a single card with the header inside */}
        <div className="col-12 col-md-6 col-lg-6"> {/* Increased width for the card */}
          <div className="card shadow-lg border-0 mb-4">
            <div className="card-body">
              <div className="col-12">
                <h5 className="mb-4">Upcoming Trips</h5>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default UpcomingTripCard;

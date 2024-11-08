import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';  // Import Bootstrap
import '../css/upcomingtripcard.css';  // Import the CSS file for custom styles

function UpcomingTripCard() {
  return (
    <div className="container-fluid"> {/* Adjust container to fluid for full-width on larger screens */}
      <div className="row justify-content-center"> {/* Center card on larger screens */}
        {/* Card column sizing adjusted for responsiveness */}
        <div className="col-12 col-md-10 col-lg-8">
          <div className="card shadow-lg border-0 mb-4 responsive-card">
            <div className="card-body">
              <div className="col-12">
                <h5 className="mb-4">Upcoming Trips</h5>
                {/* Additional content can be placed here */}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default UpcomingTripCard;

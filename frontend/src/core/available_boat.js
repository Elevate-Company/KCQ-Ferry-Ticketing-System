import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'; // Ensure Bootstrap is imported

function AvailableBoat() {
  return (
    <div className="container mt-4">

      <div className="row justify-content-center">
        <div className="col-md-4 mb-4">
          <div className="card shadow-sm border-0">
            <div className="card-body">

            <h2 className="text-center mb-4">Available Boats</h2>
              <h5 className="card-title">Number of Available Boats</h5>
              <p className="card-text" style={{ fontSize: '1.5rem', fontWeight: 'bold' }}>
                10 Boats Available {/* Replace with actual number if dynamic */}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default AvailableBoat;

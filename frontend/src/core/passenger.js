import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'; // Ensure Bootstrap is imported

function Passenger() {
  return (
    <div className="card shadow-sm border-0 mb-4 col-12 col-md-6 col-lg-4 position-relative">
      {/* Card body for passenger information */}
      <div className="card-body">
        <h2 className="text-center mb-4">Passenger Information</h2>
        <h5 className="card-title">Number of Passengers</h5>
        <p className="card-text" style={{ fontSize: '1.5rem', fontWeight: 'bold' }}>
          150 Passengers {/* Replace with dynamic value if necessary */}
        </p>
      </div>
    </div>
  );
}

export default Passenger;

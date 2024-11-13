import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'; // Make sure to import Bootstrap if not already imported

function ManageTripCard() {
  return (
    <div className="card" style={{ width: '18rem', margin: '20px' }}>
      <div className="card-body">
        {/* Content of the card */}
        <h5 className="card-title">Trip Title</h5>
        <p className="card-text">Details of the trip will go here.</p>
      </div>
    </div>
  );
}

export default ManageTripCard;

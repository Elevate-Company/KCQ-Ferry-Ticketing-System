import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'; // Ensure Bootstrap is imported

function TicketSold() {
  const ticketsSold = 1200;  // Set the number of tickets sold

  return (
    <div className="card shadow-sm border-0 mb-4" style={{ width: '100%', maxWidth: '45%' }}>  {/* Removed solid border */}
      <div className="card-body">
        <h5 className="card-title">Total Tickets Sold This Month:</h5>
        <p className="card-text">{ticketsSold} Tickets</p>
      </div>
    </div>
  );
}

export default TicketSold;

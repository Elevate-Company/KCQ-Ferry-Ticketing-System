import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css'; // Ensure Bootstrap is imported
import ticketImage from '../../assets/ticket.png'; // Corrected import path

function TicketSold() {
  const ticketsSold = 1200;  // Set the number of tickets sold

  return (
    <div className="card shadow-sm border-0 mb-4 col-12 col-md-6 col-lg-4 position-relative">
      {/* Image displayed at the top left corner */}
      <img 
        src={ticketImage} 
        alt="Ticket" 
        style={{
          position: 'absolute', 
          top: '10px', 
          left: '10px',  // Positioned to the top-left
          width: '50px',  // Adjust size as needed
          height: 'auto',
          zIndex: 1  // Ensures the image stays on top
        }} 
      />
      <div className="card-body mt-5 fade-in-up">
        <h5 className="card-title">Total Tickets Sold This Month</h5>
        <p className="card-text">{ticketsSold} Tickets</p>
        <p>Today</p>
      </div>
    </div>
  );
}

export default TicketSold;

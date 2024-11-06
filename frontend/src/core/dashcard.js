import React from 'react';
import '../css/dashcard.css';  // Import custom CSS for additional styling
import TicketSales from './ticket_sales';  // Import TicketSales
import TicketSold from './ticket_sold';    // Import TicketSold

const DashCard = () => {
  return (
    <div className="container mt-4">
      <div className="row justify-content-center">
        <div className="col-md-12 col-lg-8"> {/* Larger card for both pieces of data */}
          <div className="card shadow-none border-0 mb-4">  {/* No shadow or border on DashCard */}
            <div className="card-body">
              <h2 className="card-title">Welcome, Employee Name!</h2>
              
              {/* Container to hold the cards horizontally on large screens and vertically on smaller screens */}
              <div className="d-flex flex-column flex-md-row justify-content-between">
                {/* Left Side - Total Sales */}
                <TicketSales />  
                
                {/* Right Side - Tickets Sold */}
                <TicketSold />   
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashCard;

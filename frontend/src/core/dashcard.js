import React from 'react';
import '../css/dashcard.css';  // Import custom CSS for additional styling
import TicketSales from './ticket_sales';  // Import TicketSales
import TicketSold from './ticket_sold';    // Import TicketSold
import AvailableBoat from './available_boat'; // Import AvailableBoat
import Passenger from './passenger'; // Import Passenger component
import UpcomingTripCard from './upcomingtripcard'; // Import UpcomingTripCard

const DashCard = () => {
  return (
    <div className="container mt-4">
      <div className="row justify-content-center">
        <div className="col-md-12 col-lg-15"> {/* Adjusted width of the card on large screens */}
          <div className="card no-shadow-no-border mb-4">  {/* Removed shadow and border */}
            <div className="card-body">
              <h2 className="card-title">Welcome, Employee Name!</h2>

              {/* Container to hold the cards horizontally on large screens and vertically on smaller screens */}
              <div className="d-flex flex-column flex-md-row justify-content-between">
                {/* Left Side - Total Sales */}
                <TicketSales />  

                {/* Right Side - Tickets Sold */}
                <TicketSold />   
              </div>

              {/* New Card - Available Boats and Passengers aligned horizontally */}
              <div className="d-flex flex-column flex-md-row mt-4 justify-content-between">
                {/* Available Boats component aligned horizontally on desktop, vertically on mobile */}
                <AvailableBoat />
                
                {/* Passenger component aligned horizontally with Available Boats */}
                <Passenger />
              </div>

              {/* New Upcoming Trip Card */}
              <div className="mt-4">
                <UpcomingTripCard />
              </div>
            </div>
          </div>
        </div>
      </div> 
    </div>
  );
};

export default DashCard;

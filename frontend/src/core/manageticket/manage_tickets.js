import React from 'react';
import '../../css/manageticket/manageticket.css'; // Import CSS file for styling
import TicketCard from './ticketcard'; // Import TicketCard component

function ManageTrips() {
  return (
    <div className="manage-trips-container">
      {/* Header, Search, and Dropdown in a single row */}
      <div className="header-search-dropdown-row">
        {/* Header */}
        <h1 className="header-ticket">Manage Ticket</h1>

        {/* Container for Search and Dropdown on the right */}
        <div className="search-dropdown-container">
          {/* Search input */}
          <input type="text" className="search-input-ticket" placeholder="Search Trip..." />

          {/* Dropdown filter */}
          <select className="filter-dropdown-ticket">
            <option value="all">All</option>
            <option value="upcoming">Upcoming</option>
            <option value="completed">Completed</option>
            <option value="cancelled">Cancelled</option>
          </select>
        </div>
      </div>

      {/* Empty Card with specified content */}
      <div className="empty-card-ticket">
        <div className="card-content-ticket">
          <div className="destination-ticket">DESTINATION</div>
          <div className="destination-ticket">CUSTOMER</div>
          <div className="destination-ticket">ID</div>
          <div className="boat-type-ticket">TYPE BOAT</div>
          <div className="capacity-ticket">CAPACITY</div>
        </div>
      </div>

      {/* Add TicketCard here to display individual trip tickets */}
      <div className="ticket-cards-container">
        <TicketCard />
        <TicketCard />
        <TicketCard />
        {/* Add as many TicketCard components as needed */}
      </div>
    </div>
  );
}

export default ManageTrips;

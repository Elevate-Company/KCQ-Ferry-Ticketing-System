import React from 'react';
import '../css/managetrips.css';  // Import the CSS file for ManageTrips
import TripMenu from './trip_menu';  // Import TripMenu component

function ManageTrips() {
  return (
    <div className="manage-trips-container">
      {/* Header and Search */}
      <div className="header-container">
        <h1 className="header">All Trips</h1>
        
        {/* Search component */}
        <input type="text" className="search-input" placeholder="Search Trip..." />
        
        {/* Dropdown filter */}
        <select className="filter-dropdown">
          <option value="all">All</option>
          <option value="upcoming">Upcoming</option>
          <option value="completed">Completed</option>
          <option value="cancelled">Cancelled</option>
        </select>
      </div>

      {/* Display the TripMenu component */}
      <TripMenu className="mt-5" />

    </div>
  );
}

export default ManageTrips;

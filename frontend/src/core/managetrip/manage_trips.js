import React from 'react';
import '../../css/managetrips.css';  // Import the CSS file for ManageTrips
import TripMenu from './trip_menu';  // Import TripMenu component
import ManageTripCard from './managetripcard';  // Correct path for ManageTripCard

function ManageTrips() {
  return (
    <div className="manage-trips-container">
      {/* Header and Search */}
      <div className="header-container">
        <h1 className="header">All Trips</h1>
        
        {/* Search component */}
        <input type="text" className="search-inputt" placeholder="Search Trip..." />
        
        {/* Dropdown filter */}
        <select className="filter-dropdown">
          <option value="all">All</option>
          <option value="upcoming">Upcoming</option>
          <option value="completed">Completed</option>
          <option value="cancelled">Cancelled</option>
        </select>
      </div>

      {/* TripMenu.js */}
      <TripMenu className="mt-5" />

      {/* ManagetripCard.js */}
      <div className="card-container mt-3">
        <ManageTripCard />
      </div>
    </div>
  );
}

export default ManageTrips;

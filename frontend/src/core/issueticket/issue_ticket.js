import React from 'react';
import '../../css/issueticket.css'; // Import the CSS file for styling
import SelectTrip from './selectrip'; // Import the SelectTrip component

function IssueTicket() {
  // Define an array with the number of SelectTrip components you want to render
  const selectTripCount = [1, 2, 3, 4]; // This will render 3 SelectTrip components inside the select card

  return (
    <div className="issue-ticket-container">
      <h1>Issue Ticket</h1>

      {/* Container for cards */}
      <div className="cards-row">
        {/* Select Card with dynamic SelectTrip components */}
        <div className="card-select-issue select-card">
          <div className="card-select">
            Select Trip
          </div>

          {/* Loop through the array and render multiple SelectTrip components inside the select card */}
          {selectTripCount.map((_, index) => (
            <SelectTrip key={index} /> // Render each SelectTrip component dynamically
          ))}

          {/* Arrow positioned at the top-right corner of the Select Card */}
          <div className="arrow-container">
            <button className="arrow" onClick={() => alert('Arrow button clicked!')}>
              &gt;
            </button>
          </div>
        </div>

        {/* Contact Card */}
        <div className="card-contact-issue contact-card">
          <div className="card-contact">
            Contact Info
          </div>
        </div>
      </div>
    </div>
  );
}

export default IssueTicket;

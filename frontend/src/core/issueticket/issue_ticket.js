import React from 'react';
import '../../css/issueticket.css'; // Import the general CSS file
import '../../css/contactinfo.css'; // Import the CSS for Contact Info card
import SelectTrip from './selectrip'; // Import the SelectTrip component

function IssueTicket() {
  // Define an array with the number of SelectTrip components you want to render
  const selectTripCount = [1, 2, 3, 4, 5, 6, 7, 8];

  return (
    <div className="issue-ticket-container mt-5">

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
            <h3>Contact Info</h3>
            {/* Form inputs */}
            <form className="contact-form">
              <label>
                Passenger Name:
                <input type="text" placeholder="Name" />
              </label>
              <label>
                Phone Number:
                <input type="tel" placeholder="Contact number" />
              </label>
              <label>
                Passenger Email:
                <input type="email" placeholder="Email" />
              </label>
              <label>
                Number of Tickets:
                <input type="number" placeholder="Number" />
              </label>
              {/* Horizontal line */}
              <hr />
              <p>Total: PHP 1,999</p>
              <hr />
              {/* Generate Ticket Button */}
              <button type="button" onClick={() => alert('Ticket Generated!')}>
                Generate Ticket
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
}

export default IssueTicket;

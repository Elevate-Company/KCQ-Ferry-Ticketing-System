import React from 'react';
import '../../css/issueticket.css'; // Import the CSS file for styling

function IssueTicket() {
  return (
    <div className="issue-ticket-container">
      <h1>Issue Ticket</h1>

      {/* Container for cards */}
      <div className="cards-row">
        {/* Select Card */}
        <div className="card-select-issue select-card">
          <div className="card-select">
            Select Trip
          </div>

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

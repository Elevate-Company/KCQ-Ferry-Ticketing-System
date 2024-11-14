import React from 'react';


function Tcard({ from, destination, boatImage, date = "12/25/2024", boatNumber = "PBO-1234" }) {
  return (
    <div className="navbar-cardT">
      {/* Profile avatar (boat image) */}
      <div className="profile-avatarT">
        <img src={boatImage} alt="Boat" className="avatarT" />
      </div>

      {/* "From" Section */}
      <div className="text-contentT">
        <p>From</p>
        <div className="h6-containerT">
          <h6>{from}</h6>
        </div>
      </div>

      {/* Horizontal Dashed Line Separator */}
      <div className="separatorT"></div>

      {/* "To" Section */}
      <div className="text-contentT">
        <p>To</p>
        <div className="h6-containerT">
          <h6>{destination}</h6>
        </div>
      </div>

      {/* Date, Boat Number, and Pumboat Express Section */}
      <div className="date-contentT">
        <p>Date</p>
        <div className="date-boat-containerT">
          <h6>{date}</h6>
          <div className="boat-infoT">
            <p className="boat-numberT">{boatNumber}</p>
            <p className="boat-nameT">Pumboat Express</p> {/* New text added here */}
          </div>
        </div>
      </div>
    </div>
  );
}

export default Tcard;

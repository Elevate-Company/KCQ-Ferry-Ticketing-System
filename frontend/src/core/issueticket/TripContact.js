import React, { useState } from "react";
import '../../css/issue_ticket.css';

const Tripcontact = () => {
  const [passengerName, setPassengerName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [email, setEmail] = useState('');
  const [ticketCount, setTicketCount] = useState('1');

  const ticketPrice = 10; // Price per ticket (you can adjust this)

  const totalPrice = ticketPrice * ticketCount;

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(`Form submitted with the following details:
      Name: ${passengerName}
      Phone: ${phoneNumber}
      Email: ${email}
      Tickets: ${ticketCount}`);
  };

  return (
    <div className="Tcontact container mb-5">
      <h2>Contact Information</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="passengerName">Passenger Name</label>
          <input
            type="text"
            id="passengerName"
            className="form-control"
            value={passengerName}
            onChange={(e) => setPassengerName(e.target.value)}
            placeholder="Enter passenger name"
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="phoneNumber">Phone Number</label>
          <input
            type="tel"
            id="phoneNumber"
            className="form-control"
            value={phoneNumber}
            onChange={(e) => setPhoneNumber(e.target.value)}
            placeholder="Enter phone number"
            required
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Passenger Email</label>
          <input
            type="email"
            id="email"
            className="form-control"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter email address"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="ticketCount">Number of Tickets</label>
          <select
            id="ticketCount"
            className="form-control"
            value={ticketCount}
            onChange={(e) => setTicketCount(e.target.value)}
          >
            {[1, 2, 3, 4, 5].map((num) => (
              <option key={num} value={num}>{num}</option>
            ))}
          </select>
        </div>

        <div className="form-group">
          <h4>Total: ${totalPrice}</h4> 
        </div>

        <button type="submit" className="btn btn-primary">Generate Ticket</button>
      </form>
    </div>
  );
};

export default Tripcontact;

import React from 'react';
import Tripselector from './Tripselector';
import Tripcontact from './TripContact';
import '../css/issue_ticket.css'

function IssueTicket() {
  return (
    <div className='Iticks'>
    <Tripselector/>  {}
    <Tripcontact/>  {}
    </div>
  );
}

export default IssueTicket;

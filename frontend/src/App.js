import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './core/components'; // Ensure this path points to the components.js file
import IssueTicket from './core/issue_ticket'; // Ensure this path points to your issue_ticket.js

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/dashboard" element={<Dashboard />} /> {/* Added this line */}
        <Route path="/issue-ticket" element={<IssueTicket />} />
        {/* Add other routes as needed */}
      </Routes>
    </Router>
  );
}

export default App;

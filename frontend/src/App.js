import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Dashboard from './core/dashboard'; // Adjusted path
import IssueTicket from './core/issue_ticket'; // Adjusted path

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/issue-ticket" element={<IssueTicket />} />
      </Routes>
    </Router>
  );
}

export default App;

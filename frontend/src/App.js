import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './core/navbar'; // Import Navbar
import Dashboard from './core/components';
import DashboardScreen from './core/dashboard';
import IssueTicket from './core/issue_ticket';
import ManageTrips from './core/manage_trips';
import ManageTickets from './core/manage_tickets';
import Profile from './core/profile';
import Reports from './core/reports';
import Settings from './core/settings';

function App() {
  return (
    <Router>
      <Navbar /> {/* Navbar at the top */}
      <Routes>
        <Route path="/" element={<Dashboard />}>
          <Route path="dashboard" element={<DashboardScreen />} />
          <Route path="issue-ticket" element={<IssueTicket />} />
          <Route path="manage-trips" element={<ManageTrips />} />
          <Route path="manage-tickets" element={<ManageTickets />} />
          <Route path="profile" element={<Profile />} />
          <Route path="reports" element={<Reports />} />
          <Route path="settings" element={<Settings />} />
        </Route>
      </Routes>
    </Router>
  );
}

export default App;

import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Dashboard from './core/components';
import DashboardScreen from './core/dashboard';
import IssueTicket from './core/issue_ticket';
import ManageTrips from './core/manage_trips';
import ManageTickets from './core/manage_tickets';
import Profile from './core/profile';
import Reports from './core/reports';
import Settings from './core/settings';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  return (
    <Router>
      <Routes>
        {/* Dashboard layout with sidebar */}
        <Route path="/" element={<Dashboard />}>
          {/* Redirect root to /dashboard */}
          <Route index element={<Navigate to="dashboard" replace />} />
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

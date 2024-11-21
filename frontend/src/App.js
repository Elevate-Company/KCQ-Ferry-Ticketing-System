import React from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from 'react-router-dom';
import Login from './core/auth/login';
import Dashboard from './core/components';
import DashboardScreen from './core/dashboard/dashboard';
import IssueTicket from './core/issueticket/issue_ticket';
import ManageTrips from './core/managetrip/manage_trips';
import ManageTickets from './core/manageticket/manage_tickets';
import Profile from './core/profile';
import Reports from './core/reports';
import Settings from './core/settings/settings';
import ProtectedRoute from './components/protectedroute'; // Ensure correct path
import 'bootstrap/dist/css/bootstrap.min.css';

// Authentication checker
const isAuthenticated = () => !!localStorage.getItem('accessToken');

function App() {
    return (
        <Router>
            <Routes>
                {/* Public Route */}
                <Route path="/login" element={<Login />} />

                {/* Protected Routes */}
                <Route
                    path="/"
                    element={
                        <ProtectedRoute isAuthenticated={isAuthenticated}>
                            <Dashboard />
                        </ProtectedRoute>
                    }
                >
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

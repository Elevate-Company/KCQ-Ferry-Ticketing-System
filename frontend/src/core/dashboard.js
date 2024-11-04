import React from 'react';
import { Link } from 'react-router-dom'; // Import Link for routing
import '../css/dashboard.css'; // Ensure this path points to your CSS file
import logo from '../assets/logo.png'; // Adjust the path to your logo

function Dashboard() {
  return (
    <div className="dashboard-container">
      <nav className="sidebar">
        <img src={logo} alt="Logo" className="sidebar-logo" />
        <ul>
          <li><Link to="/dashboard"><i className="fas fa-tachometer-alt"></i> Dashboard</Link></li>
          <li><a href="/issue-ticket"><i className="fas fa-ticket-alt"></i> Issue Ticket</a></li>
          <li><Link to="/manage-trips"><i className="fas fa-ship"></i> Manage Trips</Link></li>
          <li><Link to="/manage-tickets"><i className="fas fa-file-alt"></i> Manage Tickets</Link></li>
          <li><Link to="/profile"><i className="fas fa-user"></i> Profile</Link></li>
          <li><Link to="/reports"><i className="fas fa-chart-line"></i> Reports</Link></li>
          <li><Link to="/settings"><i className="fas fa-cog"></i> Settings</Link></li>
        </ul>
        {/* Need Help Section */}
        <div className="need-help">
          <i className="fas fa-comments"></i>
          <span>Need Help?</span>
        </div>
      </nav>
      <div className="dashboard-content">
        <h1>Welcome to the Dashboard!</h1>
        <p>This is where your main content will go.</p>
      </div>
    </div>
  );
}

export default Dashboard;

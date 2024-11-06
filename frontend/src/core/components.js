import React, { useState } from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import '../css/dashboard.css';  // Import global styles for layout
import '../css/components.css';  // Import sidebar-specific styles
import logo from '../assets/kcq.png';
import dashboardIcon from '../assets/dashboard.png';
import issueTicketIcon from '../assets/issueticket.png';
import manageTicketsIcon from '../assets/managetickets.png';
import manageTripsIcon from '../assets/managetrips.png';
import profileIcon from '../assets/profile.png';
import reportsIcon from '../assets/reports.png';
import settingsIcon from '../assets/setting.png';
import needHelpIcon from '../assets/needhelp.png';

function Components() {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  return (
    <div className="container-fluid">
      <div className="row">
        {/* Sidebar */}
        {isSidebarOpen && (
          <div className="col-md-3 col-lg-2 p-3 sidebar">
            <div className="d-flex justify-content-between align-items-center mb-4">
              <div className="d-flex align-items-center">
                <img src={logo} alt="KCQ Logo" className="sidebar-logo me-2" />
                <span className="h5 text-white">Express</span>
              </div>
              <button onClick={toggleSidebar} className="btn-close-sidebar">
                ×
              </button>
            </div>
            <ul className="nav flex-column">
              <li className="nav-item">
                <NavLink to="/dashboard" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                  <img src={dashboardIcon} alt="Dashboard" className="sidebar-icon me-2" /> Dashboard
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/issue-ticket" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                  <img src={issueTicketIcon} alt="Issue Ticket" className="sidebar-icon me-2" /> Issue Ticket
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/manage-trips" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                  <img src={manageTripsIcon} alt="Manage Trips" className="sidebar-icon me-2" /> Manage Trips
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/manage-tickets" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                  <img src={manageTicketsIcon} alt="Manage Tickets" className="sidebar-icon me-2" /> Manage Tickets
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/profile" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                  <img src={profileIcon} alt="Profile" className="sidebar-icon me-2" /> Profile
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/reports" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                  <img src={reportsIcon} alt="Reports" className="sidebar-icon me-2" /> Reports
                </NavLink>
              </li>
              <li className="nav-item">
                <NavLink to="/settings" className={({ isActive }) => `nav-link ${isActive ? 'active' : ''}`}>
                  <img src={settingsIcon} alt="Settings" className="sidebar-icon me-2" /> Settings
                </NavLink>
              </li>
            </ul>
            <div className="d-flex align-items-center mt-auto need-help">
              <img src={needHelpIcon} alt="Need Help" className="sidebar-icon me-2" />
              <span>Need Help?</span>
            </div>
          </div>
        )}

        {/* Main Content */}
        <div className={`col ${isSidebarOpen ? 'col-md-9 col-lg-10' : 'col-12'} p-4`}>
          <Outlet />
          {!isSidebarOpen && (
            <button onClick={toggleSidebar} className="btn-open-sidebar">
              ☰
            </button>
          )}
        </div>
      </div>
    </div>
  );
}

export default Components;

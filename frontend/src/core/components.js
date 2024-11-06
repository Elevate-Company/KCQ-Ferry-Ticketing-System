import React from 'react';
import { NavLink, Outlet } from 'react-router-dom';
import '../css/dashboard.css';
import logo from '../assets/kcq.png';
import dashboardIcon from '../assets/dashboard.png';
import issueTicketIcon from '../assets/issueticket.png';
import manageTicketsIcon from '../assets/managetickets.png';
import manageTripsIcon from '../assets/managetrips.png';
import profileIcon from '../assets/profile.png';
import reportsIcon from '../assets/reports.png';
import settingsIcon from '../assets/setting.png';
import needHelpIcon from '../assets/needhelp.png';

function Dashboard() {
  return (
    <div className="dashboard-container">
      <nav className="sidebar">
        <div className="sidebar-logo-container">
          <img src={logo} alt="KCQ Logo" className="sidebar-logo" />
          <span className="sidebar-title">Express</span>
        </div>
        <ul>
          <li>
            <NavLink to="/dashboard" className={({ isActive }) => (isActive ? 'active-link' : '')}>
              <img src={dashboardIcon} alt="Dashboard" className="sidebar-icon" /> Dashboard
            </NavLink>
          </li>
          <li>
            <NavLink to="/issue-ticket" className={({ isActive }) => (isActive ? 'active-link' : '')}>
              <img src={issueTicketIcon} alt="Issue Ticket" className="sidebar-icon" /> Issue Ticket
            </NavLink>
          </li>
          <li>
            <NavLink to="/manage-trips" className={({ isActive }) => (isActive ? 'active-link' : '')}>
              <img src={manageTripsIcon} alt="Manage Trips" className="sidebar-icon" /> Manage Trips
            </NavLink>
          </li>
          <li>
            <NavLink to="/manage-tickets" className={({ isActive }) => (isActive ? 'active-link' : '')}>
              <img src={manageTicketsIcon} alt="Manage Tickets" className="sidebar-icon" /> Manage Tickets
            </NavLink>
          </li>
          <li>
            <NavLink to="/profile" className={({ isActive }) => (isActive ? 'active-link' : '')}>
              <img src={profileIcon} alt="Profile" className="sidebar-icon" /> Profile
            </NavLink>
          </li>
          <li>
            <NavLink to="/reports" className={({ isActive }) => (isActive ? 'active-link' : '')}>
              <img src={reportsIcon} alt="Reports" className="sidebar-icon" /> Reports
            </NavLink>
          </li>
          <li>
            <NavLink to="/settings" className={({ isActive }) => (isActive ? 'active-link' : '')}>
              <img src={settingsIcon} alt="Settings" className="sidebar-icon" /> Settings
            </NavLink>
          </li>
        </ul>
        <div className="need-help">
          <img src={needHelpIcon} alt="Need Help" className="sidebar-icon" />
          <span>Need Help?</span>
        </div>
      </nav>

      <div className="dashboard-content">
        <Outlet />
      </div>
    </div>
  );
}

export default Dashboard;

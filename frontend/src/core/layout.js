// src/core/Layout.js
import React from 'react';
import { Outlet } from 'react-router-dom'; // Import Outlet for nested routes
import Dashboard from './dashboard'; // Import your sidebar component
import '../css/dashboard.css'; // Ensure this path points to your CSS file

const Layout = () => {
  return (
    <div className="layout">
      <Dashboard /> {/* Sidebar component */}
      <div className="main-content">
        <Outlet /> {/* This will render the matched child route */}
      </div>
    </div>
  );
};

export default Layout;

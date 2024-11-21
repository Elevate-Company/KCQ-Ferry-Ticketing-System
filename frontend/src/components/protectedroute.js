import React from 'react';
import { Navigate } from 'react-router-dom';

// ProtectedRoute checks if the user is authenticated
const ProtectedRoute = ({ isAuthenticated, children }) => {
    if (!isAuthenticated) {
        return <Navigate to="/login" replace />;
    }

    return children; // If authenticated, show the child component (Dashboard, etc.)
};

export default ProtectedRoute;

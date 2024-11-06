import React from 'react';
import '../css/dashcard.css';  // Import custom CSS for additional styling

const DashCard = () => {
  // Sample data for demonstration
  const totalSales = 1500;
  const totalTickets = 350;

  return (
    <div className="container mt-4">
      <div className="row justify-content-center">
        <div className="col-md-6 col-lg-4">  {/* Bootstrap grid column */}
          <div className="card shadow-sm">
            <div className="card-body">
              <h2 className="card-title">Dashboard Card</h2>
              <div className="card-content">
                <p><strong>Total Sales This Month:</strong> ${totalSales}</p>
                <p><strong>Total Tickets Sold:</strong> {totalTickets} tickets</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default DashCard;

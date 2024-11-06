import React from 'react';
import '../css/ticket_sales.css';

function TicketSales() {
  // Sample sales data
  const totalSales = 1200;
  const salesData = [
    {
      id: 1,
      date: "2024-11-01",
      ticketsSold: 120,
      revenue: "$1,200",
    },
    {
      id: 2,
      date: "2024-11-02",
      ticketsSold: 150,
      revenue: "$1,500",
    },
    {
      id: 3,
      date: "2024-11-03",
      ticketsSold: 180,
      revenue: "$1,800",
    },
  ];

  return (
    <div className="ticket-sales-container">
      <h2>Recent Ticket Sales</h2>
      <div className="ticket-card">
        <p>Total sales this month: ${totalSales}</p>
        <div className="sales-list">
          {salesData.map((sale) => (
            <div key={sale.id} className="sales-item">
              <p><strong>Date:</strong> {sale.date}</p>
              <p><strong>Tickets Sold:</strong> {sale.ticketsSold}</p>
              <p><strong>Revenue:</strong> {sale.revenue}</p>
              <hr />
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}

export default TicketSales;

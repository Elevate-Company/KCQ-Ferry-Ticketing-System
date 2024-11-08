import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';  // Import Bootstrap
import '../css/upcomingtripcard.css';  // Import custom styles
import Tripcard from './tripcard';  // Import Tripcard component

function UpcomingTripCard() {
  // Example data for upcoming trips
  const trips = [
    { id: 1, from: 'Cebu', destination: 'Manila', boatImage: 'boatlogo.png', dashImage: 'dash.png' },
    { id: 2, from: 'Davao', destination: 'Cagayan de Oro', boatImage: 'boatlogo.png', dashImage: 'dash.png' },
    { id: 3, from: 'Iloilo', destination: 'Negros', boatImage: 'boatlogo.png', dashImage: 'dash.png' },
  ];

  return (
    <div className="container-fluid"> {/* Full-width for larger screens */}
      <div className="row justify-content-center"> {/* Center card on larger screens */}
        <div className="col-12 col-md-10 col-lg-12">
          <div className="card shadow-lg border-0 mb-4 responsive-card">
            <div className="card-body">
              <h5 className="mb-4 text-center">Upcoming Trips</h5>
              {/* Map over the trips array to render multiple Tripcards */}
              {trips.map((trip) => (
                <Tripcard
                  key={trip.id}
                  from={trip.from}
                  destination={trip.destination}
                  boatImage={require(`../assets/${trip.boatImage}`)}  // Dynamic boat image path
                  dashImage={require(`../assets/${trip.dashImage}`)}  // Dynamic dash image path
                />
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default UpcomingTripCard;

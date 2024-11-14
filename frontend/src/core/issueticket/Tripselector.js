import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';  // Import Bootstrap
import Tcard from './Tcard';
import "../../css/Tripselector.css";
function Tripselector() {
  const trips = [
    { id: 1, from: 'Cebu', destination: 'North Korea', boatImage: 'boatlogo.png', dashImage: 'dash.png' },
    { id: 2, from: 'Davao', destination: 'Japan', boatImage: 'boatlogo.png', dashImage: 'dash.png' },
    { id: 3, from: 'Iloilo', destination: 'China', boatImage: 'boatlogo.png', dashImage: 'dash.png' },
  ];

  return (
    <div className="container-fluid"> {/* Full-width for larger screens */}
      <div className="row justify-content-center"> {/* Center card on larger screens */}
        <div className="col-12 col-md-10 col-lg-12">
          <div className="card shadow-lg border-0 mb-4 responsive-card">
            <div className="card-body">
              <h5 className="mb-4 d-flex justify-content-start">Select Trip</h5>
              {trips.map((trip) => (
                <Tcard
                  key={trip.id}
                  from={trip.from}
                  destination={trip.destination}
                  boatImage={require(`../../assets/${trip.boatImage}`)}  // Dynamic boat image path
                  dashImage={require(`../../assets/${trip.dashImage}`)}  // Dynamic dash image path
                />
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Tripselector;

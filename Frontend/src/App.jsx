import React, { useState, useEffect } from 'react';
import EventList from './components/EventList';
import './App.css'; // Assuming you have some basic styling in App.css

const API_URL = `${import.meta.env.VITE_APP_BASE_URL}/api/events`;

function App() {
  const [events, setEvents] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [isFirstLoad, setIsFirstLoad] = useState(true);

  useEffect(() => {
    const fetchEvents = async () => {
      if (isFirstLoad) {
        setIsLoading(true); // Show loader only during the first fetch
      }
      try {
        const response = await fetch(API_URL);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setEvents(data);
        setIsFirstLoad(false); // After the first successful fetch, set this to false
      } catch (error) {
        console.error('Error fetching events:', error);
      } finally {
        setIsLoading(false); // Ensure the loader is hidden after the first fetch
      }
    };

    fetchEvents();
    const interval = setInterval(fetchEvents, 15000); // Continue fetching every 15 seconds

    return () => clearInterval(interval);
  }, [isFirstLoad]);

  return (
    <div className="App">
      {isLoading ? (
        <div className="loader-container">
          <div className="loader"></div>
        </div>
      ) : (
        <EventList events={events} />
      )}
    </div>
  );
}

export default App;

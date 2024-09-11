// src/App.jsx
import React, { useState, useEffect } from 'react';
import EventList from './components/EventList';

const API_URL = 'http://127.0.0.1:5000/api/events';

function App() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await fetch(API_URL);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        setEvents(data);
      } catch (error) {
        console.error('Error fetching events:', error);
      }
    };

    fetchEvents();
    const interval = setInterval(fetchEvents, 15000);

    return () => clearInterval(interval);
  }, []);

  return (
    <div className="App">
      <EventList events={events} />
    </div>
  );
}

export default App;



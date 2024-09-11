import React from 'react';
import './EventList.css';

function EventList({ events }) {
  const formatEvent = (event) => {
    const { type, author, from_branch, to_branch, timestamp, repo_name } = event;
    const formattedTimestamp = new Date(timestamp).toLocaleString('en-US', {
      day: 'numeric',
      month: 'long',
      year: 'numeric'
      hour: 'numeric',
      minute: 'numeric',
      hour12: true,
      timeZone: 'UTC',
    });

    switch (type) {
      case 'PUSH':
        return `${author} pushed to "${to_branch}" in ${repo_name} on ${formattedTimestamp} UTC`;
      case 'PULL_REQUEST':
        return `${author} submitted a pull request from "${from_branch}" to "${to_branch}" in ${repo_name} on ${formattedTimestamp} UTC`;
      case 'MERGE':
        return `${author} merged branch "${from_branch}" to "${to_branch}" in ${repo_name} on ${formattedTimestamp} UTC`;
      default:
        return 'Unknown event type';
    }
  };

  return (
    <div className='event-div'>
        <h2>Repository Data</h2>
        <div className="event-list">
        {events.map((event, index) => (
            <div key={index} className={`event-item ${event.type.toLowerCase()}`}>
            {formatEvent(event)}
            </div>
        ))}
        </div>
    </div>
  );
}

export default EventList;


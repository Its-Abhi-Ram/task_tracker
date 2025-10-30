import React, { useEffect, useState } from 'react';
import axios from 'axios';

export default function TaskList() {
  const [tasks, setTasks] = useState([]);
  const [filter, setFilter] = useState({ status: '', priority: '' });

  const fetchTasks = async () => {
    const params = {};
    if (filter.status) params.status = filter.status;
    if (filter.priority) params.priority = filter.priority;
    const res = await axios.get('http://localhost:5000/tasks', { params });
    setTasks(res.data);
  };

  useEffect(() => { fetchTasks(); }, [filter]);

  return (
    <div className='filter'>
      <div className='filter-opt'>
      <select onChange={e => setFilter({ ...filter, status: e.target.value })}>
        <option value="">All Status</option><option>Open</option><option>InProgress</option><option>Done</option>
      </select>
      <select onChange={e => setFilter({ ...filter, priority: e.target.value })}>
        <option value="">All Priority</option><option>Low</option><option>Medium</option><option>High</option>
      </select>
      </div>
      <ul>
        {tasks.map(t => (
          <li key={t.id}>{t.title} — {t.priority} — {t.due_date} — {t.status}</li>
        ))}
      </ul>
    </div>
  );
}

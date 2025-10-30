import React, { useState } from 'react';
import axios from 'axios';

export default function TaskForm({ onAdd }) {
  const [form, setForm] = useState({
    title: '', description: '', priority: 'Medium', due_date: '', status: 'Open'
  });

  const handleChange = e => setForm({ ...form, [e.target.name]: e.target.value });

  const handleSubmit = async e => {
    e.preventDefault();
    await axios.post('http://localhost:5000/tasks', form);
    onAdd();
  };

  return (
    <form onSubmit={handleSubmit}>
      <input name="title" placeholder="Title" onChange={handleChange} required />
      <textarea name="description" placeholder="Description" onChange={handleChange} />
      <select name="priority" onChange={handleChange}>
        <option>Low</option><option>Medium</option><option>High</option>
      </select>
      <input type="date" name="due_date" onChange={handleChange} required />
      <select name="status" onChange={handleChange}>
        <option>Open</option><option>InProgress</option><option>Done</option>
      </select>
      <button type="submit">Add Task</button>
    </form>
  );
}

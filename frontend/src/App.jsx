import React from 'react';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';
import InsightsPanel from './components/InsightsPanel';

import './index.css'

function App() {
  return (
    <div>
      <h1>Task Tracker</h1>
      <TaskForm  />
      <TaskList />
      <InsightsPanel />
    </div>
  );
}

export default App;

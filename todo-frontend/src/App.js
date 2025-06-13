import React, { useEffect, useState } from 'react';
import axios from 'axios';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';

const App = () => {
  const [tasks, setTasks] = useState([]);

  
  useEffect(() => {
    axios.get('http://localhost:5000/tasks')
      .then(res => setTasks(res.data))
      .catch(err => console.error(err));
  }, []);

  
  const addTask = (title) => {
    axios.post('http://localhost:5000/tasks', { title })
      .then(res => setTasks([...tasks, res.data]))
      .catch(err => console.error(err));
  };

  const deleteTask = (id) => {
    axios.delete(`http://localhost:5000/tasks/${id}`)
      .then(() => setTasks(tasks.filter(task => task.id !== id)))
      .catch(err => console.error(err));
  };

  return (
    <div style={{ maxWidth: '600px', margin: '40px auto', textAlign: 'center' }}>
      <h1>Task Management App</h1>
      <TaskForm onAdd={addTask} />
      <TaskList tasks={tasks} onDelete={deleteTask} />
    </div>
  );
};

export default App;

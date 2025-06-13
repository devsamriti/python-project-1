
import React, { useState } from 'react';

const TaskForm = ({ onAdd }) => {
  const [title, setTitle] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (title.trim() !== '') {
      onAdd(title.trim());
      setTitle('');
    }
  };

  return (
    <form onSubmit={handleSubmit} style={{ marginBottom: '20px' }}>
      <input
        type="text"
        placeholder="Enter new task"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        style={{ padding: '8px', width: '250px', marginRight: '10px' }}
      />
      <button type="submit" style={{ padding: '8px 16px' }}>Add Task</button>
    </form>
  );
};

export default TaskForm;

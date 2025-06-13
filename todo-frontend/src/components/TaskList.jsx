
import React from 'react';

const TaskList = ({ tasks, onDelete }) => {
  if (tasks.length === 0) return <p>No tasks added yet!</p>;

  return (
    <ul style={{ listStyleType: 'none', paddingLeft: 0 }}>
      {tasks.map((task) => (
        <li key={task.id} style={{ marginBottom: '10px' }}>
          {task.title}
          <button
            onClick={() => onDelete(task.id)}
            style={{ marginLeft: '15px', cursor: 'pointer' }}
          >
            Delete
          </button>
        </li>
      ))}
    </ul>
  );
};

export default TaskList;

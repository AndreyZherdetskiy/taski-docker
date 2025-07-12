const Task = ({ data, handleEdit, handleDelete }) => {
  return (
    <li className="list-group-item d-flex justify-content-between align-items-center flex-column align-items-start">
      <span
        className={`task-title mr-2 ${data.completed ? "completed-task" : ""}`}
        title={data.description}
      >
        {data.title}
      </span>
      <span className="text-muted small w-100" style={{ wordBreak: 'break-word' }}>
        {data.description}
      </span>
      <span className="align-self-end mt-2">
        <button
          className="btn btn-secondary mr-2"
          onClick={() => handleEdit(data)}
        >
          Edit
        </button>
        <button className="btn btn-danger" onClick={() => handleDelete(data)}>
          Delete
        </button>
      </span>
    </li>
  );
};

export default Task;

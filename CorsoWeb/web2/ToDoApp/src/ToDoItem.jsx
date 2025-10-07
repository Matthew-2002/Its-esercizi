import React, {  useState } from "react";

const TodoItem = ({ task, onDeleteTask, onToggleTask,onUpdateTask}) => {
  const [isEditing, setIsEditing] = useState(false);
  const [editText,setEditText] = useState(task.text);
  const handleSave = () => {
    console.log(editText)
    if(editText.trim()){
      onUpdateTask(task.id,editText)
      setIsEditing(false)
    }else{
      setIsEditing(false)
    }
  };
  return (
    <li className="list-group-item d-flex justify-content-between">
      {isEditing ? (
        <div>
          <input
            type="text"
            className="form-control d-inline-block"
            value={editText}
           onChange={(e)=>setEditText(e.target.value)}
            onBlur={handleSave}
           
            style={{ width: "300px", marginRight: "3px" }}
            autoFocus
          ></input>
          <button
            onClick={() => setIsEditing(false)}
            className="btn btn-danger"
             style={{marginTop: "-6px" }}
          >
            X
          </button>
          
        </div>
      ) : (
        <div>
          <input
            type="checkbox"
            className="form-check-input me-2"
            checked={task.completed}
            onChange={() => {
              onToggleTask(task.id, task.completed);
            }}
          ></input>
          <span
            onDoubleClick={() => setIsEditing(true)}
            style={{ textDecoration: task.completed ? "line-through" : "none" }}
          >
            {task.text}
          </span>
        </div>
      )}

      <button className="btn btn-danger" onClick={() => onDeleteTask(task.id)}>
        Delete
      </button>
    </li>
  );
};

export default TodoItem;
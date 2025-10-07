const API_URL = "http://localhost:3000/tasks";

export const fetchTasksService = async () => {
  const response = await fetch(API_URL);
  if (!response.ok) throw new Error("Errore nella fetch");
  const data = await response.json();
  return data;
};

export const deleteTaskService = async (id) => {
  await fetch(API_URL + "/" + id, { method: "DELETE" });
};

export   const toggleTaskService = async (id, completed) => {
    await fetch(API_URL + "/" + id, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ completed: !completed }),
    });

  };

export  const addTaskService = async (text) => {
    await fetch(API_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text, completed: false }),
    });
  
  };

export  const updateTaskService = async (id, text) => {
    await fetch(API_URL + "/" + id, {
      method: "PATCH",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
  
  };
import React, { useState, useEffect } from "react";
import TodoForm from "./TodoForm";
import TodoList from "./TodoList";
import { fetchTasksService,deleteTaskService,toggleTaskService,addTaskService,updateTaskService } from "./api";

const TodoApp = () => {
  const [tasks, setTasks] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchTasks = async () => {
    try {
      const data = await fetchTasksService();
      setTasks(data);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };

  const deleteTask = async  (id) => {
    await deleteTaskService(id);
    fetchTasks();
  };

  const toggleTask = async (id, completed) => {
    await toggleTaskService(id, completed);
    fetchTasks();
  };
  
  const addTask = async (text) => {
    await addTaskService(text)
    fetchTasks();
  };
const updateTask = async (id, text) => {
    await updateTaskService (id, text)
    fetchTasks();
  };
  useEffect(() => {
    fetchTasks();
  }, []);

  if(loading) return <div className="alert alert-info">Sto caricando....</div>
  if(error) return <div className="alert alert-danger">Errore: {error}</div>

  return (
    <div>
      <h1>Todolist Cloud</h1>
      <TodoForm onAddTask={addTask}></TodoForm>
      <TodoList
        tasks={tasks}
        onDeleteTask={deleteTask}
        onToggleTask={toggleTask}
        onUpdateTask={updateTask}
      ></TodoList>
    </div>
  );
};

export default TodoApp;
import './App.css'
import React, { useState } from 'react'


function App() {

  const [lista, setLista] = useState([]);
  const [toDoItem, setTodoItem] = useState("")

  function catturaModLista(e){
    e.preventDefault()
    setLista([...lista, toDoItem])
    setTodoItem("")
  }

  function catturaModTesto(e){
    setTodoItem(e.target.value)
  }

  return (
    <>
      <div className='container'>
        <h3 className='h3'>To do list:</h3>
          <form onSubmit={catturaModLista}>
            <input onChange={catturaModTesto} className='form-control' type='text' placeholder='Inserisci nuovo elemento' value={toDoItem}>
              </input>
            <button className='btn btn-primary' type='submit'>Aggiungi</button>            
          </form>
          <ul className='list-group'>
            {lista.map((el, index) => {
              return (
                <li key={index} className='list-group-item mio-item'>{el}</li>
              )
            })}
          </ul>
      </div>
    </>
  )
}

export default App

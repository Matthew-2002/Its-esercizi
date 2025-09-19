import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import Saluto from './Saluto'
import CardUtente from './CardUtente'
import Menu from './MenuRistorante'

function App() {
  const [count, setCount] = useState(0)
  const persona=  {
      nome: "ugo",
      email: "rob@rob.it",
      imgUrl: "https://placehold.co/600x400/png",
    }
  const persone = [
    {
      nome: "ugo",
      email: "rob@rob.it",
      imgUrl: "https://placehold.co/600x400/png",
    },
    {
      nome: "Pippo",
      email: "rob@rob.it",
      imgUrl: "https://placehold.co/600x400/png",
    },
    {
      nome: "Gino",
      email: "rob@rob.it",
      imgUrl: "https://placehold.co/600x400/png",
    },
  ];

  return (
    <>
    <Saluto></Saluto>
    <CardUtente
        nome="Roberto"
        email="rob@rob.it"
        imgUrl="https://placehold.co/600x400/png"
      ></CardUtente>
      
      <CardUtente {...persona}></CardUtente>

      <div className="row">
        {persone.map((p) => {
          return (
            <div className="col">
              <CardUtente {...p}></CardUtente>
            </div>
          );
        })}
      </div>

      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
      </div>
      <Menu></Menu>
    </>
  )
}

export default App

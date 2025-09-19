import { useEffect, useState } from "react";


const urlUser = "https://jsonplaceholder.typicode.com/users";
const UserCrud = () => {
  const [users, setUsers] = useState([]);


  const getUsers = () => {
    fetch(urlUser)
      .then((response) => response.json())
      .then((ris) => setUsers(ris));
  };
  useEffect(() => {
    getUsers();
  }, []);


  const deleteUser = (id) => {
    const newUsers = users.filter((u) => u.id !== id);
    if (window.confirm("Sei sicuro di voler cancellare questo utente?")) {
      setUsers(newUsers);
    }
  };


  return (
    <>
      <div className="container">
        <h1>USER CRUD</h1>


        <div class="mb-3 row">
          <label htmlfor="staticEmail" className="col-sm-2 col-form-label">
            Email
          </label>
          <div className="col-sm-10">
            <input
              type="text"
              readonly
              className="form-control-plaintext"
              id="staticEmail"
              value="email@example.com"
            ></input>
          </div>
        </div>
        <div className="mb-3 row">
          <label htmlfor="inputPassword" className="col-sm-2 col-form-label">
            Password
          </label>
          <div className="col-sm-10">
            <input
              type="password"
              className="form-control"
              id="inputPassword"
            ></input>
          </div>
        </div>


        <div className="row">
          <div className="col-8 p-2 d-flex justify-content-start bg-secondary text-white">
            Utente
          </div>
          <div className="col-4 p-2 d-flex justify-content-end bg-secondary text-white">
            Azioni
          </div>
        </div>
        <div>
          {users.map((u) => {
            return (
              <div className="row my-1 border">
                <div className="col-8 p-2 d-flex justify-content-start">
                  {u.name}
                </div>
                <div className="col-4 p-2 d-flex justify-content-end gap-2">
                  <button className="btn btn-primary">Update</button>
                  <button
                    className="btn btn-danger"
                    onClick={() => {
                      deleteUser(u.id);
                    }}
                  >
                    Delete
                  </button>
                </div>
              </div>
            );
          })}
        </div>
      </div>
    </>
  );
};


export default UserCrud;

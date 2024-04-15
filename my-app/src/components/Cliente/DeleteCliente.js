import "./DeleteCliente.css";
import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

function DeleteCliente({ clientes, setClientes }) {
  const [clienteIdInput, setClienteIdInput] = useState("");
  const [clienteSeleccionado, setClienteSeleccionado] = useState(null);
  const [clienteEliminado, setClienteEliminado] = useState(false);
  const navigate = useNavigate();

  const handleInputChange = (event) => {
    setClienteIdInput(event.target.value);
  };

  const handleBuscarCliente = () => {
    const cliente = clientes.find(
      (cliente) => cliente.id === parseInt(clienteIdInput)
    );
    if (cliente) {
      setClienteSeleccionado(cliente);
    } else {
      setClienteSeleccionado(null);
      alert("Cliente no encontrado");
    }
  };

  const eliminarCliente = () => {
    const nuevosClientes = clientes.filter(
      (cliente) => cliente.id !== clienteSeleccionado.id
    );
    setClientes(nuevosClientes);
    setClienteEliminado(true);
  };

  const handleOkClick = () => {
    navigate("/cliente");
  };

  return (
    <div className="DeleteCliente">
      <h1>Eliminar Cliente</h1>
      {!clienteSeleccionado && (
        <div className="Cajita-container">
          <div className="Cajita">
            <br></br>
            <label htmlFor="clienteIdInput">Ingrese el ID del cliente:</label>
            <br></br>
            <input
                type="number"
                id="clienteIdInput"
                value={clienteIdInput}
                onChange={handleInputChange}
                inputMode="numeric"
            />
            <ul className="botC">
              <button onClick={handleBuscarCliente}>Buscar</button>
            </ul>
            <div className="section">
                <ul className="botC">
                  <Link
                      to={{
                        pathname: "/cliente",
                        state: {clientes, setClientes},
                      }}
                  >
                    <button>Regresar</button>
                  </Link>
                </ul>
              </div>
          </div>
        </div>
        )}
      {clienteSeleccionado && !clienteEliminado && (
        <div className="Cajita-container">
          <div className="Cajita">
            <p>¿Eliminar al cliente?</p>
            <p>
              Nombre: {clienteSeleccionado.nombre} {clienteSeleccionado.apellidoPaterno} {clienteSeleccionado.apellidoMaterno}
            </p>
            <p>Correo: {clienteSeleccionado.email}</p>
            <div className="section">
              <ul className="botC">
                <button onClick={eliminarCliente}>Eliminar</button>
              </ul>
              <ul className="botC">
                <Link
                  to={{
                    pathname: "/cliente",
                    state: { clientes, setClientes },
                  }}
                >
                  <button>Regresar</button>
                </Link>
              </ul>
            </div>
          </div>
        </div>
      )}
      {clienteEliminado && (
        <div className="Cajita-container">
          <div className="Cajita">
            <p>Cliente eliminado</p>
            <div className="section">
              <ul className="botC">
                <button onClick={handleOkClick}>Ok</button>
              </ul>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default DeleteCliente;
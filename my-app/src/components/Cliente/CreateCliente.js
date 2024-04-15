import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./CreateCliente.css";

function CreateCliente({ clientes, setClientes }) {
  const [cliente, setCliente] = useState({
    nombre: "",
    apellidoPaterno: "",
    apellidoMaterno: "",
    contrasena: "",
    email: "",
    superUsuario: false,
  });

  const [clienteAgregado, setClienteAgregado] = useState(false);
  const navigate = useNavigate();

  const handleInputChange = (event) => {
    const { name, value, type, checked } = event.target;
    setCliente((prevCliente) => ({
      ...prevCliente,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const agregarCliente = () => {
    const total = clientes.length;
    const ultimoCliente = clientes[total - 1];
    const ultimoId = ultimoCliente.id;
    const idCliente = ultimoId + 1;
    const nuevoCliente = { id: idCliente, ...cliente };
    setClientes((prevClientes) => [...prevClientes, nuevoCliente]);
    setClienteAgregado(true);
  };

  const handleOkClick = () => {
    navigate("/cliente");
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    agregarCliente();
  };

  return (
    <div className="CreateCliente">
      <h1>Agregar Cliente</h1>
      <div className="mensaje">
        {clienteAgregado && (
          <div className="contenedor">
            <p>Cliente agregado</p>
            <p>
              Cliente: {cliente.nombre} {cliente.apellidoPaterno} {cliente.apellidoMaterno}
            </p>
            <div className="section">
              <ul className="botC">
                <button onClick={handleOkClick}>OK</button>
              </ul>
            </div>
          </div>
        )}
      </div>
      {!clienteAgregado && (
        <div className="Pedir-container">
          <div className="Pedir">
            <br></br>
            <form onSubmit={handleSubmit}>
              <label htmlFor="nombre">
                Nombre<span className="required">*</span>:
              </label>
              <input
                type="text"
                id="nombre"
                name="nombre"
                value={cliente.nombre}
                onChange={handleInputChange}
                required
              />
              <br></br>
              <label htmlFor="apellidoPaterno">
                Apellido Paterno<span className="required">*</span>:
              </label>
              <input
                type="text"
                id="apellidoPaterno"
                name="apellidoPaterno"
                value={cliente.apellidoPaterno}
                onChange={handleInputChange}
                required
              />
              <br></br>
              <label htmlFor="apellidoMaterno">Apellido Materno:</label>
              <input
                type="text"
                id="apellidoMaterno"
                name="apellidoMaterno"
                value={cliente.apellidoMaterno}
                onChange={handleInputChange}
              />
              <br></br>
              <label htmlFor="contrasena">
                Contraseña<span className="required">*</span>:
              </label>
              <input
                type="password"
                id="contrasena"
                name="contrasena"
                value={cliente.contrasena}
                onChange={handleInputChange}
                required
              />
              <br></br>
              <label htmlFor="email">
                Email<span className="required">*</span>:
              </label>
              <input
                type="email"
                id="email"
                name="email"
                value={cliente.email}
                onChange={handleInputChange}
                required
              />
              <br></br>
              <label htmlFor="superUsuario">Super Usuario:</label>
              <input
                type="checkbox"
                id="superUsuario"
                name="superUsuario"
                checked={cliente.superUsuario}
                onChange={handleInputChange}
              />
              <br></br>
              <span className="required">*</span> Campos obligatorios
              <br></br>
              <div className="section">
                <ul className="botC">
                  <button>Agregar</button>
                </ul>
              </div>
            </form>
            <div className="section">
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
    </div>
  );
}

export default CreateCliente;

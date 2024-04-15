import "./UpdateCliente.css";

import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

function UpdateCliente({ clientes, setClientes }) {
  const [datosCliente, setDatosCliente] = useState({
    nombre: "",
    apellidoPaterno: "",
    apellidoMaterno: "",
    contrasena: "",
    email: "",
    superUsuario: false,
  });

  const [clienteSeleccionado, setClienteSeleccionado] = useState(null);
  const [clienteModificado, setClienteModificado] = useState(false);
  const [idInput, setIdInput] = useState("");

  const navigate = useNavigate();

  const handleIdChange = (event) => {
    setIdInput(event.target.value);
  };

  const handleBuscarCliente = () => {
    const clienteId = parseInt(idInput);
    const cliente = clientes.find((cliente) => cliente.id === clienteId);
    if (cliente) {
      setClienteSeleccionado(cliente);
      setDatosCliente({ ...cliente });
    } else {
      setClienteSeleccionado(null);
      setDatosCliente({
        nombre: "",
        apellidoPaterno: "",
        apellidoMaterno: "",
        contrasena: "",
        email: "",
        superUsuario: false,
      });
    }
  };

  const handleChange = (event) => {
    const { name, value, type, checked } = event.target;
    setDatosCliente((prevDatosCliente) => ({
      ...prevDatosCliente,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const modificarCliente = () => {
    const index = clientes.findIndex((c) => c.id === clienteSeleccionado.id);
    const clienteModificado = { ...clienteSeleccionado, ...datosCliente };
    const nuevosClientes = [...clientes];
    nuevosClientes[index] = clienteModificado;
    setClientes(nuevosClientes);
    setClienteModificado(true);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    modificarCliente();
  };

  const handleOkClick = () => {
    navigate("/cliente");
  };

  return (
    <div className="UpdateCliente">
      <h1>Modificar Cliente</h1>
      {!clienteSeleccionado && (
        <div className="Caja-container">
          <div className="Caja">
            <br/>
            <label htmlFor="idInput">ID del Cliente:</label>
            <input
                type="text"
                id="idInput"
                name="idInput"
                value={idInput}
                onChange={handleIdChange}
            />
            <ul className="botC">
              <button onClick={handleBuscarCliente}>Buscar</button>
            </ul>
            <br/>
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
      {clienteSeleccionado && !clienteModificado && (
        <div>
          <form onSubmit={handleSubmit}>
            <div className="Cajita-container">
              <div className="Cajita">
                <br />
                <label htmlFor="nombre">
                  Nombre<span className="required">*</span>:
                </label>
                <input
                  type="text"
                  id="nombre"
                  name="nombre"
                  value={datosCliente.nombre}
                  onChange={handleChange}
                  required
                />
                <br />
                <label htmlFor="apellidoPaterno">
                  Apellido Paterno<span className="required">*</span>:
                </label>
                <input
                  type="text"
                  id="apellidoPaterno"
                  name="apellidoPaterno"
                  value={datosCliente.apellidoPaterno}
                  onChange={handleChange}
                  required
                />
                <br />
                <label htmlFor="apellidoMaterno">Apellido Materno:</label>
                <input
                  type="text"
                  id="apellidoMaterno"
                  name="apellidoMaterno"
                  value={datosCliente.apellidoMaterno}
                  onChange={handleChange}
                />
                <br />
                <label htmlFor="contrasena">
                  Contraseña<span className="required">*</span>:
                </label>
                <input
                  type="password"
                  id="contrasena"
                  name="contrasena"
                  value={datosCliente.contrasena}
                  onChange={handleChange}
                  required
                />
                <br />
                <label htmlFor="email">
                  Email<span className="required">*</span>:
                </label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={datosCliente.email}
                  onChange={handleChange}
                  required
                />
                <br />
                <label htmlFor="superUsuario">Super Usuario:</label>
                <input
                  type="checkbox"
                  id="superUsuario"
                  name="superUsuario"
                  checked={datosCliente.superUsuario}
                  onChange={handleChange}
                />
                <br />
                <span className="required">*</span> Campos obligatorios
                <br />
                <div className="section">
                  <ul className="botC">
                    <button type="submit">Guardar Cambios</button>
                  </ul>
                </div>
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
          </form>
        </div>
      )}
      {clienteModificado && (
        <div className="Caja-container">
          <div className="Caja">
            <p>Edicion de cliente de forma exitosa</p>
            <div className="section">
              <ul className="botC">
                <button onClick={handleOkClick}>OK</button>
              </ul>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default UpdateCliente;

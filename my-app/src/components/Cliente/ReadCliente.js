// ReadCliente.js

import React from "react";
import { Link } from "react-router-dom";
import "./ReadCliente.css";


function ReadCliente({ clientes }) {
  return (
    <div className="Indice">
      <h1>Lista de Clientes</h1>
      <div className="tablecontainer">
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Nombre</th>
              <th>Apellido Paterno</th>
              <th>Apellido Materno</th>
              <th>Contraseña</th>
              <th>Email</th>
              <th>Super Usuario</th>
            </tr>
          </thead>
          <tbody>
            {clientes.map((cliente) => (
              <tr key={cliente.id}>
                <td>{cliente.id}</td>
                <td>{cliente.nombre}</td>
                <td>{cliente.apellidoPaterno}</td>
                <td>{cliente.apellidoMaterno}</td>
                <td>{cliente.contrasena}</td>
                <td>{cliente.email}</td>
                <td>{cliente.superUsuario}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
      <div className="section">
        <ul className="botC">
          <Link to={{ pathname: "/cliente/agregar", state: { clientes } }}>
            <button className="custom-button">
              Agregar Cliente
            </button>
          </Link>
        </ul>
        <ul className="botC">
          <Link to={{pathname: "/cliente/modificar", state: { clientes } }}>
            <button className="custom-button">
              Editar Cliente
            </button>
          </Link>
        </ul>
        <ul className="botC">
          <Link to={{ pathname: "/cliente/eliminar", state: { clientes } }}>
            <button className="custom-button">
              Eliminar Cliente
            </button>
          </Link>
        </ul>
        <ul className="botC">
          <Link to="/">
            <button className="custom-button">
              Regresar
            </button>
          </Link>
        </ul>
      </div>
    </div>
  );
}

export default ReadCliente;

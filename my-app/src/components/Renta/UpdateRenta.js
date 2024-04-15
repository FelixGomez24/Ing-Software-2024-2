import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./UpdateRenta.css";

function UpdateRenta({ clientes, peliculas, rentas, setRentas }) {
  const [datosRenta, setDatosRenta] = useState({
    idCliente: "",
    idPelicula: "",
    fecha_renta: "",
    dias_de_renta: 5,
    estatus: false,
  });

  const [rentaSeleccionada, setRentaSeleccionada] = useState(null);
  const [rentaModificada, setRentaModificada] = useState(false);
  const [idInput, setIdInput] = useState(""); // State to store the input rent ID

  const navigate = useNavigate();

  const handleIdChange = (event) => {
    setIdInput(event.target.value); // Update the ID state as the user types
  };

  const handleBuscarRenta = () => {
    const rentaId = parseInt(idInput); // Convert the input rent ID to an integer
    const renta = rentas.find((renta) => renta.idRentar === rentaId);
    if (renta) {
      setRentaSeleccionada(renta);
      setDatosRenta({ ...renta });
    } else {
      setRentaSeleccionada(null);
      alert("Renta no encontrada");
    }
  };

  const handleChange = (event) => {
    const { name, value, type, checked } = event.target;
    setDatosRenta((prevDatosRenta) => ({
      ...prevDatosRenta,
      [name]: type === "checkbox" ? checked : value,
    }));
  };

  const modificarRenta = () => {
    const idRentar = rentaSeleccionada.idRentar;
    const rentaModi = { idRentar, ...datosRenta };
    const nuevasRentas = rentas.map((renta) =>
      renta.idRentar === idRentar ? rentaModi : renta
    );
    setRentas(nuevasRentas);
    setRentaModificada(true);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    modificarRenta();
  };

  const handleOkClick = () => {
    navigate("/renta");
  };

  const formatFecha = (fecha) => {
    const fechaDate = new Date(fecha);
    fechaDate.setDate(fechaDate.getDate() + 1);
    return fechaDate.toLocaleDateString();
  };

  return (
    <div className="UpdateRenta">
      <h1>Actualizar Renta</h1>
      {!rentaSeleccionada && (
        <div className="Caja-container">
          <div className="Caja">
            <br/>
            <label htmlFor="idInput">ID de la Renta:</label>
            <input
                type="text"
                id="idInput"
                name="idInput"
                value={idInput}
                onChange={handleIdChange}
            />
            <ul className="botC">
              <button onClick={handleBuscarRenta}>Buscar</button>
            </ul>
            <br/>
              <div className="section">
                <ul className="botC">
                  <Link
                      to={{
                        pathname: "/renta",
                        state: {clientes, peliculas, rentas, setRentas},
                      }}
                  >
                    <button>Regresar</button>
                  </Link>
                </ul>
              </div>
          </div>
        </div>
        )}
      {rentaModificada && (
        <div className="Caja-container">
          <div className="Caja">
            <p>Renta modificada</p>
            <div className="section">
              <ul className="botC">
                <button onClick={handleOkClick}>Ok</button>
              </ul>
            </div>
          </div>
        </div>
      )}
      {rentaSeleccionada && !rentaModificada && (
        <div>
          <form onSubmit={handleSubmit}>
            <div className="Caja-container">
              <div className="Caja">
                <br />
                <label htmlFor="idCliente">ID del Cliente:</label>
                <input
                  type="text"
                  id="idCliente"
                  name="idCliente"
                  value={datosRenta.idCliente}
                  readOnly
                />
                <br />
                <label htmlFor="idPelicula">ID de la Película:</label>
                <input
                  type="text"
                  id="idPelicula"
                  name="idPelicula"
                  value={datosRenta.idPelicula}
                  readOnly
                />
                <br />
                <label htmlFor="fecha_renta">Fecha de Renta:</label>
                <input
                  type="text"
                  id="fecha_renta"
                  name="fecha_renta"
                  value={formatFecha(datosRenta.fecha_renta)}
                  readOnly
                />
                <br />
                <label htmlFor="dias_de_renta">Días de Renta:</label>
                <input
                  type="number"
                  id="dias_de_renta"
                  name="dias_de_renta"
                  value={datosRenta.dias_de_renta}
                  readOnly
                />
                <br />
                <label htmlFor="estatus">Estado:</label>
                <input
                  type="checkbox"
                  id="estatus"
                  name="estatus"
                  checked={datosRenta.estatus}
                  onChange={handleChange}
                />
                <br />
                <div className="section">
                  <ul className="botC">
                    <button type="button" onClick={handleSubmit}>
                      Guardar Cambios
                    </button>
                  </ul>
                </div>
                <div className="section">
                  <ul className="botC">
                    <Link
                      to={{
                        pathname: "/renta",
                        state: { clientes, peliculas, rentas, setRentas },
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
    </div>
  );
}

export default UpdateRenta;

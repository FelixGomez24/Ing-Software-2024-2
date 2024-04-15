import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./CreateRenta.css";

function CreateRenta({ rentas, setRentas }) {
  const [renta, setRenta] = useState({
    id: "", // <-- Make sure this is a unique identifier
    idCliente: "",
    idPelicula: "",
    fecha_renta: "",
    dias_de_renta: 1,
    estatus: "",
  });
  const [rentaAgregada, setRentaAgregada] = useState(false);
  const navigate = useNavigate();

  const handleChange = (event) =>
    setRenta({
      ...renta,
      [event.target.name]:
        event.target.type === "checkbox"
          ? event.target.checked
          : event.target.value,
    });

  const agregarRenta = () => {
    renta.dias_de_renta < 1 && (renta.dias_de_renta = 1);
    const idRentar = rentas.length + 1;
    const nuevaRenta = { ...renta, id: idRentar.toString() }; // Ensure ID is converted to string
    setRentas([...rentas, nuevaRenta]);
    setRentaAgregada(true);
  };

  const handleOkClick = () => {
    navigate("/renta");
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    agregarRenta();
  };

  return (
    <div className="CreateRenta">
      <h1>Agregar Renta</h1>
      <div className="mensaje">
        {rentaAgregada && (
          <div className="Pedir">
            <p>Renta agregada</p>
            <div className="section">
              <ul className="botC">
                <button onClick={handleOkClick}>Regresar</button>
              </ul>
            </div>
          </div>
        )}
      </div>
      {!rentaAgregada && (
        <div className="Pedir-container">
          <div className="Pedir">
            <br />
            <form onSubmit={handleSubmit}>
              <label htmlFor="idCliente">Selecciona el Cliente:</label>
              <input
                type="text"
                name="idCliente"
                value={renta.idCliente}
                onChange={handleChange}
                required
              />
              <br />
              <label htmlFor="idPelicula">Selecciona la Película:</label>
              <input
                type="text"
                name="idPelicula"
                value={renta.idPelicula}
                onChange={handleChange}
                required
              />
              <br />
              <label htmlFor="fecha_renta">Fecha de Renta:</label>
              <input
                type="date"
                name="fecha_renta"
                value={renta.fecha_renta}
                onChange={handleChange}
                required
              />
              <br />
              <label htmlFor="dias_de_renta">Días de Renta:</label>
              <input
                type="number"
                name="dias_de_renta"
                value={renta.dias_de_renta}
                min={1}
                step={1}
                onChange={handleChange}
              />
              <br />
              <label htmlFor="estatus">Estado:</label>
              <select
                name="estatus"
                value={renta.estatus}
                onChange={handleChange}
                required
              >
                <option value="">Seleccionar estado</option>
                <option value="Entregada">Entregada</option>
                <option value="Sin Entregar">Sin Entregar</option>
              </select>
              <br />
              <div className="section">
                <ul className="botC">
                    <button type="submit">Agregar</button>
                </ul>
              </div>
            </form>
            <div className="section">
              <ul className="botCCR">
                <Link
                    to={{
                      pathname: "/renta",
                      state: {rentas, setRentas},
                    }}
                >
                  <ul className="botC">
                    <button>Regresar</button>
                  </ul>
                </Link>
              </ul>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default CreateRenta;

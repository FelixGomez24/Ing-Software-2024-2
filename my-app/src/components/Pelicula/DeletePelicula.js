import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./DeletePelicula.css";

function DeletePelicula({ peliculas, setPeliculas }) {
  const [peliculaSeleccionada, setPeliculaSeleccionada] = useState(null);
  const [peliculaEliminada, setPeliculaEliminada] = useState(false);
  const [idInput, setIdInput] = useState(""); // State to store the input movie ID

  const navigate = useNavigate();

  const handleIdChange = (event) => {
    setIdInput(event.target.value); // Update the ID state as the user types
  };

  const handleBuscarPelicula = () => {
    const peliculaId = parseInt(idInput); // Convert the input movie ID to an integer
    const pelicula = peliculas.find(
      (pelicula) => pelicula.idPelicula === peliculaId
    );
    if (pelicula) {
      setPeliculaSeleccionada(pelicula);
    } else {
      setPeliculaSeleccionada(null);
      alert("Película no encontrada");
    }
  };

  const eliminarPelicula = () => {
    const idPelicula = peliculaSeleccionada.idPelicula;
    const nuevasPeliculas = peliculas.filter(
      (pelicula) => pelicula.idPelicula !== idPelicula
    );
    setPeliculas(nuevasPeliculas);
    setPeliculaEliminada(true);
  };

  const handleEliminarClick = () => {
    if (window.confirm("¿Estás seguro de que quieres eliminar esta película?")) {
      eliminarPelicula();
    }
  };

  const handleOkClick = () => {
    navigate("/pelicula");
  };

  return (
    <div className="DeletePelicula">
      <h1>Eliminar Película</h1>
      {!peliculaSeleccionada && (
        <div className="Caja-container">
          <div className="Caja">
            <br/>
            <label htmlFor="idInput">ID de la Película:</label>
            <input
                type="text"
                id="idInput"
                name="idInput"
                value={idInput}
                onChange={handleIdChange}
            />
            <ul className="botC">
              <button onClick={handleBuscarPelicula}>Buscar</button>
            </ul>
            <br/>
              <div className="section">
                <ul className="botC">
                  <Link
                      to={{
                        pathname: "/pelicula",
                        state: {peliculas, setPeliculas},
                      }}
                  >
                    <button>Regresar</button>
                  </Link>
                </ul>
              </div>
          </div>
        </div>
        )}
      {peliculaSeleccionada && !peliculaEliminada && (
        <div className="Caja-container">
          <div className="Caja">
            <p>¿Estás seguro de que quieres eliminar esta película?</p>
            <p>ID: {peliculaSeleccionada.idPelicula}</p>
            <p>Nombre: {peliculaSeleccionada.nombre}</p>
            <p>Género: {peliculaSeleccionada.genero}</p>
            <p>Duración: {peliculaSeleccionada.duracion}</p>
            <p>Inventario: {peliculaSeleccionada.inventario}</p>
            <div className="section">
              <ul className="botC">
                <button onClick={handleEliminarClick}>Eliminar</button>
              </ul>
            </div>
          </div>
        </div>
      )}
      {peliculaEliminada && (
        <div className="Caja-container">
          <div className="Caja">
            <p>Película eliminada</p>
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

export default DeletePelicula;

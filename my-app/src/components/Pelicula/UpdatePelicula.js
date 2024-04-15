import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import "./UpdatePelicula.css";

function UpdatePelicula({ peliculas, setPeliculas }) {
  const [datosPelicula, setDatosPelicula] = useState({
    nombre: "",
    genero: "",
    duracion: "",
    inventario: 1,
  });

  const [peliculaSeleccionada, setPeliculaSeleccionada] = useState(null);
  const [peliculaModificada, setPeliculaModificada] = useState(false);
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
      setDatosPelicula({ ...pelicula });
    } else {
      setPeliculaSeleccionada(null);
      alert("Película no encontrada");
    }
  };

  const handleChange = (event) => {
    const { name, value } = event.target;
    setDatosPelicula((prevDatosPelicula) => ({
      ...prevDatosPelicula,
      [name]: value,
    }));
  };

  const modificarPelicula = () => {
    const idPelicula = peliculaSeleccionada.idPelicula;
    const peliculaModi = { idPelicula, ...datosPelicula };
    const nuevasPeliculas = peliculas.map((pelicula) =>
      pelicula.idPelicula === idPelicula ? peliculaModi : pelicula
    );
    setPeliculas(nuevasPeliculas);
    setPeliculaModificada(true);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    modificarPelicula();
  };

  const handleOkClick = () => {
    navigate("/pelicula");
  };

  return (
    <div className="UpdatePelicula">
      <h1>Modificar Película</h1>
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
      {peliculaModificada && (
        <div className="Caja-container">
          <div className="Caja">
            <p>Película modificada</p>
            <div className="section">
              <ul className="botC">
                <button onClick={handleOkClick}>Ok</button>
              </ul>
            </div>
          </div>
        </div>
      )}
      {peliculaSeleccionada && !peliculaModificada && (
        <div>
          <form onSubmit={handleSubmit}>
            <div className="Caja-container">
              <div className="Caja">
                <br />
                <label htmlFor="nombre">Nombre:</label>
                <input
                  type="text"
                  id="nombre"
                  name="nombre"
                  value={datosPelicula.nombre}
                  onChange={handleChange}
                />
                <br />
                <label htmlFor="genero">Género:</label>
                <input
                  type="text"
                  id="genero"
                  name="genero"
                  value={datosPelicula.genero}
                  onChange={handleChange}
                />
                <br />
                <label htmlFor="duracion">Duración:</label>
                <input
                  type="number"
                  id="duracion"
                  name="duracion"
                  value={datosPelicula.duracion}
                  min={1}
                  step={1}
                  onChange={handleChange}
                />
                <br />
                <label htmlFor="inventario">Inventario:</label>
                <input
                  type="number"
                  id="inventario"
                  name="inventario"
                  value={datosPelicula.inventario}
                  min={0}
                  step={1}
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
                        pathname: "/pelicula",
                        state: { peliculas, setPeliculas },
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

export default UpdatePelicula;

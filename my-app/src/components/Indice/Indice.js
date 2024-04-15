import React from "react";
import { Link } from "react-router-dom";
import "./Indice.css";

function Indice() {
  return (
    <div className="Indice">
      <h1>INICIO</h1>
      <div className="section">
        <Link to="/cliente" className="section-item">
          <button className="custom-button">
            <div className="button-content">
              <img src="/usuario.jpg" alt="Cliente Icon" className="button-image" />
              <span>USUARIOS</span>
            </div>
          </button>
        </Link>
        <Link to="/pelicula" className="section-item">
          <button className="custom-button">
            <div className="button-content">
              <img src="/movies1.jpg" alt="Pelicula Icon" className="button-image" />
              <span>PELICULAS</span>
            </div>
          </button>
        </Link>
        <Link to="/renta" className="section-item">
          <button className="custom-button">
            <div className="button-content">
              <img src="/renta.jpg" alt="Renta Icon" className="button-image" />
              <span>RENTA</span>
            </div>
          </button>
        </Link>
      </div>
    </div>
  );
}

export default Indice;

/*import "./App.css";*/

import React, {useState} from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Indice from "./components/Indice/Indice";
import ReadCliente from "./components/Cliente/ReadCliente";
import CreateCliente from "./components/Cliente/CreateCliente";
import UpdateCliente from "./components/Cliente/UpdateCliente";
import DeleteCliente from "./components/Cliente/DeleteCliente";
import ReadPelicula from "./components/Pelicula/ReadPelicula";
import CreatePelicula from "./components/Pelicula/CreatePelicula";
import UpdatePelicula from "./components/Pelicula/UpdatePelicula";
import DeletePelicula from "./components/Pelicula/DeletePelicula";
import ReadRenta from "./components/Renta/ReadRenta";
import CreateRenta from "./components/Renta/CreateRenta";
import UpdateRenta from "./components/Renta/UpdateRenta";

function App() {
  const [clientes, setClientes] = useState([
    {
      id: 1,
      nombre: "María",
      apellidoPaterno: "García",
      apellidoMaterno: "Hernández",
      contrasena: "contrasena123",
      email: "maria@example.com",
      superUsuario: false,
    },
    {
      id: 2,
      nombre: "Juan",
      apellidoPaterno: "López",
      contrasena: "clave456",
      email: "juan@gmail.com",
      superUsuario: true,
    },
    {
      id: 3,
      nombre: "Lucía",
      apellidoPaterno: "Sánchez",
      contrasena: "luciapass",
      email: "lucia@example.com",
      superUsuario: false,
    },
    {
      id: 4,
      nombre: "Diego",
      apellidoPaterno: "Pérez",
      apellidoMaterno: "Gómez",
      contrasena: "diego1234",
      email: "diego@gmail.com",
      superUsuario: false,
    },
    {
      id: 5,
      nombre: "Elena",
      apellidoPaterno: "Martínez",
      contrasena: "elenapass",
      email: "elena@example.com",
      superUsuario: false,
    },
    {
      id: 6,
      nombre: "Alejandro",
      apellidoPaterno: "González",
      apellidoMaterno: "Rodríguez",
      contrasena: "ale123",
      email: "alejandro@gmail.com",
      superUsuario: false,
    },
    {
      id: 7,
      nombre: "Carolina",
      apellidoPaterno: "Hernández",
      contrasena: "caro456",
      email: "carolina@example.com",
      superUsuario: true,
    },
    {
      id: 8,
      nombre: "Pablo",
      apellidoPaterno: "Díaz",
      apellidoMaterno: "Fernández",
      contrasena: "pablito",
      email: "pablo@gmail.com",
      superUsuario: false,
    },
    {
      id: 9,
      nombre: "Julia",
      apellidoPaterno: "Ruíz",
      contrasena: "juliapass",
      email: "julia@example.com",
      superUsuario: false,
    },
    {
      id: 10,
      nombre: "Mateo",
      apellidoPaterno: "Gómez",
      apellidoMaterno: "Jiménez",
      contrasena: "mateo123",
      email: "mateo@gmail.com",
      superUsuario: false,
    },
  ]);

  const [peliculas, setPeliculas] = useState([
    {
      idPelicula: 1,
      nombre: "La forma del agua",
      genero: "Drama",
      duracion: 123,
      inventario: 6,
    },
    {
      idPelicula: 2,
      nombre: "Inception",
      genero: "Ciencia Ficción",
      duracion: 148,
      inventario: 3,
    },
    {
      idPelicula: 3,
      nombre: "Forrest Gump",
      genero: "Drama",
      duracion: 142,
      inventario: 8,
    },
    {
      idPelicula: 4,
      nombre: "Interestelar",
      genero: "Ciencia Ficción",
      duracion: 169,
      inventario: 4,
    },
    {
      idPelicula: 5,
      nombre: "Matrix",
      genero: "Acción",
      duracion: 136,
      inventario: 5,
    },
    {
      idPelicula: 6,
      nombre: "Jurassic Park",
      genero: "Aventura",
      duracion: 127,
      inventario: 2,
    },
    {
      idPelicula: 7,
      nombre: "El Rey León",
      genero: "Animación",
      duracion: 88,
      inventario: 7,
    },
    {
      idPelicula: 8,
      nombre: "Mujer Maravilla",
      genero: "Acción",
      duracion: 141,
      inventario: 1,
    },
    {
      idPelicula: 9,
      nombre: "El Padrino",
      genero: "Crimen",
      duracion: 175,
      inventario: 3,
    },
    {
      idPelicula: 10,
      nombre: "Pulp Fiction",
      genero: "Crimen",
      duracion: 154,
      inventario: 6,
    },
  ]);

  const [rentas, setRentas] = useState([
    {
      idRentar: 1,
      idUsuario: 2,
      idPelicula: 3,
      fecha_renta: new Date("2023-05-15"),
      dias_de_renta: 4,
      estatus: false,
    },
    {
      idRentar: 2,
      idUsuario: 4,
      idPelicula: 6,
      fecha_renta: new Date("2024-02-20"),
      dias_de_renta: 2,
      estatus: true,
    },
    {
      idRentar: 3,
      idUsuario: 8,
      idPelicula: 7,
      fecha_renta: new Date("2023-11-10"),
      dias_de_renta: 6,
      estatus: false,
    },
    {
      idRentar: 4,
      idUsuario: 6,
      idPelicula: 2,
      fecha_renta: new Date("2022-07-05"),
      dias_de_renta: 3,
      estatus: true,
    },
    {
      idRentar: 5,
      idUsuario: 9,
      idPelicula: 10,
      fecha_renta: new Date("2021-09-30"),
      dias_de_renta: 5,
      estatus: false,
    },
  ]);


  return (
    <Router>
      <Routes>
        <Route exact path="/" element={<Indice />} />
        <Route
          path="/cliente"
          element={<ReadCliente clientes={clientes} setClientes={setClientes} />}
        />
        <Route
          path="/cliente/agregar"
          element={<CreateCliente clientes={clientes} setClientes={setClientes} />}
        />
        <Route
          path="/cliente/modificar"
          element={<UpdateCliente clientes={clientes} setClientes={setClientes} />}
        />
        <Route
          path="/cliente/eliminar"
          element={<DeleteCliente clientes={clientes} setClientes={setClientes} />}
        />
        <Route
          path="/renta"
          element={<ReadRenta rentas={rentas} setRentas={setRentas} />}
        />
        <Route
          path="/renta/agregar"
          element={<CreateRenta rentas={rentas} setRentas={setRentas} />}
        />
        <Route
          path="/renta/modificar"
          element={<UpdateRenta rentas={rentas} setRentas={setRentas} />}
        />
        <Route
          path="/pelicula"
          element={<ReadPelicula peliculas={peliculas} setPeliculas={setPeliculas} />}
        />
        <Route
          path="/pelicula/agregar"
          element={<CreatePelicula peliculas={peliculas} setPeliculas={setPeliculas} />}
        />
        <Route
          path="/pelicula/modificar"
          element={<UpdatePelicula peliculas={peliculas} setPeliculas={setPeliculas} />}
        />
        <Route
          path="/pelicula/eliminar"
          element={<DeletePelicula peliculas={peliculas} setPeliculas={setPeliculas} />}
        />
      </Routes>
    </Router>
  );
}

export default App;
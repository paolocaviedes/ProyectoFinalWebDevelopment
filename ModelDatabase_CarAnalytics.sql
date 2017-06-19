CREATE TABLE Transmision (  
  idTransmision INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,  
  tipoTransmision VARCHAR NOT NULL,  
  sigla VARCHAR NOT NULL,  
  PRIMARY KEY(idTransmision)  
);  

CREATE TABLE Categoria (  
  idCategoria INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,  
  nombreCategoria VARCHAR NOT NULL,  
  sigla VARCHAR NOT NULL,  
  PRIMARY KEY(idCategoria)  
);  

CREATE TABLE Carroceria (  
  idCarroceria INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,  
  nombreCarroceria VARCHAR NOT NULL,  
  sigla VARCHAR NOT NULL,  
  PRIMARY KEY(idCarroceria)  
);  

CREATE TABLE Pais (
  idPais INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  nombre VARCHAR NULL,
  sigla VARCHAR NULL,
  PRIMARY KEY(idPais)
);

CREATE TABLE Region (
  idRegion INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Pais_idPais INTEGER UNSIGNED NOT NULL,
  nombre INTEGER UNSIGNED NULL,
  numero INTEGER UNSIGNED NULL,
  sigla INTEGER UNSIGNED NULL,
  PRIMARY KEY(idRegion),
  INDEX Region_FKIndex1(Pais_idPais)
);

CREATE TABLE Ciudad (
  idCiudad INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Region_idRegion INTEGER UNSIGNED NOT NULL,
  nombre INTEGER UNSIGNED NULL,
  sigla INTEGER UNSIGNED NULL,
  PRIMARY KEY(idCiudad),
  INDEX Ciudad_FKIndex2(Region_idRegion)
);

CREATE TABLE Marca (
  idMarca INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Pais_idPais INTEGER UNSIGNED NOT NULL,
  nombre VARCHAR NULL,
  sigla VARCHAR NULL,
  PRIMARY KEY(idMarca),
  INDEX Marca_FKIndex1(Pais_idPais)
);

CREATE TABLE Modelo (
  idModelo INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Marca_idMarca INTEGER UNSIGNED NOT NULL,
  nombre VARCHAR NULL,
  sigla VARCHAR NULL,
  PRIMARY KEY(idModelo),
  INDEX Modelo_FKIndex1(Marca_idMarca)
);

CREATE TABLE Version (
  idVersion INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Modelo_idModelo INTEGER UNSIGNED NOT NULL,
  nombreversion VARCHAR NULL,
  sigla VARCHAR NULL,
  descripcion VARCHAR NULL,
  PRIMARY KEY(idVersion),
  INDEX Version_FKIndex1(Modelo_idModelo)
);

CREATE TABLE Tipo (  
  idTipo INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,  
  nombreTipo VARCHAR NOT NULL,  
  sigla VARCHAR NOT NULL,  
  esparticular BOOL NOT NULL,  
  esautomotora BOOL NOT NULL,  
  PRIMARY KEY(idTipo)  
);

CREATE TABLE Particular (
  idParticular INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Ciudad_idCiudad INTEGER UNSIGNED NOT NULL,
  Tipo_idTipo INTEGER UNSIGNED NOT NULL,
  nombreDuenno VARCHAR NULL,
  direccion VARCHAR NULL,
  telefono INTEGER UNSIGNED NULL,
  email VARCHAR NULL,
  personalIdentifier INTEGER UNSIGNED NULL,
  PRIMARY KEY(idParticular),
  INDEX Particular_FKIndex1(Tipo_idTipo),
  INDEX Particular_FKIndex2(Ciudad_idCiudad)
);

CREATE TABLE Automotora (
  idAutomotora INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Ciudad_idCiudad INTEGER UNSIGNED NOT NULL,
  Tipo_idTipo INTEGER UNSIGNED NOT NULL,
  nombre VARCHAR NULL,
  direccion VARCHAR NULL,
  comuna VARCHAR NULL,
  telefono INTEGER UNSIGNED NULL,
  email VARCHAR NULL,
  PRIMARY KEY(idAutomotora),
  INDEX Automotora_FKIndex1(Tipo_idTipo),
  INDEX Automotora_FKIndex2(Ciudad_idCiudad)
);

CREATE TABLE contacto (
  idcontacto INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Ciudad_idCiudad INTEGER UNSIGNED NOT NULL,
  Automotora_idAutomotora INTEGER UNSIGNED NOT NULL,
  nombre VARCHAR NULL,
  direccion VARCHAR NULL,
  comuna VARCHAR NULL,
  PRIMARY KEY(idcontacto),
  INDEX contacto_FKIndex1(Automotora_idAutomotora),
  INDEX contacto_FKIndex3(Ciudad_idCiudad)
);


CREATE TABLE Vehiculo (
  idVehiculo INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  Version_idVersion INTEGER UNSIGNED NOT NULL,
  Modelo_idModelo INTEGER UNSIGNED NOT NULL,
  Marca_idMarca INTEGER UNSIGNED NOT NULL,
  Tipo_idTipo INTEGER UNSIGNED NOT NULL,
  Ciudad_idCiudad INTEGER UNSIGNED NOT NULL,
  Carroceria_idCarroceria INTEGER UNSIGNED NOT NULL,
  Categoria_idCategoria INTEGER UNSIGNED NOT NULL,
  Transmision_idTransmision INTEGER UNSIGNED NOT NULL,
  kilometraje INTEGER UNSIGNED NULL,
  precio INTEGER UNSIGNED NULL,
  fechapublicacion INTEGER UNSIGNED NULL,
  anno INTEGER UNSIGNED NULL,
  esnuevo BOOL NULL,
  colorexterior VARCHAR NULL,
  puertas INTEGER UNSIGNED NULL,
  combustible VARCHAR NULL,
  aireacondicionado BOOL NULL,
  alzavidrioselectricos BOOL NULL,
  espejoselectricos BOOL NULL,
  frenosabs BOOL NULL,
  airbag BOOL NULL,
  unicoduenno BOOL NULL,
  cierrecentralizado BOOL NULL,
  catalitico BOOL NULL,
  llantas BOOL NULL,
  radio BOOL NULL,
  direccion VARCHAR NULL,
  cilindrada VARCHAR NULL,
  fechadeultimaedicion DATE NULL,
  fechadeventa DATE NULL,
  PRIMARY KEY(idVehiculo),
  INDEX Vehiculo_FKIndex1(Transmision_idTransmision),
  INDEX Vehiculo_FKIndex2(Categoria_idCategoria),
  INDEX Vehiculo_FKIndex3(Carroceria_idCarroceria),
  INDEX Vehiculo_FKIndex5(Ciudad_idCiudad),
  INDEX Vehiculo_FKIndex6(Tipo_idTipo),
  INDEX Vehiculo_FKIndex7(Marca_idMarca),
  INDEX Vehiculo_FKIndex8(Modelo_idModelo),
  INDEX Vehiculo_FKIndex9(Version_idVersion)
);


CREATE TABLE ContactoVehiculo (
  idContactoVehiculo INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,
  contacto_idcontacto INTEGER UNSIGNED NOT NULL,
  Vehiculo_idVehiculo INTEGER UNSIGNED NOT NULL,
  PRIMARY KEY(idContactoVehiculo),
  INDEX ContactoVehiculo_FKIndex1(Vehiculo_idVehiculo),
  INDEX ContactoVehiculo_FKIndex2(contacto_idcontacto)
);
# Proyecto Final Desarrollo Web

## Base de Datos
Modelo escogido: Estrella  
Tabla de hechos: Vehiculo  
Para representar los requerimientos del negocio, se realizo el diseño de la base de datos segun la siguiente descripcion:  

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

CREATE TABLE Tipo (  
  idTipo INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,  
  nombreTipo VARCHAR NOT NULL,  
  sigla VARCHAR NOT NULL,  
  esparticular BOOL NOT NULL,  
  esautomotora BOOL NOT NULL,  
  PRIMARY KEY(idTipo)  
);

CREATE TABLE Carroceria (  
  idCarroceria INTEGER UNSIGNED NOT NULL AUTO_INCREMENT,  
  nombreCarroceria VARCHAR NOT NULL,  
  sigla VARCHAR NOT NULL,  
  PRIMARY KEY(idCarroceria)  
);  




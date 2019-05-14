CREATE DATABASE IF NOT EXISTS goldAndSilver;
USE goldAndSilver;

CREATE TABLE IF NOT EXISTS gold (
  id int NOT NULL AUTO_INCREMENT,
  numberOfDate int NOT NULL,
  price DECIMAL(6,2) NOT NULL,
  realDate VARCHAR(20) NOT NULL,
  UNIQUE(numberOfDate),
  PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS silver (
  id int NOT NULL AUTO_INCREMENT,
  numberOfDate int NOT NULL,
  price DECIMAL(6,2) NOT NULL,
  realDate VARCHAR(20) NOT NULL,
  UNIQUE(numberOfDate),
  PRIMARY KEY(id)
);

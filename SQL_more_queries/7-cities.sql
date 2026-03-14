-- Creates the database hbtn_0d_usa and the table cities
-- cities description:
--   id INT unique, auto generated, can't be null and is a primary key
--   state_id INT, can't be null and must be a FOREIGN KEY 
--   name VARCHAR(256) can't be null

-- Create the database if it doesn't already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Switch to the database
USE hbtn_0d_usa;

-- Create the table cities
CREATE TABLE IF NOT EXISTS cities (
    id INT UNIQUE NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);

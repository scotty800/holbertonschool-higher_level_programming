-- Create the database "hbtn_0d_usa" if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Use the "hbtn_0d_usa" database for the subsequent commands.
USE hbtn_0d_usa;
-- Create the table "cities" if it does not already exist, with the specified columns:
-- "id" is an integer that is auto-incremented, unique, not null, and is the primary key.
-- "state_id" is an integer that cannot be null and serves as a foreign key referencing the "id" column in the "states" table.
-- "name" is a string of maximum 256 characters that cannot be null.
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256),
    FOREIGN KEY(state_id) REFERENCES states(id)
);
-- Table definitions for the tournament project.
--
-- REMAINDER:
-- $ psql
-- $ psql => \i tournament.sql
-- $ psql => \q  # exit psql

-- CREATE AND CONNECT DATABASE
-- Delete old torunament database
DROP DATABASE IF EXISTS tournament;
-- Create the torunament database
CREATE DATABASE tournament;
-- Connect to the database
\c tournament;


-- TABLES
-- Payers table
CREATE TABLE players (id SERIAL PRIMARY KEY,
                      name VARCHAR(50) NOT NULL,
                      createdAt TIMESTAMP DEFAULT current_timestamp
                      );

-- Matches table
CREATE TABLE matches (id SERIAL PRIMARY KEY, 
                      winner INTEGER REFERENCES players (id), 
                      loser INTEGER REFERENCES players (id) 
                        CHECK (winner != loser)
                      );

-- VIEWS
-- Create standings wiew with each player wins and matches
CREATE VIEW standings AS 
  SELECT 
    players.id as id, 
    players.name as name,
    (SELECT count(*) 
      FROM matches
      WHERE players.id = matches.winner) AS wins,
    (SELECT count(*) 
      FROM matches
      WHERE players.id = matches.winner OR 
            players.id = matches.loser) AS matches
    FROM players
    ORDER BY wins DESC;
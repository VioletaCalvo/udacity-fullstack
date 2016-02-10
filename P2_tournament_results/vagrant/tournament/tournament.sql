-- Table definitions for the tournament project.
--
-- REMAINDER:
-- $ psql
-- $ psql => \i tournament.sql

DROP DATABASE IF EXISTS tournament;

CREATE DATABASE tournament;

\c tournament;

CREATE TABLE players (id SERIAL PRIMARY KEY,
                      name VARCHAR(50) NOT NULL,
                      createdAt TIMESTAMP DEFAULT current_timestamp
                      );

CREATE TABLE matches (id SERIAL PRIMARY KEY,
                      FOREIGN KEY winner INTEGER REFERENCES players (id),
                      FOREIGN KEY loser INTEGER REFERENCES players (id),
                      );

-- -Create standings wiew with each player wins and matches
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
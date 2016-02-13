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
                        CHECK (winner != loser),
                      draw BOOLEAN DEFAULT false
                      );

-- VIEWS
-- Create standings wiew with each player points
-- Points score are:
--    * win: 3 points
--    * draw: 1 point
--    * lose: 0 points
CREATE VIEW standings AS 
  SELECT 
    players.id as id, 
    players.name as name,
    ((SELECT count(*)*3
           FROM matches
           WHERE players.id = matches.winner AND matches.draw != True)
      +
     (SELECT count(*)
           FROM matches
           WHERE (players.id = matches.winner OR players.id = matches.loser) AND matches.draw = True)
     ) AS points,
    (SELECT count(*)
      FROM matches
      WHERE players.id = matches.winner OR 
            players.id = matches.loser) AS matches
    FROM players
    ORDER BY points DESC;

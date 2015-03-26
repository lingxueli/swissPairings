-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.



CREATE TABLE players (
	id SERIAL PRIMARY KEY,
	name TEXT
	);

CREATE TABLE matches (
	id INTEGER REFERENCES players(id),
	result REAL

	);
-- id  win#   matches#
-- create view tournament as select players.id AS id, players.name AS name, COALESCE(sum(matches.result), 0) AS wins, COALESCE(count(matches.result), 0) AS matches from players LEFT JOIN matches on players.id = matches.id GROUP BY players.id;


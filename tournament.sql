-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.
--
--

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

--connect to database 'tournament'
\c tournament

--SERIAL allows AUTO_INCREMENT
CREATE TABLE players (
id SERIAL PRIMARY KEY,
player_name VARCHAR
);

CREATE TABLE matches (
id SERIAL PRIMARY KEY,
winner INT REFERENCES players(id) ON DELETE CASCADE,
loser INT REFERENCES players(id) ON DELETE CASCADE,
CHECK (winner <> loser) --ensures winner and loser is different from each other
);

CREATE VIEW view_wins AS
select players.id AS view_wins_id, count(matches.id) AS wins
FROM players LEFT OUTER JOIN matches
    ON players.id = matches.winner
GROUP BY players.id;

CREATE VIEW view_played AS
SELECT players.id AS view_played_id, count(matches.id) AS played
FROM players LEFT OUTER JOIN matches
    ON players.id = matches.winner OR players.id = matches.loser
GROUP BY players.id;

CREATE VIEW standings AS
SELECT players.id, players.player_name, view_wins.wins AS total_wins, view_played.played AS matches_played
FROM players, view_wins, view_played
WHERE players.id = view_wins_id AND players.id = view_played_id
ORDER BY total_wins DESC;

--CREATE VIEW next_round AS
--SELECT players.id AS player1_id, players.player_name AS player1_name,
--players.id AS player2_id, players.player_name AS player2_name
--FROM standings
--WHERE player1_id.wins = player2_id.wins;

Here is the view definition:

CREATE VIEW ranking AS
SELECT standings.id , standings.name , standings.wins , ceiling(1.0 * row_number() over(order by standings.wins ,standings.id) / 2) as rank
FROM standings
Here is the logic of the student's swissPairings() function:

    db = connect()
    c = db.cursor()
    query = """
    select c1.id as id1, c1.Name as name1, c2.id as id2, c2.name as name2
    from ranking c1
    join ranking c2 on c1.rank = c2.rank and c1.id > c2.id;
    """
    c.execute(query)
    rows = c.fetchall()
    db.close()
    return rows

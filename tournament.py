#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

DBNAME = "tournament"

#def connect():
#    """Connect to the PostgreSQL database. Returns a database connection."""
#    return psycopg2.connect("dbname=tournament")

def connect(database_name="tournament"):
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print("<error message>")

#To build on the suggestion that a previous reviewer gave you: you can use a part of the psycopg2 library that will return a specific error message that will correctly describe why the connection failed.
#
#Here is some code from another student's project that shows how to do this:
#
#    except psycopg2.OperationalError as db_exept:
#        print('Unable to connect!\n{0}').format(db_exept)
#        quit()
#This is what happens when I inadventently specify an incorrect database name:
#
#>>> import tournament as t
#>>> t.connect('zournament')
#Unable to connect!
#FATAL:  database "zournament" does not exist


def deleteMatches():
    """Remove all the match records from the database."""
    db, c = connect()
    c.execute("DELETE FROM matches;")
    db.commit()
    db.close()

def deletePlayers():
    """Remove all the player records from the database."""
    db, c = connect()
    c.execute("DELETE FROM players;")
    db.commit()
    db.close()



def countPlayers():
    """Returns the number of players currently registered."""
    db, c = connect()
    c.execute("SELECT COUNT(*) AS num FROM players;")
    num_of_players = c.fetchone()
    db.close()
    # num_of_players returns the first row [0] from the table query
    return num_of_players[0]



def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    db, c = connect()
    c.execute("INSERT INTO players (player_name) VALUES(%s)", (name,))
    db.commit()
    db.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db, c = connect()
    # create view bc query too long
    c.execute("SELECT * FROM standings;")
    player_standings = c.fetchall()
    db.close()
    return player_standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db, c = connect()
    c.execute("INSERT INTO matches(winner,loser) VALUES (%s, %s)", (winner, loser,))
    db.commit()
    db.close()



def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    #db, c = connect()
    standings = playerStandings()
    pairs = []
    total = len(standings)

    for a in range(0, total, 2):
        results = (standings[a][0], standings[a][1], standings[a+1][0], standings[a+1][1])
        pairs.append(results)

    return pairs
    #db.close()

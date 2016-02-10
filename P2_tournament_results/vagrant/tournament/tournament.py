#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#
# REMAINDER:
# execute the file tournament_test.py from console using:
# python tournament_test.py
# If you use sublimetext with python package you can run it with Ctrl+B

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def executeQuery(query, data=None, get_result=False):
    """ Execute an standard query to a database. Returns the result of
        the query if required.

    Args:
      query: String - The SQL query
      data (optional): The query data
      getResult (optional, default False): Boolean - wether a result is needed
    """
    # Connect and get cursor
    connection = connect()
    cursor = connection.cursor()
    # Check data argument and execute cursor depending on data value
    if data is None:
        cursor.execute(query)
    else:
        cursor.execute(query, data)
    connection.commit()
    # check get_result argument and fetchall if needed
    if get_result:
        result = cursor.fetchall()
    # close connection
    connection.close()
    # return result on demand
    if get_result:
        return result


def deleteMatches():
    """Remove all the match records from the database."""
    query = 'DELETE FROM matches;'
    executeQuery(query)


def deletePlayers():
    """Remove all the player records from the database."""
    query = 'DELETE FROM players;'
    executeQuery(query)

def countPlayers():
    """Returns the number of players currently registered."""
    query = 'SELECT count(*) FROM players;'
    result = executeQuery(query, get_result=True)
    # result has only a row with a single column
    return result[0][0]


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    query = 'INSERT INTO players (name) VALUES (%s);'
    data = (name,)
    executeQuery(query, data)


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
    query = 'SELECT * FROM standings;'
    return executeQuery(query, get_result=True)


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    query = 'INSERT INTO matches (winner, loser) VALUES (%s, %s);'
    data = (winner, loser,)
    return executeQuery(query, data)
 
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
    standings = playerStandings()
    total_pairs = len(standings) / 2
    pairs = []
    for pair in range(0, total_pairs):
        player1 = standings[2 * pair]
        player2 = standings[2 * pair + 1]
        pair = (player1[0], player1[1], player2[0], player2[1])
        pairs.append(pair)
    return pairs



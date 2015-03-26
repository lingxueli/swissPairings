#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM matches;")
    DB.commit()   
    DB.close()



def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    c = DB.cursor()
    c.execute("DELETE FROM players;")
    DB.commit()   

    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    c = DB.cursor()
    c.execute("SELECT count(*) FROM players;")
    counts = c.fetchall()[0][0]
    DB.close()
    return counts


    


def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    c = DB.cursor()
    c.execute("INSERT INTO players (name) VALUES (%s);",(name,))
    DB.commit()       
    DB.close()


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
    DB = connect()
    c = DB.cursor()
    c.execute("select players.id AS id, players.name AS name, COALESCE(sum(matches.result),0) AS wins,COALESCE(count(matches.result),0) AS matches from players left join matches on players.id = matches.id GROUP BY players.id ORDER BY wins DESC;")
    result = c.fetchall()
    DB.close()
    return result

    


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    DB = connect()
    c = DB.cursor()
    winner_sql = "INSERT INTO matches(id,result) VALUES (%s, 1);"
    loser_sql = "INSERT INTO matches(id,result) VALUES (%s, 0);"

    
    c.execute(winner_sql,(winner,))
    c.execute(loser_sql,(loser,))
    DB.commit()   
    DB.close()
 
 
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
    standings = playerStandings();
    return [(standings[i-1][0], standings[i-1][1], standings[i][0], standings[i][1]) for i in range(1, len(standings), 2)]


    #DB = connect()
    #c = DB.cursor()
    #c.execute("select t1.id as id1, t1.name as name1, t2.id as id2, t2.name as name2 from tournament t1, tournament t2 where t1.matches = t2.matches and t1.wins = t2.wins and t1.wins>t2.wins;")
    #pairs = [{'id1': row[0], 'name1':str(row[1]),'id2': row[2], 'name2':str(row[3]) } for row in c.fetchall() ]

    #DB.close()

    #return pairs
    



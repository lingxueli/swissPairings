Project Description: Tournament Planner

This project is a Python module running in a Linux Vitural Machine, which uses the PostgreSQL database to keep track of players and matches in a game tournament.

The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

This project has two parts: defining the database schema (SQL table definitions), and writing the code that will use it.


Running Instruction:

1. VirtualBox: 

This modele runs on a configured Vagrant VM. Make sure VirtualBox platform package is installed on your operating system, in order to run the Vagrant. You do not need to launch VirtualBox after installing it.

2. Vagrant: 

Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem.  Download it from vagrantup.com. Install the version for your operating system.

3. Configure the VM:

Use Git to fetch the VM configuration

Windows --- Use the Git Bash program (installed with Git) to get a Unix-style terminal. 
Other systems --- Use your favorite terminal program. Run

git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack

This will give you a directory named fullstack, which contains all the files in the VM.

4.Run the virtual machine:

Using the terminal, change directory to fullstack/vagrant (cd fullstack/vagrant), then type vagrant up to launch your virtual machine.

Once it is up and running, type vagrant ssh to log into it. This will log your terminal in to the virtual machine, and you'll get a Linux shell prompt.


5.Initialize database and tables:

Replace the three files under tournament directory with the files.  Then do this in Linux shell prompt and connect to PostgreSQL:

vagrant@vagrant-ubuntu-trusty-32:~$ cd /vagrant/tournament/
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ psql

Create database and import setting in tournament.sql file.

vagrant=> create database tournament;
vagrant=> \i tournament.sql;
vagrant=> \q;

6.Test the module:

vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py


7.Quit:

Log out the VM: vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ exit

Turn the virtual machine off (without deleting anything): vagrant $ vagrant halt






Code Templates:

The template file tournament.sql is where stored the database schema , in the form of SQL create table commands.

The template file tournament.py is where put the code of this module.

Finally, the file tournament_test.py contains unit tests that will test the functions written in tournament.py.



Functions in tournament.py:

1.registerPlayer(name)

Adds a player to the tournament by putting an entry in the database. The database should assign an ID number to the player. Different players may have the same names but will receive different ID numbers.

2.countPlayers()

Returns the number of currently registered players. This function should not use the Python len() function; it should have the database count the players.

3.deletePlayers()

Clear out all the player records from the database.

4.reportMatch(winner, loser)

Stores the outcome of a single match between two players in the database.

5.deleteMatches()

Clear out all the match records from the database.

6.playerStandings()

Returns a list of (id, name, wins, matches) for each player, sorted by the number of wins each player has.

7.swissPairings()

Given the existing set of registered players and the matches they have played, generates and returns a list of pairings according to the Swiss system. Each pairing is a tuple (id1, name1, id2, name2), giving the ID and name of the paired players. For instance, if there are eight registered players, this function should return four pairings. This function should use playerStandings to find the ranking of players.




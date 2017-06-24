*Tournament program version 1.0 16/06/2017*

>"Tournament project emulates a Swiss tournament system. Using the python application (`tournament_test.py`) you can check if your database and query pass or is usable."

## General Usage Notes:
- This program use a Virtual Machine(VM) to run the python application on the computer.
It adapt the application to use a database backend. If you're already experienced in this field
you may use your own device for creating your database.
- This was designed for beginners who has basic knowledge of python and is learning SQL basics.

## Installation and Setup
The project involved installing the following softwares:
- [python 2.7.13](https://www.python.org/downloads/release/python-2713/) (opt. python 3, most recent)
- [vagrant](https://www.vagrantup.com/)
    * _easy access without creating user, password, server etc._
- [Virtual Machine(VM)](https://www.virtualbox.org/wiki/Downloads) - Choose under 'platform packages'
    * _checks if system is running_

NB: Tested only in Windows 10 via [GitBash](https://git-for-windows.github.io/), and opened with [Atom](https://atom.io/) text Editor.

## Running
1. Open cmd shell, and located to the following directory: `cd /vagrant`
2. Start-up Vagrant with the following code: `vagrant up`
    _If you haven't installed it before it may take several minutes or depending on
your internet speed. After that, whenever you start it up again it should only take seconds._
3. Login Vagrant with the following code: `vagrant ssh`
4. Now you can have access to the program!

Type `psql` to open Vagrant database, and to connect to `tournament.sql` type `\c tournament`. Or type `psql tournament` to access the `tournament.sql` database immediately.

You _must_ open psql to write query (SQL) in the tournament.sql file to create, delete or alter database and tables.

To **logout** exit out of psql type `\q` or `ctrl` + `d`. To logout of vagrant setup type `ctrl` + `d`.

If you want to check errors in the your codes, the run the following command:

`$ python tournament_test.py`

It uses the tournament_test.py file to pass in your code, and display where in a Swiss system tournament inputs fail.



## Available Input Types and Examples
The program use Relational Database with PostgreSQL(psycopg2).

The following tables are involved in the database `tournament.sql`.

NB: To an extent, I used `VIEW` to normalized my data.

```
tournament=> \dt
         List of relations
 Schema |  Name   | Type  |  Owner
--------+---------+-------+---------
 public | matches | table | vagrant
 public | players | table | vagrant
(2 rows)
```

Below is example of the database production when running the `tournament_test.py`.

```
tournament=> select * from standings;
 id  |    player_name    | total_wins | matches_played
-----+-------------------+------------+-------------+----------------
 565 | Twilight Sparkle  |          0 |              0
 566 | Fluttershy        |          0 |              0
 567 | Applejack         |          0 |              0
 568 | Pinkie Pie        |          0 |              0
 569 | Rarity            |          0 |              0
 570 | Rainbow Dash      |          0 |              0
 571 | Princess Celestia |          0 |              0
 572 | Princess Luna     |          0 |              0
(8 rows)
```

To view list of database use `\l`, and to exit out of it press `q`. (This is access in the vagrant psql database.)

Tournament program can be reached at:

Voice: n/a

Web site: n/a

E-mail: unorthodoxthing@gmail.com

_Copyright 2016
Copyright for educational purposes from Udacity as Intro To Programming - Exracurricular Back-End Developer: Tournament Results Project
All other brand and product names are trademarks or registered_

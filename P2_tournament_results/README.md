# P2: Tournament results

A relational DB (Postgre SQL) project created for the second Project of Udacity's [Full Stack Web Developper Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

## Features

This project has a Python module that uses the PostgreSQL database to keep track of players and matches in a game tournament with swiss pairings.

The game tournament use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible.

### Basic & extra features

`tournament` forlder contains basic implementation of project especifications

`tournament-plus` folder contains an extra, it supports draw (tied games)

## How to run

### Requirements

This project has a Vagrant virtual machine you can use with all required software already installed and configured by Udaticy. This requires you have installed Vagrant and Virtual Box.

### Run


1. Clone this repository and log in the virtual machine with this commands:

  ```sh
  cd vagrant      # go to the vagrant folder
  vagrant up      # powers on the virtual machine
  vagrant ssh     # logs into the virtual machine
  ```
2. Once loged in the virtual machine go to the tournament project directory:

  ```sh
  cd /vagrant/tournament
  ```

3. Run Postgre SQL already installed in the virtual machine with:

  ```sh
  psql
  ```
4. Create the databases with the `tournament.sql` file and then exit

  ```sh
  \i tournament.sql
  \q
  ```
5. Now you can run the tests with the command below or you can run functions in tournament.py for your tournament.

  ```sh
  python tournament_test.py
  ```

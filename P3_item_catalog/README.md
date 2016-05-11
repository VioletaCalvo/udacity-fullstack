# P3: Catalog Tournament

An app created for the 3th Project of Udacity's [Full Stack Web Developper Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004).

Demo version [here](https://udacity-catalog.herokuapp.com)

## Features

#### API Endpoints

This app implements a JSON endpoint that serves the catalog information at `http://localhost:8000/catalog.json`

#### CRUD

This app implements CRUD opreations from a database. Create, Update and Delete operations are only allowed for logged users.

#### Authentication & Authorization

This apps uses Google and Facebook as authentication & authorization service.


## How to run

### Requirements

This project has a Vagrant virtual machine you can use with all required software already installed and configured by Udaticy. This requires you have installed Vagrant and Virtual Box.

This project users Google and Facebook services for authentication & authorization. You must configure your apps on both services in order to run this app.

### Run


1. Clone this repository and log in the virtual machine with this commands:

  ```sh
  cd vagrant      # go to the vagrant folder
  vagrant up      # powers on the virtual machine
  vagrant ssh     # logs into the virtual machine
  ```
2. Once loged in the virtual machine go to the tournament project directory:

  ```sh
  cd /vagrant/catalog
  ```

3. Setup database, initialize database with categories:

  ```sh
  python database_setup.py
  ```

4. Replace your client secrets for Facebook and Google sing in:

  * Replace your Facebook client secrets in `clientsecrets_facebook.json`
  * Replace your Google client secrets in `clientsecrets_google.json`

  _NOTE: You must configure your Google and Facebook apps correctly_


5. Now you can run the application:

  ```sh
  python application.py
  ```

6. Go to your browser an type `localhost:8000`

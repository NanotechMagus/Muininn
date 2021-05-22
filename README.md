# Muininn

## The Project
Muininn is a personal python project with three (potentially four) distinct parts:

* Sirocco Discord Bot
  * Eldrfalk Guilded Bot (potential)
* Muininn Back-end application
* Solringen Web Interface
  
These distinct parts have the following goals:
* Provide Solringen Enterprise Discord users the ability to access certain information from various gaming APIs
* Allow registered users on the Solringen website the ability to register as a client or contractor
* Provide a queuing system for linking client requests to available contractors (FIFO) based on contract type
* Maintain a list of validated reputation as a function of user score and completed contracts
* Link the interface and automation of queues and group creation between the Solringen website and Discord // Guilded to provide seamless interaction with all three

## The Thoughts and Musings behind the Project

### The Sirocco Discord should do the following:
* Provide output for certain API queries in a permitted channel
    - FleetYards.net
    - xivapi.com
    - citizendb - internal
    - reddit
    - twitter
    - robertsspaceindustries.com
* Interface with Muininn - internally developed queue application - to push and receive information about a job
* Provide RESTful information to an admin panel integrated with Huginn (docker agent app)
* Interface with a Mongo database for Users that is shared between Muininn and the Solringen Django project
* Digest and resend webhook information to specific channels
* Provide a list of admin commands usable only by specific roles
* Provide a welcome message to any new users about the role of the bot and server
* Create any number of monitored messages (via reactions) and do a pre-programmed task with each.
* Potentially create a semi-anonymized messaging system between users should cross-platform emerge

### The Muininn Back-end application should do the following:

* Orchestrate the queue technology in an expedient manner by linking clients with contractors
* Push a notification through Discord to the queued clients and contractors via Sirocco 
* Interface with MongoDB to provide the following
  * Maintain a record of users' jobs and history.
  * Maintain a ledger of credits and debits to users' accounts
  * Maintain cached information readily available to Sirocco and Solringen
* Potentially provide a secure messaging backend between two users should a cross-platform issue occur (Discord vs Guilded)
* Hook for future implementation of RSI API

### The Solringen web Interface should do the following:

* Provide user account access and control
* Provide an administration interface to both Muininn and the Sirocco bot
* Discord OAuth integration to easily link Discord information with uniquely identified users
* Potentially provide a secure messaging system between users on multiple platforms
* Provide a ledger of transactions -- client and/or contractor
* Future Integration with Kofi or Patreon to allow for crowd-sourced funding and automated ledger rewards

## Technologies

This project will utilize the following
* Discord bot - **Python**
* Web Framework - **Django**
* Internal API - **Flask**
* noSQL Database - **MongoDB**
* Cache - **Redis**

## Contributing

As this is a personal project, feel free to follow along in the development, but this is more for myself.  In the future when there may be a need for multiple developers, contributions will be welcomed then.

## License
[MIT](https://choosealicense.com/licenses/mit/)
# Muininn

## The Project
Muininn is a personal python project with five distinct goals:

* Provide Solringen Enterprise Discord users the ability to access certain information from various gaming APIs
* Allow registered users on the Solringen website the ability to register as a client or contractor
* Provide a queuing system for linking client requests to available contractors (FIFO) based on contract type
* Maintain a list of validated reputation as a function of user score and completed contracts
* Link the interface and automation of queues and group creation between the Solringen website and Discord // Guilded to provide seamless interaction with all three

## The Thoughts and Musings behind the Project
This is the main back-end file for the Sirocco application designed to provide an interface between the Solringen Django project and the Sirocco Discord bot.

### This bot should do the following:
   * Provide output for certain API queries in a permitted channel
        - FleetYards.net
        - xivapi.com
        - citizendb - internal
        - reddit
        - twitter
        - robertsspaceindustries.com
    * Interface with Muininn - internally developed queue application - to push and receive information about a job
    * Provide RESTful information to an admin panel integrated with Huginn
    * Interface with a Mongo database for Users that is shared between Muininn and the Solringen Django project
    * Digest and resend webhook information to specific channels
    * Provide a list of admin commands usable only by specific roles
    * Provide a welcome message to any new users about the role of the bot and server
    * Create any number of monitored messages (via reactions) and do a pre-programmed task with each.


### Front-End Methodology:

   * Use different cogs to integrate specific commands to the bot - e.g. /xiv or /sc
   * Reacting to any Muininn-monitored messages will send a message conducting a transaction with the user

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
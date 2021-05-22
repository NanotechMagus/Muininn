#!/etc/python-3.9

# Standard Library Imports

# Locally Developed Imports

# Third Party Imports

"""
This is the main back-end file for the Sirocco application designed to provide an interface between the Solringen
Django project and the Sirocco Discord bot.

This bot should do the following:
    - Provide output for certain API queries in a permitted channel
        - FleetYards.net
        - xivapi.com
        - citizendb - internal
        - reddit
        - twitter
        - robertsspaceindustries.com
    - Interface with Muininn - internally developed queue application - to push and receive information about a job
    - Provide RESTful information to an admin panel integrated with Huginn
    - Interface with a Mongo database for Users that is shared between Muininn and the Solringen Django project
    - Digest and resend webhook information to specific channels
    - Provide a list of admin commands usable only by specific roles
    - Provide a welcome message to any new users about the role of the bot and server
    - Create any number of monitored messages (via reactions) and do a pre-programmed task with each.

Methodology:
    - Use different cogs to integrate specific commands to the bot - e.g. /xiv or /sc
    - Reacting to any Muininn-monitored messages will send a message conducting a transaction with the user
"""
# Pushetta skill

A simple skill for sending push notifications to one channel with Pushetta. Maybe in the future I will implement support for multiple channels.

## How to install

Unzip or clone `PushettaSkill` into `mycroft-core/mycroft/skills` directory.

`pip install pushetta` into Mycroft's virtual environment.

Restart mycroft instance and test with the sentence like "push it remember to go buy milk".

In the config file you need to create an entry for the Pushetta skill with the api key and channel name.

Example:

  },
  "PushettaSkill": {
    "pushetta_api_key": "xxxxxxxxxxxxxxxxx",
    "pushetta_channel": "Blabla channel"
  }, 

# rollbot-discordbot

rollbot is a python discord bot that allows a server's members to roll dice.

Current Commands:
- !help  
This will post a message in the same channel the bot read the message showing the formats of other commands to use with rollbot.  

- !roll 20  
The above will roll a random number on a d20. (Works with any number rather than just the generic dice side number).  

- !roll 2d8+3  
This will roll two 8 sided dice and add 3 to the result. This will only show you the total value at the end of the roll and modifier. (The modifier can be negative as well)  

- !rollout 5d20  
Will roll five 20 sided dice, and post a message containing what each dice rolled as well as a final message with the total.


## Requirements
```pip install discord```

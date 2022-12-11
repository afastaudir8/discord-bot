# discord-bot
This is the Discord bot I made for the official RampRage game Discord server.


## Why I open sourced my bot
Basically, I haven't updated the bot for over 2 months now. If anyone wants to add stuff to it, go for it. I give you permission to make fun of my shitty code.

### If you want to modify the bot to make a pull request, please fork the `dev` branch.

## Known issues

The translate command sometimes doesn't work. This is presumably due to the GoSlate library not working well with how I made the command.

## Install

### Download

To download the bot's files, first run

```
git clone --recursive https://github.com/afastaudir8/discord-bot
```
If you want to, you can clone the `dev` branch. 
>**Warning**
>The dev branch is a branch that may not work at all depending on what I'm doing with it. I will not help you with it.
```
git clone --recursive https://github.com/afastaudir8/discord-bot --branch dev
```

### Prerequisites

First, you have to install python. Linux and macOS should have Python built in (albeit, possibly with an outdated build). On Windows you need to install seperately from [here](https://www.python.org/). You also need to have `pip` installed.


To install the required python modules, `cd` into the bot's directory then run the following 
```
pip3 install -r ./requirements.txt
```
If that doesn't work for you, use one of the following commands

```
python3 -m pip install -r ./requirements.txt
```
or this on Windows
```
python -m pip install -r ./requirements.txt
```

The bot *should* work after installing these

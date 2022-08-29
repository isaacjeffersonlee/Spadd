# Spadd: Spotify Add

#### Author: Isaac Lee
#### Date: 13/08/2022

## Introduction
Often I am listening to music and doing something else
on my computer and a song comes on I think is groovy.
Navigating to Spotify and using my mouse to select which
playlist I want to add it to is not fun.

This is much more fun!
Select a playlist using bemenu/dmenu
and then add the currently playing spotify track to it.

## Installation 
Go to https://developer.spotify.com/dashboard/ and login and
then add an app. Edit the settings and add a redirect URI.
This can be any webpage but I just use: https://www.google.com/ 

Then run the install script and input the details and you should be
all good to go!

### Requirements
Requires dmenu / bemenu
```
sudo pacman -S bemenu dmenu
```

Then to install just run the install script:
```sh
./install.sh
```


## Keybinding
I personally use this script along with a keybinding mod+s.
This makes it frictionless to add the currently playing song
to any of my playlists.


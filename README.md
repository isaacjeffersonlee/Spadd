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

The first time you run it, you will be redirected to your browser to 
accept the user permissions. Once you have accepted you should be
taken to your redirect URL. Copy this url back into the terminal and
everything should be setup.

The next time you run spadd everything should work!

### Requirements
Requires dmenu / bemenu
```
sudo pacman -S bemenu dmenu
```

The only python requirement is spotipy:

```shell
pip install spotipy
```



### Installing

Then to install just run the install script:
```sh
./install.sh
```


## Keybinding
I personally use this script along with a keybinding mod+s.
This makes it frictionless to add the currently playing song
to any of my playlists. An example binding from my Sway config:

```shell
bindsym $mod+s exec ./Projects/Spadd/spadd/spadd_run.py
```




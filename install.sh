#!/bin/sh

echo ""
echo "Spadd Install Script"
echo "--------------------"
echo ""
echo "Please visit: https://developer.spotify.com/dashboard/login"
echo ""

read -p "Spotify Client ID: " CLIENT_ID 
read -p "Spotify Secret: " CLIENT_SECRET
read -p "Spotify Redirect URI: " REDIRECT_URI

echo "# .* This config file was automatically generated *." > credentials.py
echo "client_id = '$CLIENT_ID'" >> credentials.py
echo "client_secret = '$CLIENT_SECRET'" >> credentials.py
echo "redirect_uri = '$REDIRECT_URI'" >> credentials.py

echo "Generated ./credentials.py"

echo "pip installing spotipy..."
pip install -r requirements.txt

echo "------------------------------------------------------------------"
echo ""
echo "Finished!"
echo ""
echo "The first time you run spadd.py, you will be redirected to"
echo "your redirect uri. Accept the stuff and copy the url as prompted."

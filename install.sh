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

echo "{" >> credentials.json
echo "  \"CLIENT_ID\":" "\"$CLIENT_ID\"," >> credentials.json
echo "  \"CLIENT_SECRET\":" "\"$CLIENT_SECRET\"," >> credentials.json
echo "  \"REDIRECT_URI\":" "\"$REDIRECT_URI\"" >> credentials.json
echo "}" >> credentials.json

echo "Generated credentials.json:"
cat credentials.json

echo "pip installing requirements..."
pip install -r requirements.txt
echo "pip installing spadd"
cd .. && pip install -e Spadd

echo "------------------------------------------------------------------"
echo ""
echo "Finished!"
echo ""
echo "The first time you run spadd.py, you will be redirected to"
echo "your redirect uri. Accept the stuff and copy the url as prompted."

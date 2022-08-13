#!/usr/bin/env python3

import credentials
import subprocess
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = [
    "playlist-modify-private",
    "playlist-modify-public",
    "playlist-read-private",
    "user-read-playback-state",
    "user-read-currently-playing",
    "playlist-read-collaborative",
]

# Client Credentials
client_secret = credentials.client_secret
client_id = credentials.client_id
redirect_uri = credentials.redirect_uri

# Where to look for .cache
cache_path = os.path.dirname(__file__) + "/.cache"

# Where to look for spotify icon for notifications
images_path = os.path.dirname(__file__) + "/Images"

auth_manager = spotipy.oauth2.SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    cache_path=cache_path,
    scope=scope,
)

sp = spotipy.Spotify(auth_manager=auth_manager)


def sp_notify(title: str, description: str, duration: int) -> None:
    """Send a notification for duration secs with title and description."""
    t = duration * 1000
    os.system(
        f"notify-send -t {t} -i {images_path}/spotify_logo.png "
        + f"'{title}' '{description}'"
    )


def bemenu_show(items: list, bemenu_cmd: str = "bemenu -i") -> str:
    """Display items with bemenu and return selected item."""
    newline_items = "\\n".join([str(item) for item in items])
    cmd = f"printf '{newline_items}' | {bemenu_cmd} -l {len(items)}"
    ps = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    return str(ps.communicate()[0]).strip("b").replace("'", "").replace("\\n", "")


def main():
    playlists = sp.current_user_playlists(limit=50, offset=0)["items"]
    playlist_names = [playlist["name"] for playlist in playlists]
    playlist_name = bemenu_show(playlist_names)
    if playlist_name is None:
        pass
    else:
        for playlist in playlists:
            if playlist["name"] == playlist_name:
                playlist_uri = playlist["uri"]

        current_track_info = sp.current_user_playing_track()
        if current_track_info:
            cur_track_uri = current_track_info["item"]["uri"]
            sp.playlist_add_items(playlist_uri, [cur_track_uri])
            sp_notify(
                title="Added Song",
                description=f'Added {sp.current_user_playing_track()["item"]["name"]} to {playlist_name}',
                duration=4,
            )
        else:
            sp_notify(
                title="Spadd",
                description="Failed to add track: no track is currently playing!",
                duration=4
            )


if __name__ == "__main__":
    main()

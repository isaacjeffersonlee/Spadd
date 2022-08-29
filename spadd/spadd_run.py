#!/usr/bin/env python3
import subprocess
import os
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Absolute path of the spadd module directory
MODULE_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__))
)
# Absolute path of the parent directory of spadd module
ROOT_PATH = os.path.dirname(MODULE_PATH)
# Get app credentials
with open(f"{ROOT_PATH}/credentials.json", 'r') as f:
    credentials = json.load(f)
CLIENT_SECRET = credentials["CLIENT_SECRET"]
CLIENT_ID = credentials["CLIENT_ID"]
REDIRECT_URI = credentials["REDIRECT_URI"]
# Other paths
CACHE_PATH = ROOT_PATH + "/.cache"
IMG_PATH = ROOT_PATH + "/Images"
# Spotify permissions required
SCOPE = [
    "playlist-modify-private",
    "playlist-modify-public",
    "playlist-read-private",
    "user-read-playback-state",
    "user-read-currently-playing",
    "playlist-read-collaborative",
]
# Initialize Spotify OAuth2 Authentication manager
AUTH_MANAGER = spotipy.oauth2.SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    cache_path=CACHE_PATH,
    scope=SCOPE,
)
# Initialize spotipy object with our authentication manager
sp = spotipy.Spotify(auth_manager=AUTH_MANAGER)


def sp_notify(title: str, description: str, duration: int) -> None:
    """Send a notification for duration secs with title and description.

    Display a notification with the spotify logo for input duration seconds.
    Depending on the notification manager of the system, duration may not
    actually work.

    Parameters
    ----------
    title : str
        Title of notification
    description : str
        Description of the notification
    duration : int
        How many *seconds* to display the notification for
    """
    t = duration * 1000
    os.system(
        f"notify-send -t {t} -i {IMG_PATH}/spotify_logo.png "
        + f"'{title}' '{description}'"
    )


def menu_show(items: list[str], prompt: str = "> ") -> str:
    """Display items with dmenu/bemenu and return selected item.

    XDG_SESSION_TYPE is queried and either dmenu or bemenu is used
    depending on whether wayland or x11 is being used.

    Parameters
    ----------
    items : list[str]
        Items to display in a vertical list using dmenu/bemenu
    prompt : str
        Left prompt to pass to the -p flag

    Returns
    -------
    str
        Selected item
    """
    xdg_session_type = os.getenv("XDG_SESSION_TYPE")  # wayland vs x11
    if xdg_session_type == "wayland":
        menu = "bemenu"
    else:  # Fallback to dmenu if x11 or $XDG_SESSION_TYPE not found
        menu = "dmenu"
    newline_items = "\\n".join([str(item) for item in items])
    cmd = f"printf '{newline_items}' | {menu} -i -p '{prompt}' -l {len(items)}"
    ps = subprocess.Popen(
        cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT
    )
    # Convert bytes object to string and remove unwanted characters
    return str(ps.communicate()[0]).strip("b").replace("'", "").replace("\\n", "")


def main() -> None:
    """Entry point."""
    playlists = sp.current_user_playlists(limit=50, offset=0)["items"]
    playlist_names = [playlist["name"] for playlist in playlists]
    playlist_name = menu_show(playlist_names, "Select playlist: ")
    if not playlist_name:
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
                description=f"Added "
                + f"{sp.current_user_playing_track()['item']['name']}"
                + f"to {playlist_name}",
                duration=4,
            )
        else:
            sp_notify(
                title="Spadd",
                description="Failed to add track: no track is currently playing!",
                duration=4,
            )


if __name__ == "__main__":
    main()

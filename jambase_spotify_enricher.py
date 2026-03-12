#!/usr/bin/env python3

import requests
import pandas as pd
from tqdm import tqdm
import time
import os

API_KEY = os.getenv("JAMBASE_API_KEY")

if not API_KEY:
    raise ValueError("JAMBASE_API_KEY environment variable not set")

INPUT_XLSX = "/Users/saugat/Downloads/jambase_events_spotify_lookup.xlsx"
OUTPUT_XLSX = "/Users/saugat/Downloads/jambase_events_with_spotify.xlsx"

BASE_URL = "https://www.jambase.com/jb-api/v1/events/id"


def get_spotify_from_event(jambase_id):

    url = f"{BASE_URL}/{jambase_id}"

    params = {
        "apikey": API_KEY,
        "expandExternalIdentifiers": "true"
    }

    try:

        r = requests.get(url, params=params, timeout=20)

        if r.status_code != 200:
            return None, None, None

        data = r.json()

        event = data.get("event", {})

        event_name = event.get("name")

        performers = event.get("performer", [])

        if not performers:
            return event_name, None, None

        artist = performers[0]

        artist_name = artist.get("name")

        spotify_id = None

        external_ids = artist.get("x-externalIdentifiers", [])

        for ext in external_ids:
            if ext.get("source") == "spotify":
                ids = ext.get("identifier")

                if isinstance(ids, list) and ids:
                    spotify_id = ids[0]

        return event_name, artist_name, spotify_id

    except Exception:
        return None, None, None


def main():

    df = pd.read_excel(INPUT_XLSX)

    events = []
    artists = []
    spotify_ids = []

    for jambase_id in tqdm(df["JamBase Event ID"], desc="Fetching JamBase events"):

        event_name, artist_name, spotify_id = get_spotify_from_event(jambase_id)

        events.append(event_name)
        artists.append(artist_name)
        spotify_ids.append(spotify_id)

        time.sleep(0.2)

    df["Event Name (API)"] = events
    df["Artist Name (API)"] = artists
    df["Spotify Artist ID"] = spotify_ids

    df.to_excel(OUTPUT_XLSX, index=False)

    print("\nSaved file:")
    print(OUTPUT_XLSX)


if __name__ == "__main__":
    main()

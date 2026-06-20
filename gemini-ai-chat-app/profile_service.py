import json
import os

PROFILE_FILE = "user_profile.json"


def load_profile():

    if os.path.exists(PROFILE_FILE):

        with open(PROFILE_FILE, "r") as file:
            return json.load(file)

    return {}


def save_profile(profile):

    with open(PROFILE_FILE, "w") as file:
        json.dump(profile, file, indent=4)
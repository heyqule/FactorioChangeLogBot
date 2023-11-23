import os
import json

json_obj = {}


def get_known_mods():
    try:
        with open('data.json') as f:
            json_obj = json.load(f)
        return json_obj
    except RuntimeError as re:
        return {}


def set_version_and_changelog(mod_id, last_version, last_posted_changelog):
    json_obj[mod_id] = {'last_known_version': last_version, 'last_posted_changelog': last_posted_changelog}
    return True


def set_last_known_version(mod_id, last_known_version):
    json_obj[mod_id].last_known_version = last_known_version
    return True


def write_json():
    with open('data.json', 'w') as f:
        json.dump(json_obj, f)

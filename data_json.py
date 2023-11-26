import os
import json


def get_known_mods():
    try:
        with open('data.json') as f:
            json_obj = json.load(f)
            return json_obj
    except json.decoder.JSONDecodeError as re:
        return {}


def set_version_and_changelog(json_obj, mod_id, last_version, last_posted_changelog):
    json_obj[mod_id] = {'last_known_version': last_version, 'last_posted_changelog': last_posted_changelog}
    return json_obj


def set_last_known_version(json_obj, mod_id, last_known_version):
    json_obj[mod_id].last_known_version = last_known_version
    return json_obj


def write_json(json_obj):
    with open('data.json', 'w') as f:
        json.dump(json_obj, f)

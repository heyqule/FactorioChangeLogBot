from version_checker import get_updated_mods
from data_json import get_known_mods
from data_json import set_version_and_changelog
from data_json import write_json
from datetime import datetime
from discord_poster import send_changelog_messages


def run_checker():
    known_mods_saved_info = get_known_mods()
    new_changelogs, known_mods_saved_info = get_updated_mods(known_mods_saved_info)

    changelogs_to_post = []

    if new_changelogs:
        for changelog in new_changelogs:
            last_posted_changelog = known_mods_saved_info[changelog.mod_id][
                'last_posted_changelog'] if changelog.mod_id in known_mods_saved_info else None
            known_mods_saved_info = set_version_and_changelog(
                known_mods_saved_info,
                changelog.mod_id,
                changelog.last_version,
                changelog.changelog
            )
            if changelog.changelog != last_posted_changelog:
                # Only post if the actual changelog text is different from the last one we posted
                print('Adding {} to post messages...'.format(changelog.mod_id))
                changelogs_to_post.append(changelog)
            else:
                print('WARN - Mod {} was upgraded but with the same changelog!'.format(changelog.mod_id))

    if changelogs_to_post:
        print('Posted to chat...')
        send_changelog_messages(changelogs_to_post)
    else:
        print('Did nothing...')

    write_json(known_mods_saved_info)

if __name__ == '__main__':
    print('Started factorio log change bot on {}...'.format(datetime.now()))
    run_checker()

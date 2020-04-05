import json
import os
import subprocess
import uuid

from datetime import datetime, timedelta
from mutagen.easyid3 import EasyID3
from gmusicapi import Musicmanager


def record(rule, file_name):
    print(f'recording {rule["title"]} ...')
    proc = subprocess.run(
        './rec_radiko_ts.sh' \
        f' -s {rule["station"]}' \
        f' -f {YESTERDAY.strftime("%Y%m%d")}{rule["start"]}' \
        f' -d {rule["duration"]}' \
        f' -o "/tmp/{file_name}"',
        shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )


def tagging(rule, file_name):
    print(f'tagging {rule["title"]} to {file_name} ...')
    tags = EasyID3(f'/tmp/{file_name}')
    tags['title'] = YESTERDAY.strftime('%Y-%m-%d')
    tags['album'] = rule['title']
    tags['artist'] = rule['artist']
    tags.save()


def upload(mm, file_name):
    print(f'uploading {file_name} ...')
    mm.upload(f'/tmp/{file_name}')


def main():
    mm = Musicmanager()
    mm.login('./oauth_credentials', uploader_id='0A:1B:2C:3D:4E:5F')

    rules = []
    with open('./rules.json') as f:
        rules = json.load(f)

    for rule in rules:
        if rule['weekday'] == YESTERDAY.weekday():
            file_name = f'{str(uuid.uuid4())}.mp3'

            record(rule, file_name)
            tagging(rule, file_name)
            upload(mm, file_name)
            os.remove(f'/tmp/{file_name}')


if __name__ == '__main__':
    YESTERDAY = datetime.today() - timedelta(days=1)
    main()

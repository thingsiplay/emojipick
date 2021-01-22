#!/usr/bin/python3

# Copyright (c) 2021 Tuncay D.
# MIT License, see LICENSE

import sys
import pathlib
import json
import urllib.request
import argparse

jdir = pathlib.Path('~/.cache/emojiget')
jdir = jdir.expanduser()
jfile = pathlib.Path(jdir / 'emoji.json')
jfile_filtered = pathlib.Path(jdir / 'emoji_filtered.json')

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filter', default='',
        help='print emoji only if name contains filter')
parser.add_argument('-l', '--limit', default=0, type=int,
        help='limit the number of output emojis, defaults to 0 (no limit')
parser.add_argument('-n', '--no-name', default=False, action='store_true',
        help='do not output emoji names')
parser.add_argument('-c', '--clean', default=False, action='store_true',
        help='delete temporary emoji files, redownload and recreate them')
args = parser.parse_args()

if args.clean:
    jfile.unlink(missing_ok=True)
    jfile_filtered.unlink(missing_ok=True)
    jdir.rmdir()
    sys.exit(0)

if jfile_filtered.exists():
    jtext = jfile_filtered.read_text()
    emojis = json.loads(jtext)
else:
    if jfile.exists():
        jtext = jfile.read_text()
    else:
        jdir.mkdir(exist_ok=True)
        # Source: overatgithub/emoji.json
        # Alternate = 'https://gist.githubusercontent.com/thingsiplay/1f500459bc117cf0b63e1f5c11e03963/raw/d8e4b78cfe66862cf3809443c1dba017f37b61db/emojis.json'
        jurl = 'https://gist.githubusercontent.com/oliveratgithub/0bf11a9aff0d6da7b46f1490f86a71eb/raw/d8e4b78cfe66862cf3809443c1dba017f37b61db/emojis.json'
        jresponse = urllib.request.urlopen(jurl)
        jdata = jresponse.read()
        jtext = jdata.decode('utf-8')
        jfile.write_text(jtext)

    emojis = json.loads(jtext)
    filtered_emojis = []
    for emoji in emojis['emojis']:
        if emoji['order'] != '':
            filtered_emojis.append(emoji)
    emojis['emojis'] = filtered_emojis
    jfile_filtered.write_text(json.dumps(emojis))

for index, emoji in enumerate(emojis['emojis']):
    if args.filter in emoji['name']:
        if args.no_name:
            print(emoji['emoji'])
        else:
            print(emoji['emoji'], emoji['name'])
        if args.limit > 0 and index > args.limit:
            break

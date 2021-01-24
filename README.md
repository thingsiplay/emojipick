# Emoji Picker

Get a selection of emojis and pick one to copy to clipboard.

- **Author**: Tuncay D.
- **License**: [MIT License](LICENSE)
- **Source**: [Github source](https://github.com/thingsiplay/emojipick)

## Introduction

Are you tired of the preinstalled Emoji tools that comes or does not come with
your distro and you wish to use a different one? Yeah, me neither. Here is it
anyway.

![dmenu](emojipick.png)

## Usage

On first run a small file from Github will be downloaded, containing the emoji
data. This is needed only once. The script itself will open a small bar on top
of the screen, with a list of smileys and other emojis. Type in something to
filter and narrow down the selection. Use the arrow keys to navigate and
Enter to select.

On selection a notification will appear and the emoji is copied to clipboard.
It is also send to stdout (echo in terminal). There is not much to configure,
just open the script itself and edit them as you like. If you want use `rofi`
instead of `dmenu`, there is a setting to enable it in `emojipick` file. For
that install rofi and enable it by changing the line `use_rofi=0` to
`use_rofi=1` in the file "emojipick". It solves 2 problems I had with dmenu. 1.
rofi supports colored emojis, 2. dmenu was a bit sluggish in my experience.

My recommendation is to assign a shortcut to the script `emojipick` and call it
from any place you need. Alternatively you can also use it as a commandline
tool, as it outputs to stdout.

You can use a favorites file with your emojis, which will be displayed at top
of the dmenu list. The default location is at `~/.myemojis` and should be
formatted like:

```
❤️ name
😂 name
```

The location of this file can be changed in the script `emojipick`.

## How it works

The entire script is based on 2 parts, one Python program responsible for
downloading and converting and saving the emoji database. The other script is a
regular Bash script and is combining the Python program with a handful of other
useful little tools. Just in the spirit of the Unix philosophy.

As these are little indipendent programs called after one another, it is very
easy to customize (if you know how to deal with it). Or just put another
program in the pipeline and modify its working with the regular Linux command
line tools. It uses minimal programs like "dmenu" and "xclip".

The emojis and their description are downloaded from
[gist.github.com/oliveratgithub/emojis.json](https://gist.github.com/oliveratgithub/0bf11a9aff0d6da7b46f1490f86a71eb) .

## Installation and Requirements

It does not require any installation of the script itself, just run
`emojipick` script. A few little programs must be present on the machine.
Required are:

- python3
- awk
- dmenu (not needed if rofi is enabled)
- xclip
- notify-send
- rofi (only if enabled)


## Feedback

If you want report a bug or have any questions, then [leave me a message](https://thingsiplay.game.blog/contact/) on my contact page.


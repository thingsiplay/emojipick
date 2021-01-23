# Emoji Picker

Get a selection of emojis and pick one to copy to clipboard.

- **Author**: Tuncay D.
- **License**: [MIT License](LICENSE)
- **Source**: [Github source](https://github.com/thingsiplay/emojipick)

![dmenu](emojipick.png)

## Introduction

Are you tired of the preinstalled Emoji tools that comes or does not come with
your distro and you wish to use a different one? Yeah, me neither. Here is it
anyway.

## Usage

On first run it will download the emoji data from github. This is only needed
once. On execution it will open a small bar on top of your display with a
selection of emojis. You can filter and narrow down a few of them. Use arrow
keys to navigate through the list. If an emoji is selected via Enter key, it
will be copied to clipboard and a little notification appears.

My recommendation is to assign a shortcut to the script `emojipick` and call
it from any place you need. It will copy the selected emoji to the clipboard.
Alternatively you can also use it as a commandline tool. It will output to
stdout too. There is not much to configure, just open the scripts itself and
edit them as you like.

## How it works

The entire script is based on 2 parts, one Python program responsible for
downloading and converting and saving the emoji database. The other script is a
regular Bash script and is combining the Python program with a handful of other
useful little tools. Just in the spirit of the Unix philosophy.

As these are little indipendent programs called after one another, it is very
easy to customize (if you know how to deal with it). Or just put another
program in the pipeline and modify its working with the regular Linux command
line tools. It uses minimal programs like "dmenu" and "xclip".

Alternatively you can use "rofi" now, instead of "dmenu". It is a drop in
replacement, and works similar. For that install rofi and enable it by changing
the line `use_rofi=0` to `use_rofi=1` in the file "emojipick". It solves 2
problems I had with dmenu. 1. rofi supports colored emojis, 2. dmenu was a bit
sluggish in my experience.

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


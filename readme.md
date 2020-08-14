# M3U Playlist Export Script

This is a small python script that can scan a m3u playlist and copy all the songs in the same order to a new location, specified by the use. It is designed for personal use, so it might need some adjustments before running. The script encodes and decodes filename using UTF-8, so most of the languages are supported.

## How To Use The Script

When running the script, it will ask you to provide to parameters:

* **Source** - a path to a m3u playlist or a path to some directory.
* **Target** - a path to a destination folder.

If the source is a playlist, the script scans it and copies all its songs to the target location. It assigns numbers to the beginning of each copied file, so they appear in the same order as in the playlist. If the source is a folder, it scans  the folder for m3u files, and repeats the same process for each playlist it finds. However, it does not scan subfolders.

## Modifications You Might Want To Consider

* The script assumes every music file that's being copied is of the form `[track number] [title].[extension]`. It cuts out the `[track number]` and replaces it with a new number. However, if the file is of the form `[title].[extension]` it might remove part of the title. So you may want to change this behavior before running the script.
* The script asks the user to type in the source file/folder and the target folder at runtime. However, it is sometimes more convenient to pass these parameters from the command line. So you may want to change this. 
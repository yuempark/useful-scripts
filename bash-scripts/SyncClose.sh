#!/bin/sh
# This script closes syncing services.

cd /Applications

osascript -e 'tell application "Box Sync" to quit'

osascript -e 'tell application "Dropbox" to quit'

osascript -e 'tell application "Backup and Sync" to quit'

cd

printf "   Closed: \033[0;35mBox Sync\033[0m\n"
printf "   Closed: \033[0;35mDropbox\033[0m\n"
printf "   Closed: \033[0;35mGoogle Drive\033[0m\n"

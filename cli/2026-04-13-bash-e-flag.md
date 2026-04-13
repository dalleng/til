# Make a bash script fail on command failure

`set -e` in bash makes the script fail on any command returning a non 0 return value. The default behavior without
that option set is for the script to continue execution even after some commands have failed.
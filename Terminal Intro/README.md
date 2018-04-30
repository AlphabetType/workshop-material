# Commandline

## Working with files and folders


`cd`: Changes directory. You can drag the destination into the terminal windows instead of typing the path.

`cd ..`: Move one directory up.

`mkdir`: Creates a directory.

`touch`: Creates a file.

`ls -al`: Displays all files of current directory in a list view.

`open .`: Opens the Finder windows on the current location.

`open`: Opens a file in it’s standard application.

`mv`: Moves file; can also be used to rename file.

`ditto`: Copy folder to another destination.

## Navigating the terminal

`pwd`: Shows current path.

`ctrl`+`c`: Cancels current process.

`cmd`+ `k`: Clears terminal.

`history`: Shows last used commands.

`↑`: (Arrow up) Use last command; cycles through history.

`⇥`: (tab key) Completes filenames.

`alt`+ (click): Move cursor to specific position in command.


## Handy commands

`base64`: Shows file as base64 string.

### Plz help!
You can use the argument `-h` after any command to see the usage help of it.

### Do this!
`sudo`: Authenticate yourself as superuser to gain extra priviliges to do stuff.

### Show hidden files
`defaults write com.apple.finder AppleShowAllFiles TRUE`:
`killall Finder`:

### Show file extensions
`defaults write NSGlobalDomain AppleShowAllExtensions -bool true`:
`killall Finder`:

### Stay awake!
`caffeinate`:
`cmd`+ `c`:

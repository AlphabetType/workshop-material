# Commandline

## Working with files and folders

| Command | Description |
| --- | --- |
|`cd`| Changes directory. You can drag the destination into the terminal windows instead of typing the path. ![cd](https://github.com/AlphabetType/workshop-material/raw/master/Terminal%20Intro/Example%20Images/cd.png)|
|`cd ..`| Move one directory up. ![cddotdot](https://github.com/AlphabetType/workshop-material/raw/master/Terminal%20Intro/Example%20Images/cddotdot.png)|
|`mkdir`| Creates a directory. ![mkdir](https://github.com/AlphabetType/workshop-material/raw/master/Terminal%20Intro/Example%20Images/mkdir.png)|
|`touch`| Creates a file. ![touch](https://github.com/AlphabetType/workshop-material/raw/master/Terminal%20Intro/Example%20Images/touch.png)|
|`ls -al`| Displays all files of current directory in a list view. ![ls](https://github.com/AlphabetType/workshop-material/raw/master/Terminal%20Intro/Example%20Images/ls.png)|
|`open .`| Opens the Finder windows on the current location.|
|`open`| Opens a file in it’s standard application. ![open](https://github.com/AlphabetType/workshop-material/raw/master/Terminal%20Intro/Example%20Images/open.png)|
|`mv`| Moves file; can also be used to rename file. ![mv](https://github.com/AlphabetType/workshop-material/raw/master/Terminal%20Intro/Example%20Images/mv.png)|
|`ditto`| Copy folder to another destination. ![ditto](https://github.com/AlphabetType/workshop-material/raw/master/Terminal%20Intro/Example%20Images/ditto.png)|

## Navigating the terminal

| Command | Description |
| --- | --- |
|`pwd`| Shows current path.|
|`ctrl`+`c`| Cancels current process.|
|`cmd`+ `k`| Clears terminal.|
|`history`| Shows last used commands.|
|`↑`| (Arrow up) Use last command; cycles through history.|
|`⇥`| (tab key) Completes filenames.|
|`alt`+ (click)| Move cursor to specific position in command.|


## Handy commands

| Command | Description |
| --- | --- |
|(some command) + `-h`| See the usage help of the command.|
|`base64`| Shows file as base64 string. Useful, when you want to embed a font in your css file. ![base64](https://github.com/AlphabetType/workshop-material/raw/master/Terminal%20Intro/Example%20Images/base64.png)|
|`sudo`| Authenticate yourself as superuser to gain extra priviliges to do stuff.|
|`defaults write com.apple.finder AppleShowAllFiles TRUE`| Shows hidden files in Finder. To make it work, you have to restart finder with `killall Finder`|
|`defaults write NSGlobalDomain AppleShowAllExtensions -bool true`| Shows file extensions in Finder. To make it work, you have to restart finder with `killall Finder`|
|`caffeinate`| Prevent your Mac from going to sleep. Use `cmd`+ `c` to go back to it’s normal sleeping schedule|

# Command Line

## Working with files and folders

| Command | Description |
| --- | --- |
|`cd`| Changes directory. You can drag the destination into the terminal windows instead of typing the path. ![cd](Example_Images/cd.png)|
|`cd ..`| Move one directory up. ![cddotdot](Example_Images/cddotdot.png)|
|`mkdir`| Creates a directory. ![mkdir](Example_Images/mkdir.png)|
|`touch`| Creates a file. ![touch](Example_Images/touch.png)|
|`ls -al`| Displays all files of current directory in a list view. ![ls](Example_Images/ls.png)|
|`open .`| Opens the Finder windows on the current location.|
|`open`| Opens a file in it’s standard application. ![open](Example_Images/open.png)|
|`cp`| Copy file to destination; can also be used to duplicate file ![cp](Example_Images/cp.png)|
|`mv`| Moves file; can also be used to rename file. ![mv](Example_Images/mv.png)|
|`ditto`| Copy folder to another destination. ![ditto](Example_Images/ditto.png)|
|`date`| Get the current date. You can add [formatting options](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior) as arguments. E.g. `+%Y-%m-%d_%H-%M` ![date](Example_Images/date.png)|

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
|`base64`| Shows file as base64 string. Useful, when you want to embed a font in your css file. ![base64](Example_Images/base64.png)|
|`sudo`| Authenticate yourself as superuser to gain extra priviliges to do stuff.|
|`defaults write com.apple.finder AppleShowAllFiles TRUE`| Shows hidden files in Finder. To make it work, you have to restart finder with `killall Finder`|
|`defaults write NSGlobalDomain AppleShowAllExtensions -bool true`| Shows file extensions in Finder. To make it work, you have to restart finder with `killall Finder`|
|`caffeinate`| Prevent your Mac from going to sleep. Use `cmd`+ `c` to go back to it’s normal sleeping schedule|

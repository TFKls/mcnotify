# mcnotify
## A notification daemon for minecraft servers

mcnotify is a simple python program designed to let you know a minecraft
server comes online and when someone joins it.

### Usage
```
usage: mcnotify.py [-h] [-q] [-p] [-d] [-r REFRESH] hostname

A minecraft notification daemon.

positional arguments:
  hostname              Hostname of the server.

optional arguments:
  -h, --help            show this help message and exit
  -q, --query           whether to use detailed server information. this only works if a server has enabled it in its properties.
  -p, --players         whether to take into account players leaving and joining. this works if query is enabled, and might work on small servers.
  -d, --daemon          whether to start mcnotify as a UNIX daemon using daemonify. if not specified, program starts in the foreground.
  -r REFRESH, --refresh REFRESH
                        interval of seconds to refresh and check for changes.
```

### License
	mcnotify
    Copyright (C) 2021 TFKls
	
	This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

	This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.

#!/usr/bin/env python3
import argparse
from time import sleep
from typing import *

from daemonize import Daemonize
from mcstatus import MinecraftServer
from pynotifier import Notification

def loop(args):
    server = MinecraftServer.lookup(args.hostname)
    notification_duration = min(10, int(args.refresh/2))
    try:
        if args.query:
            old = server.query()
        else:
            old = server.status()
    except:
        oldline = False
    else:
        oldline = True
    while True:
        sleep(args.refresh)
        try:
            if args.query:
                new = server.query()
            else:
                new = server.status()
        except:
            online = False
        else:
            online = True
        if oldline is not online:
            Notification(
                title=f'Server has {"started" if online else "stopped"}!',
                description=f'The server at {args.hostname} has been {"started" if online else "stopped"}.',
                duration=notification_duration,
	        urgency='normal'
                ).send()
        elif args.players and args.query:
            old_players = set(old.players.names)
            new_players = set(new.players.names)
            players_left = old_players - new_players
            players_join = new_players - old_players
            for player in players_join:
                Notification(
                    title=f'{player} has joined the server.',
                    description=f'{player} has joined the server at {args.hostname}.',
                    duration=notification_duration,
	            urgency='normal'
                ).send()
            for player in players_left:
                Notification(
                    title=f'{player} has left the server.',
                    description=f'{player} has left the server at {args.hostname}.',
                    duration=notification_duration,
	            urgency='normal'
                ).send()                
        elif args.players:
            old_players = old.players.sample
            new_players = new.players.sample
            if ((old_players is None and old.players.online > 0)
            or (new_players is None and new.players.online > 0)):
                old_players = old.players.online
                new_players = new.players.online
                if old_players is not new_players:
                    Notification(
                        title=f'Some people have {"left" if old_players > new_players else "joined"} the server.',
                        description=f'The server at {args.hostname} now has {new_players} players (had {old_players}).',
                        duration=notification_duration,
	                urgency='normal'
                    ).send()
            else:
                old_players = set(player.name for player in (old_players or []))
                new_players = set(player.name for player in (new_players or []))
                players_left = old_players - new_players
                players_join = new_players - old_players
                for player in players_join:
                    Notification(
                        title=f'{player} has joined the server.',
                        description=f'{player} has joined the server at {args.hostname}.',
                        duration=notification_duration,
	                urgency='normal'
                    ).send()
                for player in players_left:
                    Notification(
                        title=f'{player} has left the server.',
                        description=f'{player} has left the server at {args.hostname}.',
                        duration=notification_duration,
	                urgency='normal'
                    ).send()
                        
        old = new
        oldline = online

def main():
    parser = argparse.ArgumentParser(description='A minecraft notification daemon.')
    parser.add_argument('-q', '--query', dest='query', action='store_true',
                        help='whether to use detailed server information.\
                        this only works if a server has enabled it in its properties.')
    parser.add_argument('-p', '--players', dest='players', action='store_true',
                        help='whether to take into account players leaving and joining.\
                        this works if query is enabled, and might work on small servers.')
    parser.add_argument('-d', '--daemon', dest='daemon', action='store_true',
                        help='whether to start mcnotify as a UNIX daemon using daemonify.\
                        if not specified, program starts in the foreground.')
    parser.add_argument('hostname', type=str,
                        help='Hostname of the server.')
    parser.add_argument('-r', '--refresh', dest='refresh', type=int, default=120,
                        help='interval of seconds to refresh and check for changes.')
    args = parser.parse_args()
    if args.daemon:
        daemon = Daemonize(app='mcnotify', pid="/tmp/mcnotify.pid", action=lambda: loop(args))
        daemon.start()
    else:
        loop(args)

main()

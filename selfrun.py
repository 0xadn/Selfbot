
from curses.panel import bottom_panel
from email import message
from multiprocessing.connection import Client
from re import A
import discord
from discord.ext import commands, tasks
from discord.utils import get
import sys, os, threading
import time 
import csv
import asyncio
from selftoken import  token
input("""
███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗███╗   ███╗███████╗
██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝████╗ ████║██╔════╝
███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   ██╔████╔██║█████╗  
╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   ██║╚██╔╝██║██╔══╝  
███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   ██║ ╚═╝ ██║███████╗
╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   ╚═╝     ╚═╝╚══════╝  $me#0001""")
def require_install():
    os =input("qu'elle os utilise tu Windowns[1] Linux[2]")
    if os == "1":
        input("si tu utiliser windows lance le fichier start.bat pour install les librairie")
        input("si il ya des ereur c'est normal  le self se lancera sinon  cree un ticket sur le serv ")
        exec(open("./main.py").read())
    if os =="2":
        input("si tu utiliser linux lance le fichier start.sh pour install les librairie")
        input("si il ya des ereur c'est normal  le self se lancera sinon  cree un ticket sur le serv ")
        exec(open("./main.py").read())
require_install()
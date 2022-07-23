#libraries
import discord
from utils import *
from discord.ext import commands

#intents (used to detect member joins)
intents = discord.Intents.default()
intents.members = True

#client object
client = commands.Bot(command_prefix = 'z', case_insensitive = True, intents = intents, activity = discord.Game(name = 'with Alts'), status = discord.Status.idle)

#when the bot is ready to be used
@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

#when a member joins the server
@client.event
async def on_member_join(member):
    minimum_days = int(get_minimum_days())
    creation = member.created_at.date().day
    if creation < minimum_days:
        await member.send(f'{error_emoji} Your account is too new to join **{member.guild.name}**. Please wait `{minimum_days - creation}` more days before joining.')
        await member.kick(reason = f'Account is too new to join server.')
        try:  await client.get_channel(get_log_channel()).send(embed = discord.Embed(title = 'Member Kicked', description = f'{member.mention} was kicked for not meeting the minimum days requirement.\n\n**Creation** : `{creation}` days\n**Requirement** : `{minimum_days}` days', color = 0xffcccb))
        except:  pass
    else:
        try:  await client.get_channel(get_log_channel()).send(embed = discord.Embed(title = 'Member Joined', description = f'{member.mention} joined the server.\n **Creation** : `{creation}` days', color = 0xff0000))
        except:  pass

#a simple command which sends the bots latency
@client.slash_command(name = 'ping', description = 'returns the client latency', usage = 'ping')
async def ping(ctx):
    if not int(guild_id)== ctx.guild.id:
        guild = client.get_guild(int(guild_id))
        await ctx.respond(f'{error_emoji} This command is only available in the `{guild}` server.')
    await ctx.respond(f'Pong! **{round(client.latency * 1000)}**ms 🏓')

#set the minimum days required to be on the alt list
@client.slash_command(name = 'set-minimum-days', description = 'sets the minimum days required to be on the alt list', usage = 'set-minimum-days <days>')
async def minimum_days(ctx, days:float):
    if not int(guild_id)== ctx.guild.id:
        guild = client.get_guild(int(guild_id))
        await ctx.respond(f'{error_emoji} This command is only available in the `{guild}` server.')
    else:
        set_minimum_days(days)
        await ctx.respond(f'{success_emoji} Minimum days set to `{days}`.')

#set the log channel
@client.slash_command(name = 'set-log-channel', description = 'sets the log channel', usage = 'set-log-channel <channel>')
async def log_channel(ctx, channel:discord.TextChannel):
    if not int(guild_id)== ctx.guild.id:
        guild = client.get_guild(int(guild_id))
        await ctx.respond(f'{error_emoji} This command is only available in the `{guild}` server.')
    else:
        set_log_channel(channel.id)
        await ctx.respond(f'{success_emoji} Log channel set to `{channel}`.')

#logging in to the bot
client.run(token)
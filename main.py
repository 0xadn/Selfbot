from re import A
import discord
from discord.ext import commands, tasks
from discord.utils import get
import sys, os, threading
import time 
import csv
import asyncio
from selftoken import  token
client = commands.Bot(command_prefix=".", self_bot = True, help_command= None )
server_nb = len(client.guilds) 


print(f"""
███████╗███████╗██╗     ███████╗██████╗  ██████╗ ████████╗███╗   ███╗███████╗
██╔════╝██╔════╝██║     ██╔════╝██╔══██╗██╔═══██╗╚══██╔══╝████╗ ████║██╔════╝
███████╗█████╗  ██║     █████╗  ██████╔╝██║   ██║   ██║   ██╔████╔██║█████╗  
╚════██║██╔══╝  ██║     ██╔══╝  ██╔══██╗██║   ██║   ██║   ██║╚██╔╝██║██╔══╝  
███████║███████╗███████╗██║     ██████╔╝╚██████╔╝   ██║   ██║ ╚═╝ ██║███████╗
╚══════╝╚══════╝╚══════╝╚═╝     ╚═════╝  ╚═════╝    ╚═╝   ╚═╝     ╚═╝╚══════╝  0xadn#0016
https://discord.gg/toolsfr
userinfo \nserver :{server_nb} 
""")

@client.event
async def on_ready():
    os.system('cls')
    print(f"🟢 Ready to be used !")
    game = discord.Streaming(name=f"Selfbot toolsfr",
                             url='https://twitch.tv/abcdefg')
    await client.change_presence(status=discord.Status.dnd, activity=game)
@client.command()
async def cmd(ctx): 
    a = """```ini\n[ Self bot v1.0]\n.cmd \n.cmddb\n.cmdmd \n.cmduser\n.cmdraid``` """
    await  ctx.send(a)
    await ctx.message.delete()
@client.command()
async def cmddb(ctx):
    a = """```ini\n[ Self bot v1.0]\n.save [nom du registre] [texte] \n.find [nom du registre]```"""
    await ctx.send(a)
    await ctx.message.delete()
@client.command()
async def cmdmd(ctx):
    a =("""```ini\n[ Self bot v1.0]\n.clear [ amount ]\n.kick[user]\n.ban[user]\n.unban[user]\n.lock\n.unlock\n.leave\n.renew[channel]```""")
    await ctx.send(a)
    await ctx.message.delete()
@client.command()
async def cmdraid(ctx):
    a =("""```ini\n[ Self bot v2.0]\n.spam [ message ] \n.spameveryone [ message ]\n.raid[channel_name]\n.iraid[channel] [texte]\n.reset\n.dmall[message]\n.banall\n.kickall```""")
    await ctx.send(a)
    await ctx.message.delete()
@client.command()
async def cmdstatut(ctx):
    a =("```ini\n[ Self bot v2.0]\n.setstream[stream]```")
    await ctx.send(a)
@client.command()
async def cmduser(ctx):
    await ctx.send("```ini\n[ Self bot v1.0]\n.leave\n.server ```")
@client.command()
async def clear(ctx, nombre: int):
    message = await ctx.channel.history(limit=nombre + 1).flatten()
    for message in message:
        await message.delete()
    clearmsg = f"**clear** \n {nombre} message on bien été clear "
    await ctx.send(clearmsg)
@client.command()
async def setstream(ctx ,*,stream):
    await ctx.send(f"stream changer pour {stream}")
    game = discord.Streaming(name=f"{stream}",
                             url='https://twitch.tv/abcdefg')
    await client.change_presence(status=discord.Status.dnd, activity=game)
@client.command()
async def raid(ctx, channel_name):
    for channel in range(0,10):
        guild = ctx.guild
        channel = await guild.create_text_channel(channel_name)       
@client.command()
async def grabpp(self, ctx, *,  avamember : discord.Member=None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)
@client.command()
async def spam(ctx, *,spamtxt):
    for i in range(0,50):
        i = (f"{spamtxt}")
        await ctx.send(i)
@client.command()
async def spameveryone(ctx, *,spamtxt, nombre):
    for i in range(0,20):
        i = (f"{spamtxt} @everyone")
        await ctx.send(i)
@client.command()
async def save(ctx, registre, *,texte ): 
    with open('save.csv', mode='a') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow([registre, texte, ])
        print (len((texte)))
    await ctx.send("votre save a été sauvaugarder")
    await ctx.message.delete()
@client.command()
async def find(ctx ,*registre):
    print("donne")
    with open('save.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        print("donne")
        for row in csv_reader:
            
            if row[0] == registre:
                print("donne")
                await ctx.send(f"{row[0]} ,{row[1]}")
@client.command()
async def kick(ctx, user: discord.User, *reason):
    server = ctx.guild
    servern = server.name
    reason = "".join(reason)
    await ctx.guild.kick(user, reason=reason)
    a =(f"{user} a été kick")
    await ctx.send(a)
    await ctx.message.delete()
@client.command()
async def ban(ctx, user: discord.User, *reason):
    server = ctx.guild
    servern = server.name
    reason = "".join(reason)
    await ctx.guild.ban(user, reason=reason)
    a = (f"{user}  a bien été ban ")
    await ctx.send(a)
    await ctx.message.delete()
@client.command()
async def unban(ctx, user):
    userName, userId = user.split("#")
    bannedUsers = await ctx.guild.bans()
    for i in bannedUsers:
        if i.user.name == userName and i.user.discriminator == userId:
            await ctx.guild.unban(i.user)
            await ctx.send(f"{user} à été unban.")
            await ctx.message.delete()
            return
    await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")
    await ctx.message.delete()
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Command introuvable !")
        await ctx.message.delete()
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Il manque un argument.")
        await ctx.message.delete()
    elif isinstance(error, commands.MissingPermissions):
        await ctx.send(
            "tu n'a pas la permision de faire cette action")
        await ctx.message.delete()
    elif isinstance(error, commands.CheckFailure):
        await ctx.send("vous ne pouvez utilisez cette commande.")
        await ctx.message.delete()
    if isinstance(error.original, discord.Forbidden):
        await ctx.send(
            "je n'ai pas la permisions requis pour faire cette action")
        await ctx.message.delete()
@client.command()
async def lock(ctx, channel: discord.TextChannel = None):
    overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
    overwrite.send_messages = False
    await ctx.channel.set_permissions(ctx.guild.default_role,
                                      overwrite=overwrite)
    await ctx.send('channel lock')
    await ctx.message.delete()
@client.command()
async def unlock(ctx):
    await ctx.channel.set_permissions(ctx.guild.default_role,
                                      send_messages=True)
    await ctx.send(ctx.channel.mention + "channel unlock")
    await ctx.message.delete()
@client.command()
async def leave(ctx):
    server = ctx.guild
    servern = server.name
    await ctx.send(f"tu va leave le serv {servern}")
    time.sleep(5)

    await ctx.guild.leave()
@client.command()
async def renew(ctx, channel: discord.TextChannel = None):
    if channel == None:
        await ctx.send("channel introuvable")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="reset")
        await nuke_channel.delete()
        await new_channel.send(f"salon a été reset  ")
        await ctx.send("reset")

    else:
        await ctx.send(f"channel invalide {channel.name} ")
@client.command()
async def reset(ctx):
    for c in ctx.guild.channels:
        await c.delete()
@client.command()
async def iraid(ctx,channel_name, *,texte):
    for c in ctx.guild.channels:
        await c.delete()
        
    for channel in range(0,50):
        guild = ctx.guild
        channel = await guild.create_text_channel(channel_name) 
        for i in range(0,5):
            i = await channel.send(texte)
@client.command()
async def dmall(ctx,*,message):
    dm_message = message
    print("start")
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            if member.id == client.user.id:
                pass
            else:
                
                time.sleep(20)
                await member.send(dm_message)
                print(f"message envoyer {member}")
                
        except:
            print(f" je n'ai pas pu envoyer le message a {member}")
@client.command()
async def emojirdm(ctx):
    await ctx.send("""👌      🤤
                        🍆 💤 👔 🍆 
                              🛢️     👃
                              ⚡8==👊D 💦
                            🎺 🍆      💦""")
@client.command()
async def server(ctx):
    await ctx.send("tu est dans" + str(len(client.guilds))+ "serveur")
@client.command()
async def banall(ctx):
    for member in list(ctx.guild.members):
      try:
        await member.ban(reason="banall", delete_message_days=7)
        print(f"a été ban {member.display_name}!")
        print("ban all excuter avec succés")
      except Exception:
        pass
@client.command(pass_contxt=True)
async def kick_all(ctx):
    members = ctx.guild.members 
    members.remove(ctx.me)
    for member in members:
        try:
            if member.id != id or member.id != id: # the two ids inputed(don't want to share my id)
                await member.kick(reason="deleting server")
                print("kick ")
            else:
                print(f"Failed to kick {member}.")
        except discord.Forbidden: # forbidden error is the error that gets returned when the bot is forbidden to do something(in this case kick itself)
            print(f"Failed to kick {member}.")
        continue

#____________________logsselfbot_______________________________________________________________
@client.event
async def on_guild_join(ctx):
    servern = ctx.name
    print(f"""
             ╔══════════════════════════════════════════════════╗
             
                     tu a rejoin le serveur {servern}                 
             
             ╚══════════════════════════════════════════════════╝""")
@client.event
async def on_guild_remove(ctx):
    servern = ctx.name
    print(f"""
             ╔══════════════════════════════════════════════════╗
             
                    tu a quitter le serveur {servern}                
             
             ╚══════════════════════════════════════════════════╝""")
@client.event
async def on_invite_create(invite, ctx):
    servern = ctx.name
    print(f"""
             ╔══════════════════════════════════════════════════╗
             
                 tu a crée une invite pour le serv {servern}                
             
             ╚══════════════════════════════════════════════════╝""")
@client.event
async def on_relationship_update(before, after):
    rbefore = before
    rafter = after
    print(f"""
             ╔══════════════════════════════════════════════════╗
             
                ton amitier a été mis a jour 
                {rbefore} -> {rafter}
             
             ╚══════════════════════════════════════════════════╝""")      
client.run(token)

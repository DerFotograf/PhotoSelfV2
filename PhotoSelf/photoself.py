purple_dark= 0x6a006a
purple_medium= 0xa958a5
purple_light= 0xc481fb
orange= 0xffa500
gold= 0xdaa520
red_dark= 8e2430
red_light= 0xf94343
blue_dark= 0x3b5998
cyan= 0x5780cd
blue_light= 0xace9e7
aqua= 0x33a1ee
pink= 0xff9dbb
green_dark= 0x2ac075
green_light= 0xa1ee33
white= 0xf9f9f6
cream= 0xffdab9



import discord
from discord.ext import commands
from datetime import *
from colorama import *
import colorama
import json
import threading
from tkinter import messagebox
import tkinter
root = tkinter.Tk()
root.withdraw()
from discord.ext import tasks
import psutil
import asyncio
import time
import os
import sys
from pyfiglet import Figlet
import time
import requests
import random
from discord.ext.commands import CommandNotFound
colorama.init()



async def get_pre(bot, message):
    with open("config.json") as f:
        pprefix = json.load(f)
        prefix = pprefix["prefix"]
    return prefix


last = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
bot = commands.Bot(command_prefix=get_pre, self_bot=True)
bot.remove_command('help')
init()

@bot.event
async def on_command(ctx): 
    with open("config.json") as f:
        da = json.load(f)
        if da['delete_after_execute'] == "yes":
            await ctx.message.delete()
        elif da['delete_after_execute'] == "no":
            pass
        else:
            input("Introduce un valor a 'delete_after_execute' en config.json (El valor debe ser sí o no)")
            os._exit(0)
"""@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return"""
def show_on():
    os.system("cls")
    print(f'{Fore.MAGENTA}<#------------[Selfbot remixed by Fotograf.]#------------>')
    with open("config.json") as m:
        get_prefix = json.load(m)["prefix"]
    print()
    os.system(f'title Loggeado como: {bot.user.name} / Remixed By Fotograf.')
    print(f"{Fore.RED}>> {Fore.YELLOW}Fotogrąf.#0001")
    print(f"{Fore.RED}>> {Fore.YELLOW}Nickname: {Fore.GREEN}{bot.user.name}")
    print(f"{Fore.RED}>> {Fore.YELLOW}ID: {Fore.GREEN}{bot.user.id}")
    print(f"{Fore.RED}>> {Fore.YELLOW}Prefix: {Fore.GREEN}{get_prefix}")
    print(f"{Fore.RED}>> {Fore.YELLOW}Último loggeo: {Fore.GREEN}{last}")
    print()
@bot.event
async def on_ready():
    show_on()
    
afk_stat = 0

@bot.event
async def on_message(message):
    global afk_stat
    await bot.process_commands(message)
    if afk_stat == 1:
        with open("config.json") as m:
            mesaje = json.load(m)["afk_message"]
            if mesaje == "":
                mesaje = "`¡Esto es un mensaje auto-respondido! El usuario ahora está AFK.`"
                
        if message.guild is None:
            if message.author == bot.user:
                return
            await message.channel.send(mesaje)

@bot.command()
async def precio(ctx, curen: str=None):
    if curen is None:
        await ctx.send(f">> Especifica una divisa disponible\nDivisas disponibles: `Ethereum (eth), Bitcoin (btc), Litecoin (ltc), Monero (xmr)`"); await ctx.send("Revisa el comando.");return
    elif curen.lower() == "btc" or curen.lower() == "bitcoin":
        try:
            with requests.session() as ses:
                resp = ses.get('https://blockchain.info/ticker')
                pret = resp.json()['USD']['last']
                pret1 = resp.json()['EUR']['last']
                pret2 = resp.json()['GBP']['last']
                try:
                    embed= discord.Embed(color= orange, title="Precio Bitcoin", description=f"Te muestra el precio del Bitcoin.",timestamp=datetime.utcfromtimestamp(time.time()))
                    embed.add_field(name="El precio actual es:", value=f"${pret}\n€{pret1}\n£{pret2}", inline=True)
                    embed.set_thumbnail(url="https://i.imgur.com/GCPDIYU.png")
                    embed.set_footer(text=" Remixed By Fotograf.")
                    await ctx.send(embed=embed)
                except discord.HTTPException:
                    await ctx.send(f"- **__Precio Bitcoin:__** -\n\n- ${pret}\n- €{pret1}\n- £{pret2}")
        except Exception as e: await ctx.send(f"Error: {e}")

    elif curen.lower() == "eth" or curen.lower() == "ethereum":
        try:
            with requests.session() as ses:
                resp = ses.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP')
                pret = resp.json()['USD']
                pret1 = resp.json()['EUR']
                pret2 = resp.json()['GBP']
                try:
                    embed= discord.Embed(color= purple_medium, title="Precio Ethereum", description=f"Te muestra el precio del Ethereum.",timestamp=datetime.utcfromtimestamp(time.time()))
                    embed.add_field(name="El precio actual es:", value=f"${pret}\n€{pret1}\n£{pret2}", inline=True)
                    embed.set_thumbnail(url="https://i.imgur.com/Huyedhz.png")
                    embed.set_footer(text=" Remixed By Fotograf.")
                    await ctx.send(embed=embed)
                except discord.HTTPException:
                    await ctx.send(f"- **__Precio Ethereum:__** -\n\n- ${pret}\n- €{pret1}\n- £{pret2}")
        except Exception as e: await ctx.send(f"Error: {e}")
    elif curen.lower() == "ltc" or curen.lower() == "litecoin":
        try:
            with requests.session() as ses:
                resp = ses.get('https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,EUR,GBP')
                pret = resp.json()['USD']
                pret1 = resp.json()['EUR']
                pret2 = resp.json()['GBP']
                try:
                    embed= discord.Embed(color= blue_dark, title="Precio Litecoin", description=f"Te muestra el precio del Litecoin.",timestamp=datetime.utcfromtimestamp(time.time()))
                    embed.add_field(name="El precio actual es:", value=f"${pret}\n€{pret1}\n£{pret2}", inline=True)
                    embed.set_thumbnail(url="https://i.imgur.com/Hn4zLbc.png")
                    embed.set_footer(text=" Remixed By Fotograf.")
                    await ctx.send(embed=embed)
                except discord.HTTPException:
                    await ctx.send(f"- **__Precio Litecoin:__** -\n\n- ${pret}\n- €{pret1}\n- £{pret2}")
        except Exception as e: await ctx.send(f"Error: {e}")
    elif curen.lower() == "xmr" or curen.lower() == "monero":
        try:
            with requests.session() as ses:
                resp = ses.get('https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR,GBP')
                pret = resp.json()['USD']
                pret1 = resp.json()['EUR']
                pret2 = resp.json()['GBP']
                try:
                    embed= discord.Embed(color= orange, title="Precio Monero", description=f"Te muestra el precio del Monero.",timestamp=datetime.utcfromtimestamp(time.time()))
                    embed.add_field(name="El precio actual es:", value=f"${pret}\n€{pret1}\n£{pret2}", inline=True)
                    embed.set_thumbnail(url="https://i.imgur.com/nIjEKrN.png")
                    embed.set_footer(text=" Remixed By Fotograf.")
                    await ctx.send(embed=embed)
                except discord.HTTPException:
                    await ctx.send(f"- **__Precio Monero:__** -\n\n- ${pret}\n- €{pret1}\n- £{pret2}")
        except Exception as e: await ctx.send(f"Error: {e}")
    else:
        await ctx.send("`Divisa inválida...`")
@bot.command()
async def coinflip(ctx):
    lista = ['cara', 'cruz']
    coin = random.choice(lista)
    try:
        if coin == 'cara':
            embed= discord.Embed(color= orange, title="Cara",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://webstockreview.net/images/coin-clipart-dime-6.png")
            embed.set_footer(text=" Remixed By Fotograf.")
            await ctx.send(embed=embed)
        else:
            embed= discord.Embed(color= orange, title="Cruz",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://www.nicepng.com/png/full/146-1464848_quarter-tail-png-tails-on-a-coin.png")
            embed.set_footer(text=" Remixed By Fotograf.")
            await ctx.send(embed=embed)
    except discord.HTTPException:
        if coin == 'cara':
            await ctx.send("**Al lanzar la moneda salió:** `Cara`")
        else:
            await ctx.send("**Al lanzar la moneda salió:** `Cruz`")
@bot.command()
async def ipinfo(ctx, ip: str=None):
    if ip is None: await ctx.send("`Por favor, especifica una IP válida.`");return
    else:
        try:
            with requests.session() as ses:
                resp = ses.get(f'https://ipinfo.io/{ip}/json')
                if "Wrong ip" in resp.text:
                    await ctx.send("`Dirección IP inválida.`")
                    return
                else:
                    try:
                        j = resp.json()
                        embed= discord.Embed(color= blue_light, title=f"INFO",timestamp=datetime.utcfromtimestamp(time.time()))
                        embed.add_field(name=f'IP', value=f'{ip}', inline=True)
                        embed.add_field(name=f'Ciudad', value=f'{j["city"]}', inline=True)
                        embed.add_field(name=f'Región', value=f'{j["region"]}', inline=True)
                        embed.add_field(name=f'País', value=f'{j["country"]}', inline=True)
                        embed.add_field(name=f'Coordinadas', value=f'{j["loc"]}', inline=True)
                        embed.add_field(name=f'Postal', value=f'{j["postal"]}', inline=True)
                        embed.add_field(name=f'Timezone', value=f'{j["timezone"]}', inline=True)
                        embed.add_field(name=f'Organización', value=f'{j["org"]}', inline=True)
                        embed.set_footer(text=" Remixed By Fotograf.")
                        await ctx.send(embed=embed)
                    except discord.HTTPException:
                        await ctx.send(f'**__{ip} Info__**\n\n- **Ciudad:** `{j["city"]}`\n\n- **Región:** `{j["region"]}`\n\n- **País:** `{j["country"]}`\n\n- **Coordinadas:** `{j["loc"]}`\n\n- **Postal:** `{j["postal"]}`\n\n- **Timezone:** `{j["timezone"]}`\n\n- **Organización:** `{j["org"]}`')
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def ping(ctx):
    try:
        embed= discord.Embed(color= green_light, title=f"Pong",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_footer(text=" Remixed By Fotograf.")
        before = time.monotonic()
        message = await ctx.send(embed=embed)
        await asyncio.sleep(1)
        ping = (time.monotonic() - before) * 1000
        embed= discord.Embed(color= green_light, title=f"Ping: {int(ping)}ms",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_footer(text=" Remixed By Fotograf.")
        await message.edit(embed=embed)

    except discord.HTTPException:
        before = time.monotonic()
        message = await ctx.send("Pong!")
        ping = (time.monotonic() - before) * 1000
        await message.edit(content=f"Ping: `{int(ping)}ms`")
@bot.command()
async def ascii(ctx, *,text: str=None):
    if text is None:
        await ctx.send("`Argumento inválido...`")
    else:
        f = Figlet(font='Slant')
        j = (f.renderText(text))
        try:
            embed= discord.Embed(color= aqua, description=f"```{j}```",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_footer(text=" Remixed By Fotograf.")
            await ctx.send(embed=embed)
        except discord.HTTPException:
            try:
                await ctx.send(f"```{j}```")
            except Exception as e:
                await ctx.send(f"Error: {e}")
            
def is_me(m):
    return m.author == bot.user
@bot.command()
async def purge(ctx, amount:int=None):
    try:
        if amount is None:
            await ctx.send("`Cantidad inválida...`")
        else:
            deleted = await ctx.channel.purge(limit=amount, before=ctx.message, check=is_me)
            asd = await ctx.send('`Eliminado(s) {} mensaje(s)`'.format(len(deleted)))
            await asyncio.sleep(3)
            await asd.delete()
    except:
        try:
            await asyncio.sleep(1)
            c = 0
            async for message in ctx.message.channel.history(limit=amount):
                if message.author == bot.user:
                    c += 1
                    await message.delete()
                else:
                    pass
            asd = await ctx.send('`Eliminado(s) {} mensajes(s)`'.format((c)))
            await asyncio.sleep(3)
            await asd.delete()
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def playing(ctx, *,status: str=None):
    if status is None:
        await ctx.send(f"`Argumento inválido.`")
    else:
        try:
            game = discord.Activity(type=0, name=f"{status}")
            await bot.change_presence(activity=game)
            await ctx.send(f"Estado cambiado a: `Playing {status}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def streaming(ctx, *,status: str=None):
    if status is None:
        await ctx.send(f"`Argumento inválido.`")
    else:
        try:
            game = discord.Activity(type=1, name=f"{status}", url="https://www.twitch.tv/nexitarp")
            await bot.change_presence(activity=game)
            await ctx.send(f"Estado cambiado a: `Streaming {status}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def listening(ctx, *,status: str=None):
    if status is None:
        await ctx.send(f"`Argumento inválido.`")
    else:
        try:
            game = discord.Activity(type=2, name=f"{status}")
            await bot.change_presence(activity=game)
            await ctx.send(f"Estado cambiado a: `Listening {status}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def watching(ctx, *,status: str=None):
    if status is None:
        await ctx.send(f"`Argumento inválido.`")
    else:
        try:
            game = discord.Activity(type=3, name=f"{status}")
            await bot.change_presence(activity=game)
            await ctx.send(f"Estado cambiado a: `Watching {status}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def nostatus(ctx):

    try:
        game = discord.Activity(type=-1)
        await bot.change_presence(activity=game)
        await ctx.send(f"`Estado eliminado.`")
    except Exception as e:
        await ctx.send(f"Error: {e}")
@bot.command()
async def nickname(ctx, *, name: str=None):
    if name is None:
        await ctx.send(f"Uso: {ctx.prefix}renombrar <nuevo nombre>")
    elif len(name) < 1:
        await ctx.send("`El nombre debe de tener un caracter al menos.`")
    else:
        try:
            await ctx.author.edit(nick=name)
            await ctx.send(f"Nickname cambiado a: `{name}`")
        except Exception as e:
            await ctx.send(f"Error: {e}")
@bot.command()
async def serverimg(ctx):
    try:
        embed= discord.Embed(color= aqua, description=f"[Server Icon]({ctx.guild.icon_url})",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_image(url=ctx.guild.icon_url)
        embed.set_footer(text=" Remixed By Fotograf.")
        await ctx.send(embed=embed)
    except discord.HTTPException:    
        await ctx.send(f"{ctx.guild.icon_url}")
    except:
        await ctx.send(f"`Debes estar dentro de un server. Para el avatar de un usuario usa {ctx.prefix}pfp <usuario>`")
@bot.command()
async def pfp(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send(f"Uso: {ctx.prefix}pfp <usuario>")
    else:
        try:
            embed= discord.Embed(color= purple_dark, description=f"[PFP de {user.name}]({user.avatar_url})",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_image(url=user.avatar_url)
            embed.set_footer(text=" Remixed By Fotograf.")
            await ctx.send(embed=embed)
        except discord.HTTPException:    
            await ctx.send(f"{user.avatar_url}")
        except Exception as e:
            await ctx.send(f"Eror: {e}")
                
@bot.command()
async def nonickname(ctx):
    try:
        name = "‎‎‎‎‎‎‎‏‏‎ ឵឵ ឵឵ ឵឵ ឵឵‎"
        await ctx.author.edit(nick=name)
        await ctx.send(f"`Ahora tu nickname es invisible.`")
    except Exception as e:
        await ctx.send(f"Error: {e}")
@bot.command()
async def nickmolesto(ctx):

    try:
        name = "𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫𒐫" 
        await ctx.author.edit(nick=name)
        await ctx.send(f"`Nickname cambiado a basura que jode a los users.`")
    except Exception as e:
        await ctx.send(f"Error: {e}")
@bot.command()
async def help(ctx):
    try:
        embed= discord.Embed(color= pink, title="  Comandos",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.add_field(name="Información", value="help, ipinfo, ping", inline=False)
        embed.add_field(name="Estado", value="playing, streaming, watching, listening, nostatus", inline=False)
        embed.add_field(name="Diversión", value="coinflip, spam, junk, haxor, dox, nickname, nonickname, nickmolesto, serverimg, pfp", inline=False)
        embed.add_field(name="Economía", value="precio, btctousd, usdtobtc", inline=False)
        embed.add_field(name="Moderación", value="purge, shutdown, ban, kick, unban, nuke", inline=False)
        embed.add_field(name="Otros", value="ascii, shrug, embed", inline=False)
        embed.set_footer(text=" Remixed By Fotograf.")
        await ctx.send(embed=embed)
    except:
        await ctx.send("`Error, este canal tiene los links embedidos desactivados, comprueba tu consola.`")
        os.system("cls")
        print("""
        Comandos

        Información:
        - help
        - ipinfo
        - ping

        Estado:
        - playing
        - streaming
        - watching
        - listening
        - nostatus

        Diversión:
        - coinflip
        - spam
        - junk
        - haxor
        - dox
        - nickname
        - nonickname
        - nickmolesto
        - serverimg
        - pfp

        Economía:
        - precio
        - usdtobtc
        - btctousd

        Moderación:
        - purge
        - shutdown
        - ban
        - kick
        - unban
        - nuke


        Otros:
        - ascii
        - shrug
        - embed
        - afk

        Presiona enter para regresar al menú inicial...
        """)
        input()
        show_on()
strbtc = 0


@bot.command()
async def usdtobtc(ctx, num:int=None):
    if num is None:
        await ctx.send("`Formato inválido.`")
    else:
        with requests.session() as ses:
            resp = ses.get('https://blockchain.info/ticker')
            pret = int(resp.json()['USD']['last'])
            final = num/pret
            try:
                embed= discord.Embed(color= orange, title="USD ⟹ BTC", description=f"- USD: {num}\n\n- BTC: {final}",timestamp=datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url="https://i.imgur.com/GCPDIYU.png")
                embed.set_footer(text=" Remixed By Fotograf.")
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"`USD ⟹ BTC:`\n\n- **USD:** `{num}`\n\n- **BTC:** `{final}`")
@bot.command()
async def btctousd(ctx, num:int=None):
    if num is None:
        await ctx.send("`Formato inválido.`")
    else:
        with requests.session() as ses:
            resp = ses.get('https://blockchain.info/ticker')
            pret = int(resp.json()['USD']['last'])
            final = num*pret
            try:
                embed= discord.Embed(color= orange, title="BTC ⟹ USD", description=f"- BTC: {num}\n\n- USD: {final}",timestamp=datetime.utcfromtimestamp(time.time()))
                embed.set_thumbnail(url="https://i.imgur.com/HHSzzNz.png")
                embed.set_footer(text=" Remixed By Fotograf.")
                await ctx.send(embed=embed)
            except discord.HTTPException:
                await ctx.send(f"`BTC ⟹ USD:`\n\n- **BTC:** `{num}`\n\n- **USD:** `{final}`")

@bot.command()
async def afk(ctx):
    global afk_stat
    if afk_stat == 0:
        afk_stat += 1
        await ctx.send("Modo AFK: `ON`")
            
    elif afk_stat == 1:
        afk_stat -= 1
        await ctx.send("Modo AFK: `OFF`")

@bot.command()
@commands.has_permissions(ban_members=True)
async def unban(ctx, user: discord.Member=None):
    if user is None:
        await ctx.send("`¿A quién quieres desbanear? Especifica su ID.`")
        return
    else:pass
    try:
        user1 = await bot.fetch_user(user)
        await ctx.guild.unban(user1)
        await ctx.send(f"`El usuario {user.mention}({user.id}) ha sido desbaneado.`")
    except Exception as e:
        await ctx.send(f"Error: {e}")
@unban.error
async def unban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        
        await ctx.send(f"Error: {error}")
@bot.command()
async def shutdown(ctx):
    def check(m):
            return m.author == ctx.author and m.content == "yes" or m.content == "y"
    await ctx.send("‎‏‏‎`Tienes 10 segundos para especificar 'y' or 'yes' para apagar el selfbot o el comando será ignorado.`")
    try:
        m = await bot.wait_for('message', timeout=10.0, check=check)
    except asyncio.TimeoutError:
        await ctx.send("`Comando ignorado.`")
            
    else:
        os._exit(0)
@bot.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, user: discord.Member=None, *, reason: str=None):
    if user is None:
        await ctx.send("`¿A quién quieres banear? Por favor, menciona a un usuario.`")
        return
    elif user == ctx.author:
        await ctx.send("`Buen intento, pero no puedes banearte a ti mismo.`")
        return
    else:pass
    try:
        await user.ban(reason=reason)
        await ctx.send(f"`El usuario {user.mention}({user.id}) ha sido baneado por la razón {reason}`")
    except Exception as e:
        await ctx.send(f"{e}")
@ban.error
async def ban_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        
        await ctx.send(f"Error: {error}")
@bot.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, user: discord.Member=None, *, reason: str=None):
    if user is None:
        await ctx.send("`¿A quién quieres kickear? Por favor, menciona a un usuario.`")
        return
    elif user == ctx.author:
        await ctx.send("`Buen intento, pero no puedes kickearte a ti mismo.`")
        return
    else:pass
    try:
        await user.ban(reason=reason)
        await ctx.send(f"`El usuario {user.mention}({user.id}) ha sido kickeado por la razón {reason}`")
    except Exception as e:
        await ctx.send(f"{e}")
@kick.error
async def kick_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        
        await ctx.send(f"Error: {error}")
@bot.command()
async def shrug(ctx):
    await ctx.send("¯\_(ツ)_/¯")
@bot.command()
async def spam(ctx, amount:int=None, *, message: str=None):
    try:
        if amount is None or message is None:
            await ctx.send(f"Uso: {ctx.prefix}spam <cantidad> <mensaje>")
        else:
            for each in range (0, amount):
                await ctx.send(f"{message}")
    except Exception as e:
        await ctx.send(f"Error: {e}")
@bot.command()
async def junk(ctx):
    for each in range(0, 11):
        d = "\n"*100
        await ctx.send(f".{d}.")
@bot.command()
async def haxor(ctx, *, message: str=None):
    
    if message is None:
        await ctx.send("`Inserte su mensaje.`")
    else:
        try:
            word = message
            leetmsg = word
            leetwords = "aeioutsyou"
            for letter in word:
                if letter in leetwords:
                    leetmsg = leetmsg.replace('a', str(4))
                    leetmsg = leetmsg.replace('e', str(3))
                    leetmsg = leetmsg.replace('i', str(1))
                    leetmsg = leetmsg.replace('o', str(0))
                    leetmsg = leetmsg.replace('t', str(7))
                    leetmsg = leetmsg.replace('s', '$')
                    leetmsg = leetmsg.replace('you', 'j00')

            embed= discord.Embed(color= green_dark, title="1337 Haxor", description=f"{leetmsg.upper()}",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/TR2cv3C.jpg")
            embed.set_footer(text=" Remixed By Fotograf.")
            await ctx.send(embed=embed)
        except discord.HTTPException:
            word = message
            leetmsg = word
            leetwords = "aeioutsyou"
            for letter in word:
                if letter in leetwords:
                    leetmsg = leetmsg.replace('a', str(4))
                    leetmsg = leetmsg.replace('e', str(3))
                    leetmsg = leetmsg.replace('i', str(1))
                    leetmsg = leetmsg.replace('o', str(0))
                    leetmsg = leetmsg.replace('t', str(7))
                    leetmsg = leetmsg.replace('s', '$')
                    leetmsg = leetmsg.replace('you', 'j00')
            await ctx.send(f"{leetmsg.upper()}")
@bot.command()
async def dox(ctx, user: discord.Member=None):
    emaillist = random.choice(["gmx.de", "yahoo.com", "protonmail.com", "gmail.com", "hotmail.com"])
    nr = random.choice(range(0,9999))
    ip = random.choice(["127.0.0.1", "192.168.0.1", "192.168.0.101"])
    country = random.choice(['Estados Unidos', 'Venezuela', "España", "Colombia", "Chile", "Ecuador"])
    if user is None:
        await ctx.send("`Por favor, menciona a un usuario.`")
    else:
        try:
            embed= discord.Embed(color= green_dark, title=f"`Doxeo en progreso (%0)`",description="`Recopilando dirección de email...`",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text=" Remixed By Fotograf.")
            a = await ctx.send(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color= green_dark, title=f"`Doxeo en progreso (%50)`",description="`Recopilando su dirección IP...`",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text=" Remixed By Fotograf.")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color= green_dark, title=f"`Doxeo en progreso (%100)`",description="`Añadiendo al doxbin...`",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.set_footer(text=" Remixed By Fotograf.")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
            embed= discord.Embed(color= green_dark, title=f"`Dox de {user.name}`",timestamp=datetime.utcfromtimestamp(time.time()))
            embed.set_thumbnail(url="https://i.imgur.com/ZkFcOw6.gif")
            embed.add_field(name=f'**__Email:__**', value=f'`{user.name}{nr}@{emaillist}`', inline=False)
            embed.add_field(name=f'**__IP:__**', value=f'`{ip}`', inline=False)
            embed.add_field(name=f'**__País:__**', value=f'`{country}`', inline=False)
            embed.set_footer(text=" Remixed By Fotograf.")
            await a.edit(embed=embed)
            await asyncio.sleep(2)
        except discord.HTTPException:
            a = await ctx.send("`Doxeo en progreso (%0) - Recopilando dirección de email...`")
            await asyncio.sleep(2)
            await a.edit(content="`Doxeo en progreso (%50) - Recopilando su dirección IP...`")
            await asyncio.sleep(2)
            await a.edit(content="`Doxeo en progreso (%100) - Añadiendo al doxbin...`")
            await asyncio.sleep(2)
            await a.edit(content=f"`Dox de {user.name}`:\n\n**__Email:__** `{user.name}{nr}@{emaillist}`\n**__IP:__** `{ip}`\n**__País:__** `{country}`")



@dox.error
async def dox_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        
        await ctx.send(f"Error: {error}")
@bot.command()
async def embed(ctx,*,text: str=None):
    if text is None:
        await ctx.send("`Añada su texto...`")
    else:
        embed= discord.Embed(color= orange,description=f"{text}",timestamp=datetime.utcfromtimestamp(time.time()))
        embed.set_footer(text=" Remixed By Fotograf.")
        try:
            await ctx.send(embed=embed)
        except discord.HTTPException:
            await ctx.send(f"`Error, este canal tiene los enlaces embedidos desactivados.`")
def start():
    try:
        os.system("title Connecting to discord servers")
        print("\n>> Conectando con los servidores de discord...")

        with open("config.json") as f:
            token = json.load(f)
            bot.run(token["token"], bot=False)
    except Exception as e:
        print(f"\n>> Ha habido un fallo, por favor, compruebe el error...\n>> Error: {e}")
        input()
threading.Thread(target=start, args=()).start()

@bot.command()
async def nuke(ctx, channel: discord.TextChannel = None):
    if channel == None: 
        await ctx.send("No mencionaste un canal...")
        return

    nuke_channel = discord.utils.get(ctx.guild.channels, name=channel.name)

    if nuke_channel is not None:
        new_channel = await nuke_channel.clone(reason="He clonado al anterior. (Nukeado)")
        await nuke_channel.delete()
        await new_channel.send("`Canal nukeado correctamente.`")
        await ctx.send("`La limpieza se ejecutó con éxito.`")

    else:
        await ctx.send(f"El canal {channel.name} no encontrado...")

@nuke.error
async def nuke_error(ctx, error):
    if isinstance(error, commands.CheckFailure):
        
        await ctx.send(f"Error: {error}")
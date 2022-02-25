# Code écrit par Luckyluka17
# Version 1.0.0
# Merci de laisser ce texte si vous réutilisez ce code

# Librairies à installer :
# pycord, requests, asyncio


import json
import os
import random
import time
import asyncio

import discord
import requests
from discord.ext import commands
from discord.ui import Button, View
from requests import Session

session = Session()

os.system('clear')
token = "VOTRE TOKEN ICI"
pfc = ['pierre', 'feuille', 'ciseaux']

prefix = "/"
version = "1.0.0"

r = requests.head(url="https://discord.com/api/v1")
try:
    print(f"Rate limit : {round(int(r.headers['retry-After']) / 60)} minutes restantes")
except:
    print("Pas de rate limit")

    bot = discord.Bot()

    start = int(time.time())

    @bot.event
    async def on_ready():
        print("Bot disponible")
        activity = discord.Game(name="TheGamesBox - Joue sur Discord")
        await bot.change_presence(status=discord.Status.online, activity=activity)

    @bot.slash_command(name="help", description="Affiche l'aide concernant le bot")
    async def help(ctx):
        bouclier = bot.get_emoji(946118391859662848)
        site = bot.get_emoji(946118675981828166)
        github = bot.get_emoji(946118675944050728)
        embed=discord.Embed(title="TheGamesBox - Le bot de jeux 100% français", description=f"TheGamesBox est un bot discord pour jouer à différents mini-jeux gratuitement. Pour l'instant, il est en développement mais s'améliorera au fur et à mesure.\nMon préfixe est `{prefix}` !")
        embed.set_thumbnail(url="https://zupimages.net/up/22/08/kyi6.png")
        embed.set_image(url="https://zupimages.net/up/22/08/k50l.png")
        embed.add_field(name="🎮 Jeux", value=f"`{prefix}chifoumi`: Lance une partie de pierre, feuille, ciseaux contre le bot\n`{prefix}crystalball`: Répond à ta question\n`{prefix}speedtest`: Faites un test de rapidité", inline=True)
        embed.add_field(name="⚙️ Utilitaires", value=f"`{prefix}support`: Affiche l'invitation vers le support\n`{prefix}botinfo`: Affiche les différentes infos sur le bot", inline=True)
        embed.set_footer(text=f"Créé par Luckyluka17 - v{version}")
        bouton1 = Button(label="Github", url="https://github.com/", emoji=github)
        bouton2 = Button(label="Site", url="https://www.luckyluka17.tk", emoji=site)
        bouton3 = Button(label="Ajoute moi", url="https://discord.com/oauth2/authorize?client_id=946075376977858672&permissions=397821733888&scope=applications.commands%20bot", emoji="➕")
        view = View()
        view.add_item(bouton1)
        view.add_item(bouton2)
        view.add_item(bouton3)
        await ctx.respond(embed=embed, view=view)

    @bot.slash_command(name="support", description="Affiche le lien du serveur discord")
    async def support(ctx):
        await ctx.respond("Voici le lien vers le serveur de support :\nhttps://discord.gg/RTZ7Wkzu2n")

    @bot.slash_command(name="botinfo", description="Affiche les informations du bot")
    async def botinfo(ctx):
        latence = round(bot.latency * 1000 )
        embed=discord.Embed(title="Informations sur le bot")
        embed.set_thumbnail(url="https://zupimages.net/up/22/08/kyi6.png")
        embed.add_field(name="🏓 Ping", value=f"{latence} ms", inline=False)
        embed.add_field(name="💻 Développeur", value="Luckyluka 17#5801", inline=False)
        embed.add_field(name="⚙️ Version actuelle", value=f"`{version}`", inline=False)
        embed.add_field(name="🎮 Jeux disponibles", value="3 (stables)", inline=False)
        embed.set_footer(text="Créé par Luckyluka17")
        await ctx.respond(embed=embed)

    @bot.slash_command(name="crystalball", description="Jouer à crystalball")
    async def crystalball(ctx,*,question):
        var1 = random.randint(1, 5)
        réponse = ""
        if var1 == 1:
            réponse = "oui"
        elif var1 == 2:
            réponse = "non"
        elif var1 == 3:
            réponse = "Probablement"
        elif var1 == 4:
            réponse = "Probablement pas"
        elif var1 == 5:
            réponse = "Bien sûr !"
        await ctx.respond(f"🔮 Une réponse apparait dans la boule de crystal !\nElle vous dit **{réponse}**.")

    @bot.slash_command(name="chifoumi", description="Jouer à pierre, feuille, ciseaux")
    async def chifoumi(ctx):
        embed=discord.Embed(title="Pierre, feuille, ciseaux", description="Vous êtes prêt à jouer ? Cliquez sur votre choix ci dessous grâce aux boutons !")
        embed.set_thumbnail(url="https://i.pinimg.com/originals/02/dc/4e/02dc4e134c94e3f243f0eaefd00dfb53.gif")
        embed.set_footer(text="Créé par Luckyluka 17")
        bouton1 = Button(label="Pierre", emoji="🪨")
        bouton2 = Button(label="Feuille", emoji="🍃")
        bouton3 = Button(label="Ciseaux", emoji="✂️")

        async def pierre(interaction):
            pfc1 = random.choice(pfc)
            if str(pfc1) == "pierre":
                embed=discord.Embed(title="Pierre, feuille, ciseaux", description="Égalité ! Le bot a choisi pierre et vous aussi !")
                embed.set_thumbnail(url="https://i.pinimg.com/originals/02/dc/4e/02dc4e134c94e3f243f0eaefd00dfb53.gif")
                embed.set_footer(text="Créé par Luckyluka 17")
            elif str(pfc1) == "ciseaux":
                embed=discord.Embed(title="Pierre, feuille, ciseaux", description="Gagné ! Le bot a choisi ciseaux et vous pierre !")
                embed.set_thumbnail(url="https://i.pinimg.com/originals/02/dc/4e/02dc4e134c94e3f243f0eaefd00dfb53.gif")
                embed.set_footer(text="Créé par Luckyluka 17")
            else:
                embed=discord.Embed(title="Pierre, feuille, ciseaux", description="Perdu ! Le bot a choisi feuille et vous pierre !")
                embed.set_thumbnail(url="https://i.pinimg.com/originals/02/dc/4e/02dc4e134c94e3f243f0eaefd00dfb53.gif")
                embed.set_footer(text="Créé par Luckyluka 17")
            await interaction.response.send_message(embed=embed, view=None, ephemeral=True)

        async def ciseaux(interaction):
            pfc1 = random.choice(pfc)
            if str(pfc1) == "pierre":
                embed=discord.Embed(title="Pierre, feuille, ciseaux", description="Perdu ! Le bot a choisi pierre et vous ciseaux !")
                embed.set_thumbnail(url="https://i.pinimg.com/originals/02/dc/4e/02dc4e134c94e3f243f0eaefd00dfb53.gif")
                embed.set_footer(text="Créé par Luckyluka 17")
            elif str(pfc1) == "ciseaux":
                embed=discord.Embed(title="Pierre, feuille, ciseaux", description="Égalité ! Le bot a choisi ciseaux et vous aussi !")
                embed.set_thumbnail(url="https://i.pinimg.com/originals/02/dc/4e/02dc4e134c94e3f243f0eaefd00dfb53.gif")
                embed.set_footer(text="Créé par Luckyluka 17")
            else:
                embed=discord.Embed(title="Pierre, feuille, ciseaux", description="Gagné ! Le bot a choisi feuille et vous ciseaux !")
                embed.set_thumbnail(url="https://i.pinimg.com/originals/02/dc/4e/02dc4e134c94e3f243f0eaefd00dfb53.gif")
                embed.set_footer(text="Créé par Luckyluka 17")
            await interaction.response.send_message(embed=embed, view=None, ephemeral=True)

        async def feuille(interaction):
            pfc1 = random.choice(pfc)
            if str(pfc1) == "pierre":
                embed=discord.Embed(title="Pierre, feuille, ciseaux", description="Gagné ! Le bot a choisi pierre et vous feuille !")
                embed.set_thumbnail(url="https://i.pinimg.com/originals/02/dc/4e/02dc4e134c94e3f243f0eaefd00dfb53.gif")
                embed.set_footer(text="Créé par Luckyluka 17")
            elif str(pfc1) == "ciseaux":
                embed=discord.Embed(title="Pierre, feuille, ciseaux", description="Perdu ! Le bot a choisi ciseaux et vous feuille !")
                embed.set_thumbnail(url="https://i.pinimg.com/originals/02/dc/4e/02dc4e134c94e3f243f0eaefd00dfb53.gif")
                embed.set_footer(text="Créé par Luckyluka 17")
            else:
                embed=discord.Embed(title="Pierre, feuille, ciseaux", description="Égalité ! Le bot a choisi feuille et vous aussi !")
                embed.set_thumbnail(url="https://i.pinimg.com/originals/02/dc/4e/02dc4e134c94e3f243f0eaefd00dfb53.gif")
                embed.set_footer(text="Créé par Luckyluka 17")
            await interaction.response.send_message(embed=embed, view=None, ephemeral=True)

        bouton1.callback = pierre
        bouton2.callback = feuille
        bouton3.callback = ciseaux
        view = View()
        view.add_item(bouton1)
        view.add_item(bouton2)
        view.add_item(bouton3)
        await ctx.respond(embed=embed, view=view)

    @bot.slash_command(name="speedtest", description="Jouer à test de rapidité")
    async def speedtest(ctx):
        embed=discord.Embed(title="Test de rapidité", description="Vous êtes prêt à jouer ? Cliquez au bon moment sur le bouton !")
        embed.set_thumbnail(url="https://c.tenor.com/VWfNGYPgYUYAAAAC/eyes-lurking.gif")
        embed.set_footer(text="Créé par Luckyluka 17")

        async def clickedst(interaction):
            await interaction.response.edit_message(embed=None, view=None, content=f"Tu as cliqué en `--` !")

        async def start(interaction):
            embed=discord.Embed(title="Test de rapidité", description="Attention...")
            embed.set_thumbnail(url="https://c.tenor.com/VWfNGYPgYUYAAAAC/eyes-lurking.gif")
            embed.set_footer(text="Créé par Luckyluka 17")
            await interaction.response.send_message(embed=embed, view=None, ephemeral=True)
            await asyncio.sleep(random.randint(1, 5))
            embed=discord.Embed(title="Test de rapidité", description="CLIQUE")
            embed.set_thumbnail(url="https://c.tenor.com/VWfNGYPgYUYAAAAC/eyes-lurking.gif")
            embed.set_footer(text="Créé par Luckyluka 17")
            bouton1 = Button(label="Clique moi !", style=discord.ButtonStyle.danger)
            bouton1.callback = clickedst
            view = View()
            view.add_item(bouton1)
            await interaction.followup.send(embed=embed, view=view, ephemeral=True)

        
        bouton1 = Button(label="Démarrer le jeu", emoji="👀")
        bouton1.callback = start
        view = View()
        view.add_item(bouton1)
        await ctx.respond(embed=embed, view=view)

    @bot.slash_command(name="say", description="Répète ce que tu lui dit")
    async def say(ctx,*,message):
        await ctx.respond(content=message)


        

    bot.run(token)
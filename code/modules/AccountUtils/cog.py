#!/bin/python3
#--------------------------------------------------------------------
# Module: Account Utils
# Purpose: Various commands for users to see their data.
# Author: Dylan Sperrer (p0t4t0sandwich|ThePotatoKing)
# Date: 18NOVEMBER2022
# Updated: <date> <author>
#--------------------------------------------------------------------

import discord
from discord.ext import commands

import bot_library as b

class AccountUtils(commands.Cog):
    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.hybrid_command()
    async def bal(self, ctx: commands.Context) -> None:
        """To access the user's balance of special currency."""

        # Init variables
        channel = ctx.guild.name
        author = str(ctx.author)
        content = ctx.message.content

        # Init variables
        description, status = b.bal("discord", author)

        # Response logic
        if status == 200:
            title = "Balance:"
            color = 0x65bf65
        else:
            title = "Error:"
            color = 0xbf0f0f

        # Log the data
        self.bot.log(channel, author, content)
        self.bot.log(channel, self.bot.user, description)

        # Send Discord Embed object
        statement = discord.Embed(title = title, description = description, color = color)
        await ctx.reply(embed=statement)

    @commands.hybrid_command()
    async def playtime(self, ctx: commands.Context) -> None:
        """Access the user's playtime statistics."""

        # Init variables
        channel = ctx.guild.name
        author = str(ctx.author)
        content = ctx.message.content

        description, status = b.playtime("discord", author)

        # Response logic
        if status == 200:
            title = "Playtime:"
            color = 0x65bf65
        else:
            title = "Error:"
            color = 0xbf0f0f

        # Log the data
        self.bot.log(channel, author, content)
        self.bot.log(channel, self.bot.user, description)

        # Send Discord Embed object
        statement = discord.Embed(title = title, description = description, color = color)
        await ctx.reply(embed=statement)

    @commands.hybrid_command()
    async def ip(self, ctx: commands.Context) -> None:
        """Make the minecraft server info readily available."""

        # Init variables
        channel = ctx.guild.name
        author = str(ctx.author)
        content = ctx.message.content

        description = "For Java:\nIP: mc.basmc.ca\nFor Bedrock:\nIP: mc.basmc.ca\nPort: 19132"
        
        # Log the data
        self.bot.log(channel, author, content)
        self.bot.log(channel, self.bot.user, description)

        # Send Discord Embed object
        statement = discord.Embed(title = "The BAS Network:", description = description, color = 0x877f23)
        statement.set_image(url = "https://api.mcsrvstat.us/icon/mc.basmc.ca")
        await ctx.reply(embed=statement)

async def setup(bot: commands.bot) -> None:
    await bot.add_cog(AccountUtils(bot))
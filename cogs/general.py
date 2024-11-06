import disnake
from disnake.ext import commands

class General(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.command(name="ping")
    async def ping(ctx):
        await ctx.send("Pong! 🏓")

    @commands.slash_command(name="hello", description="Say hello to the bot!")
    async def hello(self, inter: disnake.ApplicationCommandInteraction):
        await inter.response.send_message("Hello! 👋")

    @commands.slash_command(name="echo", description="Echoes back your message.")
    async def echo(self, inter: disnake.ApplicationCommandInteraction, message: str):
        await inter.response.send_message(f"You said: {message}")

def setup(bot):
    bot.add_cog(General(bot))

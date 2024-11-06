import disnake
from disnake.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="kick", description="Kick a user from the server.")
    @commands.has_permissions(kick_members=True)
    async def kick(self, inter: disnake.ApplicationCommandInteraction, member: disnake.Member, reason: str = "No reason provided"):
        await member.kick(reason=reason)
        await inter.response.send_message(f"{member.name} has been kicked for {reason}.")

def setup(bot):
    bot.add_cog(Admin(bot))

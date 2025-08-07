from discord.ext import commands

class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # !join, !leave, !play vb. komutlar burada eklenecek

def setup(bot):
    bot.add_cog(Music(bot))

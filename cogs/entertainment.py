from discord.ext import commands
import random

class Entertainment(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='ping')
    async def ping(self, ctx):
        """Botun gecikmesini gösterir."""
        latency = round(self.bot.latency * 1000)
        await ctx.send(f'Pong! {latency}ms')

    @commands.command(name='coin')
    async def coin_flip(self, ctx):
        """Yazı-tura atar."""
        result = random.choice(['Yazı', 'Tura'])
        await ctx.send(result)

def setup(bot):
    bot.add_cog(Entertainment(bot))

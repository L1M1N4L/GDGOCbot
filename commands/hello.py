from discord.ext import commands

class Hello(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def hello(self, ctx):
        await ctx.send('Hello!')

def setup(bot):
    bot.add_cog(Hello(bot))

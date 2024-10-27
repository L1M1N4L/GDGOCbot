from discord.ext import commands
import discord

class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        # Replace 'TARGET_USER_ID' with the actual User ID
        target_user_id = 512996440486969345

        try:
            # Fetch the user object using the user ID
            user = await self.bot.fetch_user(target_user_id)
            
            # Send a direct message to the user
            await user.send("Ping!")
            await ctx.send("Ping sent to the user via direct message.")
        except discord.NotFound:
            await ctx.send("User not found.")
        except discord.Forbidden:
            await ctx.send("Unable to send direct message: Bot lacks permissions or user has blocked messages.")

def setup(bot):
    bot.add_cog(Ping(bot))

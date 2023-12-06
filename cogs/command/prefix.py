from core import Cog_Base

from discord.ext import commands


class Prefix(Cog_Base):
    
    @commands.command()
    async def adam(self, ctx: commands.Context):
        await ctx.message.delete()
        await ctx.send("adam")
        return


def setup(bot):
    bot.add_cog(Prefix(bot))
from core import Cog_Base
import discord

class Basic(Cog_Base):
    

    @discord.slash_command(name="ping", description="Ping the bot.")
    async def ping(self, ctx):
        await ctx.respond(f"延遲:{round(self.bot.latency*1000)} ms", ephemeral=True)

def setup(bot):
    bot.add_cog(Basic(bot))
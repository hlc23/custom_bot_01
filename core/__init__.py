import os
import discord
from discord.ext.commands.errors import CommandNotFound
from discord.ext.commands import Bot
from discord.ext.commands.context import Context

class CustomBot(Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.remove_command('help')

        # load cogs
        for path, subdirs, files in os.walk('cogs'):
            for name in files:
                if name.endswith('.py'):
                    print("Loading cog: " + name[:-3])
                    try:
                        self.load_extension(f'{path.replace("/", ".")}.{name[:-3]}')
                    
                    except Exception as e:
                        print(f'Failed to load extension {name[:-3]}.')
                        print(e)
                        continue
                    finally:
                        print(f'Loaded extension {name[:-3]}.')


    async def on_ready(self):
        print('Logged in as {0.user}'.format(self))
        return

    async def on_command_error(self, context: Context, exception) -> None:
        if isinstance(exception, CommandNotFound):
            return
        return await super().on_command_error(context, exception)

    def run(self, token):
        super().run(token)

class Cog_Base(discord.Cog):
    def __init__(self, bot: CustomBot) -> None:
        super().__init__()
        self.bot = bot

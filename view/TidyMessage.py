import asyncio
import discord
from model import st
from model.enums import TidyMode


class TidyMessage:
    """Class designed to handle keeping long chains of commands clean."""

    def __init__(self, **kwargs):
        self.ctx = kwargs.get("ctx")
        self.mode = kwargs.get("mode")
        self.message = kwargs.get("message")
        self.embed = kwargs.get("embed")

    @staticmethod
    async def build(ctx, content, **kwargs):
        """Make a new TidyMessage
            id:         Is the ID for a message that already exists
            ctx:        Is the context within which this TM was made
            content:    Is the content to be put into the embed
            mode:       Is the TidyMode to use to grab default values for the Embed"""
        # Make the TM instance.
        tm = TidyMessage(mode=kwargs.get("mode"), ctx=ctx)

        # Ascertain if we're making a TM out of an existing or new Message
        if kwargs.get("id"):
            tm.message = tm.ctx.get_message(kwargs.get("id"))
            return await tm.rebuild(ctx.message, content)
        elif ctx:
            return await tm.rebuild(ctx.message, content)
        else:
            return print("TidyError: Insufficient information to generate TidyMessage; "
                         "context must be discord.ext.commands.context.Context type.")

    async def rebuild(self, prompt, content, **kwargs):
        """Modifies an existing TidyMessage
            id:         Is the ID for a message that already exists
            prompt:     Is the message or reaction which invoked this TM
            content:    Is the content to be put into the embed
            mode:       Is the TidyMode to use to grab default values for the Embed"""

        # Initialize the new TidyMessage as a copy of the current one.
        tm = TidyMessage(mode=self.mode, ctx=self.ctx, message=self.message, embed=self.embed)

        # Edit mode if any change.
        if kwargs.get("mode"):
            tm.mode = kwargs.get("mode")

        # Prepare the embed.
        if isinstance(content, discord.Embed):
            tm.embed = content
        elif isinstance(content, str):
            tm.embed = await tm._convert(prompt, content, tm.mode)
        else:
            return await tm.rebuild(prompt, st.ERR_INVALID_CONTENT, mode=TidyMode.WARNING)

        # If we hit an error, end immediately.
        if isinstance(tm.embed, TidyMessage):
            return tm.embed

        # Send or edit the message.
        if isinstance(tm.message, discord.Message):
            await tm.message.edit(embed=tm.embed)
        else:
            tm.message = await tm.ctx.channel.send(embed=tm.embed)

        # SUSPENDED FOR SKULLYBOT
        # # Delete the user command.
        # try:
        #     await prompt.delete()
        # except discord.errors.NotFound:
        #     pass  # If it's not there to be deleted we already did our job.

        return tm

    async def _convert(self, prompt, content, mode):
        """Generate an Embed based on the mode given."""

        if mode == TidyMode.STANDARD:
            std = discord.Embed(title="\n",
                                description=content,
                                color=0xF2D40F)
            std.set_thumbnail(url="https://image.ibb.co/fvgnxw/chrome_2017_12_02_01_44_59.png")
            std.set_author(name=self.ctx.bot.user.name,
                           url="https://www.pivotaltracker.com/n/projects/2133511",
                           icon_url="https://image.ibb.co/nhRWPb/chrome_2017_12_05_22_29_14.png")
            return std
        elif mode == TidyMode.WARNING:
            err = discord.Embed(title="\n",
                                description=content,
                                color=0xc10000)
            err.set_thumbnail(url="https://image.ibb.co/fvgnxw/chrome_2017_12_02_01_44_59.png")
            err.set_author(name=self.ctx.bot.user.name,
                           url="https://www.pivotaltracker.com/n/projects/2133511",
                           icon_url="https://image.ibb.co/nhRWPb/chrome_2017_12_05_22_29_14.png")
            return err
        return await TidyMessage.rebuild(prompt, st.ERR_INVALID_TIDYMODE, mode=TidyMode.WARNING)

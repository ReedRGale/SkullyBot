import discord

from model import val, util, st
from view.TidyMessage import TidyMessage
from model.enums import TidyMode

# Init #


# Overwrite 'help.'
val.bot.remove_command("help")


@val.bot.command(name="help", help=st.HP_HELP, brief=st.HP_BRIEF)
async def help_command(ctx, *args):
    """Command to simplify referencing the help documents."""
    if not val.calling.get(ctx.message.author.id):
        if args and len(args) == 1:  # If they want help with a specific command...
            try:
                await TidyMessage.build(ctx, val.bot.get_command(args[0]).help, mode=TidyMode.STANDARD)
            except discord.ext.commands.errors.CommandInvokeError:
                await TidyMessage.build(ctx, st.ERR_EDIT_WHAT, mode=TidyMode.WARNING)
        elif args:
            await TidyMessage.build(ctx, st.ERR_EXTRA_ARGS.format("one"), mode=TidyMode.STANDARD)
        else:  # Otherwise print out all command briefs.
            # Prepare the string.
            help_string = "Available Commands: \n\n"
            available_commands = val.bot.all_commands
            for name in available_commands:
                help_string += "**" + name + "**" + ":  " + available_commands[name].brief + "\n\n"
            await TidyMessage.build(ctx, help_string, mode=TidyMode.STANDARD)
        val.calling[ctx.message.author.id] = False


@val.bot.event
async def on_command(ctx):
    # Record anyone calling a command.
    if ctx.message.author.id not in val.calling:
        val.calling[ctx.message.author.id] = True


@val.bot.event
async def on_ready():
    print('Logged in as')
    print(val.bot.user.name)
    print(val.bot.user.id)
    print('------')


@val.bot.command(name="newitem", help=st.NI_HELP, brief=st.NI_BRIEF)
async def new_item(ctx):
    """Makes a new canon, including folders and player prefs."""
    if not val.calling.get(ctx.message.author.id):
        await util.new_item(ctx, ctx.message)
        val.calling[ctx.message.author.id] = False


@val.bot.command(name="voteitem", help=st.VI_HELP, brief=st.VI_BRIEF)
async def vote_item(ctx, *args):
    """Makes a new canon, including folders and player prefs."""
    if not val.calling.get(ctx.message.author.id):
        await util.vote_item(ctx, " ".join(args))
        val.calling[ctx.message.author.id] = False


@val.bot.command(name="items", help=st.IS_HELP, brief=st.IS_BRIEF)
async def items(ctx, *args):
    if not val.calling.get(ctx.message.author.id):
        if args:
            await util.get_item(ctx, " ".join(args))
        else:
            await util.get_items(ctx)
        val.calling[ctx.message.author.id] = False


@val.bot.command(name="edititem", help=st.EI_HELP, brief=st.EI_BRIEF)
async def edit_item(ctx, *args):
    if not val.calling.get(ctx.message.author.id):
        if not args:
            await TidyMessage.build(ctx, st.ERR_EDIT_WHAT, mode=TidyMode.WARNING)
        else:
            await util.edit_item(ctx, " ".join(args))
        val.calling[ctx.message.author.id] = False


@val.bot.command(name="deleteitem", help=st.DI_HELP, brief=st.DI_BRIEF)
async def delete_item(ctx, *args):
    if not val.calling.get(ctx.message.author.id):
        if not args:
            await TidyMessage.build(ctx, st.ERR_DELETE_WHAT, mode=TidyMode.WARNING)
        else:
            await util.delete_item(ctx, " ".join(args))
        val.calling[ctx.message.author.id] = False


@val.bot.command(name="newrecipe", help=st.NR_HELP, brief=st.NR_BRIEF)
async def new_recipe(ctx):
    """Makes a new canon, including folders and player prefs."""
    if not val.calling.get(ctx.message.author.id):
        await util.new_recipe(ctx, ctx.message)
        val.calling[ctx.message.author.id] = False


@val.bot.command(name="voterecipe", help=st.VR_HELP, brief=st.VR_BRIEF)
async def vote_recipe(ctx, *args):
    """Makes a new canon, including folders and player prefs."""
    if not val.calling.get(ctx.message.author.id):
        await util.vote_recipe(ctx, " ".join(args))
        val.calling[ctx.message.author.id] = False


@val.bot.command(name="recipes", help=st.RS_HELP, brief=st.RS_BRIEF)
async def recipes(ctx, *args):
    if not val.calling.get(ctx.message.author.id):
        if args:
            await util.get_recipe(ctx, " ".join(args))
        else:
            await util.get_recipes(ctx)
        val.calling[ctx.message.author.id] = False


@val.bot.command(name="editrecipe", help=st.ER_HELP, brief=st.ER_BRIEF)
async def edit_recipe(ctx, *args):
    if not val.calling.get(ctx.message.author.id):
        if not args:
            await TidyMessage.build(ctx, st.ERR_EDIT_WHAT, mode=TidyMode.WARNING)
        else:
            await util.edit_recipe(ctx, " ".join(args))
        val.calling[ctx.message.author.id] = False


@val.bot.command(name="delete recipe", help=st.DR_HELP, brief=st.DR_BRIEF)
async def delete_recipe(ctx, *args):
    if not val.calling.get(ctx.message.author.id):
        if not args:
            await TidyMessage.build(ctx, st.ERR_DELETE_WHAT, mode=TidyMode.WARNING)
        else:
            await util.delete_recipe(ctx, " ".join(args))
        val.calling[ctx.message.author.id] = False


# Code #


# Run the script.
val.bot.run(util.get_app_token())

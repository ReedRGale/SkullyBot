import shlex
from pprint import pprint

from discord.ext.commands import Group, Command
from model import val, util, st
from view.TidyMessage import TidyMessage
from model.enums import TidyMode
from model.TimeoutBool import TimeoutBool


# Decorators


def call_command(command):
    """Decorator that takes a command, updates the bot's guild state and wraps it in checks.
    If it fails any of the checks, it'll route it to the proper exit."""
    async def call(*args):
        # Retrieve context and args.
        ctx = args[0]
        args = tuple(shlex.split(ctx.message.content)[2:])

        # Check if a command has already been called by this user.
        if not val.calling.get(ctx.message.author.id) or \
           not val.calling.get(ctx.message.author.id).state():
            # Lock command functionality.
            val.calling[ctx.message.author.id] = TimeoutBool.start(val.FUCKING_NOVEL)

            # Call command.
            await command(ctx, *args) if args else await command(ctx)

            # Unlock command functionality.
            val.calling[ctx.message.author.id] = False
    return call


# Init #


@val.bot.event
async def on_ready():
    print('Logged in as')
    print(val.bot.user.name)
    print(val.bot.user.id)
    print('------')

    # Prepare the TidyMessage metadata.
    TidyMessage.set_t_imgs(TidyMode.STANDARD.value, val.T_URLS_STANDARD)
    TidyMessage.set_t_imgs(TidyMode.WARNING.value, val.T_URLS_WARNING)
    TidyMessage.set_t_imgs(TidyMode.PROMPT.value, val.p_avatar)

    TidyMessage.set_a_imgs(TidyMode.STANDARD.value, val.A_URLS_STANDARD)
    TidyMessage.set_a_imgs(TidyMode.WARNING.value, val.A_URLS_WARNING)
    TidyMessage.set_a_imgs(TidyMode.PROMPT.value, val.p_avatar)

    TidyMessage.set_color(TidyMode.STANDARD.value, 0xF2D40F)
    TidyMessage.set_color(TidyMode.WARNING.value, 0xc99e3a)
    TidyMessage.set_color(TidyMode.PROMPT.value, val.p_color)

    TidyMessage.set_timeout_m(st.TIMEOUT)
    TidyMessage.set_esc_m(st.ESCAPE)
    TidyMessage.set_url(val.GITHUB_URL)


# Commands


# Overwrite 'help.'
val.bot.remove_command("help")


@val.bot.command(name="help", help=st.HELP_HELP, brief=st.HELP_BRIEF)
@call_command
async def help_command(ctx, *args):
    """Command to simplify referencing the help documents."""
    if args:
        await specific_help(ctx, *args)
    else:
        await general_help(ctx)


async def specific_help(ctx, *args):
    arg = 0  # The argument we're evaluating at the moment.
    command = val.bot.all_commands.get(args[arg])  # The current level of command we're on.
    done = lambda x: x >= len(args)

    # Iterate over all args and determine correct help string to give.
    while not done(arg):
        arg += 1
        if isinstance(command, Group) and not done(arg):
            command = command.get_command(args[arg])
        elif isinstance(command, Group) and done(arg):
            help_string = st.INF_COMMAND_GROUP
            for child in command.commands:
                if isinstance(child, Group):
                    help_string += st.itlc(st.INF_GROUP) + " " \
                                   + st.bold(child.name) + ":  " + child.brief + "\n\n"
                else:
                    help_string += st.itlc(st.INF_COMMAND) + " " \
                                   + st.bold(child.name) + ":  " + child.brief + "\n\n"
            await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                    content=help_string, mode=TidyMode.STANDARD)
        elif isinstance(command, Command) and not done(arg):
            await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                    content=st.ERR_NO_SUCH_CHILD.format(args[arg - 1], args[arg]),
                                    mode=TidyMode.WARNING)
        elif isinstance(command, Command) and done(arg):
            await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                    content=st.INF_HELP.format(command.name, command.help),
                                    mode=TidyMode.STANDARD)
        elif not done(arg):
            await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                    content=st.ERR_NO_SUCH_TYPE.format(args[arg - 1], args[arg]),
                                    mode=TidyMode.WARNING)
        elif done(arg):
            await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                    content=st.ERR_NO_SUCH_CHILD.format(args[arg - 2], args[arg - 1]),
                                    mode=TidyMode.WARNING)


async def general_help(ctx):
    help_string = st.INF_TOP_LEVEL_COMMANDS
    for name in val.bot.all_commands:
        if isinstance(val.bot.all_commands[name], Group):
            help_string += st.itlc(st.INF_GROUP) + "  " \
                           + st.bold(name) + ":  " + val.bot.all_commands[name].brief + "\n\n"
        else:
            help_string += st.itlc(st.INF_COMMAND) + "  " \
                           + st.bold(name) + ":  " + val.bot.all_commands[name].brief + "\n\n"
    await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, content=help_string,
                            req=False, mode=TidyMode.STANDARD)


@val.bot.group(name="add", help=st.ADD_HELP, brief=st.ADD_BRIEF)
async def add(ctx):
    if ctx.invoked_subcommand is None:
        await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                content=st.ERR_ADD_WHAT, mode=TidyMode.WARNING)


@add.command(name="item", help=st.ADDITEM_HELP, brief=st.ADDITEM_BRIEF)
@call_command
async def add_item(ctx, *args):
    await util.add_item(ctx)


@add.command(name="souls", help=st.ADDSOUL_HELP, brief=st.ADDSOUL_BRIEF)
@call_command
async def add_item(ctx, *args):
    await util.add_soul(ctx, *args)


@val.bot.command(name="vote", help=st.VE_HELP, brief=st.VE_BRIEF)
@call_command
async def vote(ctx, *args):
    if args:
        await util.vote_item(ctx, " ".join(args))
    else:
        await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                content=st.ERR_VOTE_WHAT, mode=TidyMode.WARNING)


@val.bot.command(name="items", help=st.ITEMS_HELP, brief=st.ITEMS_BRIEF)
@call_command
async def items(ctx, *args):
    if args:
        await util.get_item(ctx, " ".join(args))
    else:
        await util.get_items(ctx)


@val.bot.group(name="edit", help=st.EDIT_HELP, brief=st.EDIT_BRIEF)
async def edit(ctx):
    if ctx.invoked_subcommand is None:
        await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                content=st.ERR_EDIT_WHAT, mode=TidyMode.WARNING)


@edit.command(name="item", help=st.ET_HELP, brief=st.ET_BRIEF)
@call_command
async def edit_item(ctx, *args):
    await util.edit_item(ctx, " ".join(args[1:]))


@val.bot.group(name="delete", help=st.DELETE_HELP, brief=st.DELETE_BRIEF)
async def delete(ctx):
    if ctx.invoked_subcommand is None:
        await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                content=st.ERR_DELETE_WHAT, mode=TidyMode.WARNING)


@delete.command(name="item", help=st.DE_HELP, brief=st.DE_BRIEF)
@call_command
async def delete_item(ctx, *args):
    await util.delete_item(ctx, " ".join(args))


# Code #


# Run the script.
val.bot.run(util.get_app_token())

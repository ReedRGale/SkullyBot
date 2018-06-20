# ----------- Script by ReedRGale ----------- #
# Utility functions used throughout the script. #


import asyncio
import json
import os
import errno

from model import val, st, alias
from view.TidyMessage import TidyMessage
from model.enums import TidyMode


# Function Encapsulators #


async def add_item(ctx, being_edited=""):
    """Encapsulator that handles making new items."""
    preview, unacceptable, first_run = None, True, True
    tm = await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, content=st.REQ_TITLE,
                                 checks=[check_unique(being_edited)], timeout=val.MEDIUM)
    if comm_ended(tm, ctx):
        return
    title = tm.prompt.content

    # Loop until acceptable.
    while unacceptable:

        # Ask for item title.
        if not first_run:
            tm = await tm.rebuild(st.REQ_TITLE, checks=[check_unique(being_edited)])
            if comm_ended(tm, ctx):
                return
            title = tm.prompt.content
        else:
            first_run = False

        # Ask for item contents.
        tm = await tm.rebuild(st.REQ_DESCRIPTION)
        if comm_ended(tm, ctx):
            return
        description = tm.prompt.content

        # Preview for user.
        preview = "\n\n" + "_" + title + "\n\n" + description + "_" + "\n\n"

        # Check if acceptable.
        tm = await tm.rebuild(st.ASK_ITEM_ACCEPTABLE + preview, checks=[check_alias_f(alias.CONFIRM_ALIASES),
                                                                        check_args_f(st.MODE_EQ, 1)])
        if comm_ended(tm, ctx):
            return
        fin = tm.prompt.content

        if fin.lower() in alias.AFFIRM:
            unacceptable = False

    # Prepare item entry.
    item_json = {st.F_TITLE: title,
                 st.F_ITEM: description,
                 st.F_OWNER: ctx.message.author.id,
                 st.F_VOTERS: [],
                 st.F_COMP: {},
                 st.F_ATTR: {},
                 st.F_CANON: False,
                 st.F_PROOFED: False}

    # Add item entry.
    store_item(item_json)

    await tm.rebuild(st.INF_ITEM_ADDED.format(title), req=False)


async def get_items(ctx):
    """Function designed to get all items and print them in a TidyMessage."""
    # Define the path.
    items_dir = "model\\" \
                + st.ITEMS_FN

    # Load in file.
    i_names, i_json = os.listdir(items_dir), {}
    for i in i_names:
        with open(items_dir + "\\" + i, "r") as fout:
            i_json[i] = json.load(fout)

    # Prepare fields.
    all_names, names, votes = "Here are all the items I have in my inventory! \n\n", list(), list()

    for key in i_names:
        names.append("~ **" + i_json[key][st.F_TITLE] + '**\n' +
                     "> Votes: " + str(len(i_json[key][st.F_VOTERS])) + '\n')
        votes.append(len(i_json[key][st.F_VOTERS]))

    # Sort names by vote.
    for _ in range(len(names)):
        for i in range(len(names)):
            if i != 0 and votes[i] > votes[i - 1]:
                bubble = votes[i]
                votes[i] = votes[i - 1]
                votes[i - 1] = bubble

                bubble = names[i]
                names[i] = names[i - 1]
                names[i - 1] = bubble

    # Concatenate all names.
    for i in range(len(names)):
        all_names += names[i]

    # Print in a tidy message.
    await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                            content=all_names, mode=TidyMode.STANDARD)


async def get_item(ctx, item):
    """Function designed to get an item and print it in a TidyMessage."""
    if not used_title(item):
        return await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                       content=st.ERR_ITEM_NONEXIST, mode=TidyMode.WARNING)

    await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                            content=st.item_entry(ctx, get_item_json(item)), mode=TidyMode.STANDARD)


async def edit_item(ctx, item):
    """Function to edit an existing item."""
    # Make sure the item exists.
    if not used_title(item):
        return await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                       content=st.ERR_ITEM_NONEXIST, mode=TidyMode.WARNING)

    # Check to make sure the editor is the creator
    if ctx.message.author.id != get_item_json(item)[st.F_OWNER]:
        return await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                       content=st.ERR_NOT_YOURS, mode=TidyMode.WARNING)

    # Check to make sure they're okay losing votes.
    tm = await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, content=st.ASK_VOTELOSS_ACCEPTABLE,
                                 checks=[check_alias_f(alias.CONFIRM_ALIASES),
                                         check_args_f(st.MODE_EQ, 1)], mode=TidyMode.STANDARD)
    if comm_ended(tm, ctx):
        return
    if tm.prompt.content.lower() in alias.DENY:
        return await tm.rebuild(ctx, st.INF_EXIT_EDIT, req=False, mode=TidyMode.STANDARD)

    # Define the path.
    items_dir = "model\\" \
                + st.ITEMS_FN

    # Record number of files in items before making a new one.
    i_names = os.listdir(items_dir)

    # Make the new item entry.
    await add_item(ctx, item)

    # If more files now, that means the old file wasn't overwritten, so delete it.
    if len(os.listdir(items_dir)) > len(i_names):
        os.remove(items_dir + "\\" + item + ".json")


async def delete_item(ctx, item):
    """Function to delete an existing item."""
    # Make sure the item exists.
    if not used_title(item):
        return await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                       content=st.ERR_ITEM_NONEXIST, mode=TidyMode.WARNING)

    # Check to make sure the editor is the creator
    if ctx.message.author.id != get_item_json(item)[st.F_OWNER]:
        return await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                       content=st.ERR_NOT_YOURS, mode=TidyMode.WARNING)

    # Check to make sure they're sure about deleting this.
    unchecked, conf, prompt = True, None, ctx.message

    tm = await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, content=st.ASK_DELETE_ACCEPTABLE,
                                 checks=[check_alias_f(alias.CONFIRM_ALIASES),
                                         check_args_f(st.MODE_EQ, 1)], mode=TidyMode.STANDARD)
    if comm_ended(tm, ctx):
        return
    if conf.content.lower() in alias.DENY:
        return await TidyMessage.build(ctx, st.INF_EXIT_DELETE, mode=TidyMode.STANDARD)

    # Delete item entry.
    item_file = "model\\" \
                + st.ITEMS_FN + "\\" \
                + item[st.F_TITLE].lower() + ".json"
    os.remove(item_file)

    # Jankily force some time where Skully laments.
    tm = await tm.rebuild("...", req=False)
    await tm.rebuild(st.INF_ITEM_DELETED, req=False)


async def vote_item(ctx, item):
    """A function to increase the vote count on an item."""
    # Check and get item data.
    if not used_title(item):
        return await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                       content=st.ERR_ITEM_NONEXIST, mode=TidyMode.STANDARD)

    i_json = get_item_json(item)
    if ctx.message.author.name not in i_json[st.F_VOTERS]:
        # If they haven't voted yet, let them vote.
        i_json[st.F_VOTERS].append(ctx.message.author.name)
        store_item(i_json)

        await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                content=st.INF_VOTED.format(i_json[st.F_TITLE]), mode=TidyMode.STANDARD)
    else:
        await TidyMessage.build(ctx, st.ESCAPE_SEQUENCE, req=False,
                                content=st.ERR_ALREADY_VOTED, mode=TidyMode.WARNING)


# Checks


def check_unique(being_edited):
    def check(*args):
        return True if not used_title(" ".join(args)) or \
                       used_title(" ".join(args)) is being_edited + ".json" else st.ERR_NONUNIQUE
    return check


def check_alias_f(aliases, no_dups=False):
    """A check-factory that makes a check that looks to see if there's
     any of a set of characters inside of an alias [dictionary of values]."""
    def check(*args):
        # Prepare a list to measure variables already used and another to count checks.
        used, c_list, matched = list(), list(), False

        # Check each alias against each argument.
        for a in args:
            for name in aliases:
                for al in aliases[name]:
                    matched = al.lower() == a.lower()
                    if matched and name in used and no_dups:
                        return st.ERR_REPEAT_VAL.format(a)
                    elif matched:
                        used.append(name)
                        break
                if matched:
                    break
            if not matched:
                return st.ERR_NOT_IN_ALIAS.format(a)
        return True
    return check


def check_args_f(op, num):
    """A check-factory that makes a check that looks at the number of args relative to an operator.
        len(args) <op> num :: Plain English: the number of args should be <op> 'num' otherwise throw an error."""
    if op == st.MODE_GT:
        def check(*args):
            return True if len(args) > num else st.ERR_TOO_FEW_ARGS.format("more than", str(num))
    elif op == st.MODE_GTE:
        def check(*args):
            return True if len(args) >= num else st.ERR_TOO_FEW_ARGS.format(str(num), "or more")
    elif op == st.MODE_LT:
        def check(*args):
            return True if len(args) < num else st.ERR_TOO_MANY_ARGS.format("less than", str(num))
    elif op == st.MODE_LTE:
        def check(*args):
            return True if len(args) <= num else st.ERR_TOO_MANY_ARGS.format(str(num), "or less")
    elif op == st.MODE_EQ:
        def check(*args):
            return True if len(args) == num else st.ERR_INEXACT_ARGS.format(str(num))
    else:  # I hate myself, so fail silently and just not check the args for not inputting things properly.
        def check(*args):
            return True
    return check


# Utility #


def get_item_json(item):
    """Helper method to get item data. Expects .json extension."""
    # Define the path.
    item_file = "model\\" \
                + st.ITEMS_FN + "\\" \
                + item + ".json"

    # Load in file.
    with open(item_file, "r") as fout:
        i_json = json.load(fout)

    return i_json


def store_item(item):
    """Helper method to store item data."""
    # Add item entry.
    item_file = "model\\" \
                + st.ITEMS_FN + "\\" \
                + item[st.F_TITLE].lower() + ".json"

    with open(item_file, "w") as fout:
        json.dump(item, fout, indent=1)


def return_member(ctx, mention="", user_id=""):
    """Returns the user by mention or None, if none found. If an ID is provided, returns based off of that instead."""

    # # If ID provided, return what the bot would return. # #

    if user_id:
        return val.bot.get_user(user_id)

    # # If no ID provided, return based on mention. # #

    # Link members to their mentions.
    members = {}
    for mem in ctx.guild.members:
        members[mem.mention] = mem

    return members.get(mention)


def used_title(item):
    """Checks the items folder to see if an item exists. If it does, returns the item name."""
    # Make sure the item name is properly formatted.
    items_dir = "model\\" \
                + st.ITEMS_FN

    # Load in file.
    print(os.path.exists(items_dir))
    if not os.path.exists(items_dir):
        try:
            print("Making Directory...")
            os.makedirs(items_dir)
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise
    i_names = os.listdir(items_dir)
    for i in i_names:
        if i.lower() == (item + ".json").lower():
            return i
    return False


def get_app_token():
    with open('token.txt', 'r') as token:
        token = token.read()
    return token


def comm_ended(tm, ctx):
    return tm.message.embeds[0].description == st.TIMEOUT or tm.prompt.content == st.ESCAPE_SEQUENCE

# ----------- Script by ReedRGale ----------- #
# Utility functions used throughout the script. #


import asyncio
import json
import os

from model import val, st, alias
from view.TidyMessage import TidyMessage
from model.enums import TidyMode


# Function Encapsulators #


async def new_item(ctx, prompt, editing=False):
    """Encapsulator that handles making new items."""
    tidy, preview, unacceptable = "", None, True
    ctx_error = "NO ERROR"

    # Loop until acceptable.
    while unacceptable:
        # Prime the pump.
        nonunique = True

        # Ask for item title.
        while nonunique:
            if not tidy:
                title, tidy = await req(prompt, st.REQ_TITLE, ctx=ctx)
            else:
                title, tidy = await req(prompt, ctx_error + " " + st.REQ_TITLE, tidy=tidy)
            if title == val.escape:
                return val.escape
            prompt = title

            # Check for uniqueness.
            if not check_item(title.content) or editing:
                nonunique = False
            else:
                ctx_error = st.ERR_NONUNIQUE

        # Ask for item contents.
        item, tidy = await req(title, st.REQ_ITEM, tidy=tidy)
        if item == val.escape:
            return val.escape
        prompt = item

        # Preview for user.
        preview = "_" + title.content + "\n\n" + item.content + "_" + "\n\n"

        unchecked = True
        fin = None

        # Check if acceptable.
        while unchecked:
            if fin:
                fin, tidy = await req(prompt, preview + st.REPEAT_CONF + " " + st.ASK_ITEM_ACCEPTABLE, tidy=tidy)
            else:
                fin, tidy = await req(prompt, preview + st.ASK_ITEM_ACCEPTABLE, tidy=tidy)
            if fin == val.escape:
                return val.escape
            prompt = fin

            if fin.content.lower() in alias.AFFIRM:
                unacceptable = False
                unchecked = False
            elif fin.content.lower() in alias.DENY:
                unchecked = False
                ctx_error = st.REPEAT_ITEM

    # Prepare item entry.
    item_json = {st.F_TITLE: title.content,
                 st.F_ITEM: item.content,
                 st.F_OWNER: ctx.message.author.id,
                 st.F_VOTERS: [],
                 st.F_COMP: {},
                 st.F_ATTR: {},
                 st.F_CANON: False,
                 st.F_PROOFED: False}

    # Add item entry.
    store_item(item_json)

    return await tidy.rebuild(prompt, st.INF_ITEM_ADDED.format(title.content))


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

    # Concatenate all names.
    all_names, names, votes = "Here are all the items I have in my inventory! \n\n", list(), list()

    for key in i_names:
        names.append('~ ' + i_json[key][st.F_TITLE] + '\n')

    # Print in a tidy message.
    await TidyMessage.build(ctx, all_names, mode=TidyMode.STANDARD)


async def get_item(ctx, item):
    """Function designed to get an item and print it in a TidyMessage."""
    # Make sure the item exists.
    item = check_item(item)
    if not item:
        return await TidyMessage.build(ctx, st.ERR_ITEM_NONEXIST, mode=TidyMode.STANDARD)

    # Get item data.
    i_json = get_item_json(item)

    # Print in a tidy message.
    await TidyMessage.build(ctx, st.item_entry(ctx, i_json), mode=TidyMode.STANDARD)


async def edit_item(ctx, item):
    """Function to edit an existing item."""
    # Make sure the item exists.
    item = check_item(item)
    if not item:
        return await TidyMessage.build(ctx, st.ERR_ITEM_NONEXIST, mode=TidyMode.WARNING)

    # Check to make sure the editor is the creator
    item = get_item_json(item)
    if ctx.message.author.name != item[st.F_OWNER]:
        return await TidyMessage.build(ctx, st.ERR_NOT_YOURS, mode=TidyMode.WARNING)

    # Check to make sure they're okay losing votes.
    unchecked, conf, prompt = True, None, ctx.message

    while unchecked:
        if conf:
            conf, tidy = await req(prompt, st.REPEAT_CONF + " " + st.ASK_VOTE_ACCEPTABLE, tidy=tidy)
        else:
            conf, tidy = await req(prompt, st.ASK_VOTE_ACCEPTABLE, ctx=ctx)
        if conf == val.escape:
            return val.escape
        prompt = conf

        if conf.content.lower() in alias.AFFIRM:
            unchecked = False
        elif conf.content.lower() in alias.DENY:
            return await TidyMessage.build(ctx, st.INF_EXIT_EDIT, mode=TidyMode.STANDARD)

    # Define the path.
    items_dir = "model\\" \
                + st.ITEMS_FN

    # Record number of files in items before making a new one.
    i_names = os.listdir(items_dir)

    # Make the new item entry.
    await new_item(ctx, prompt, True)

    # If more files now, that means the old file wasn't overwritten, so delete it.
    if len(os.listdir(items_dir)) > len(i_names):
        os.remove(items_dir + "\\" + item)


async def vote_on(ctx, item):
    """A function to increase the vote count on an item."""
    # Check and get item data.
    item = check_item(item)
    if not item:
        return await TidyMessage.build(ctx, st.ERR_ITEM_NONEXIST, mode=TidyMode.STANDARD)
    i_json = get_item_json(item)

    if ctx.message.author.name not in i_json[st.F_VOTERS]:
        # If they haven't voted yet, let them vote.
        i_json[st.F_VOTERS].append(ctx.message.author.name)
        store_item(i_json)

        # Return a TM informing them the duty is done.
        await TidyMessage.build(ctx, st.INF_VOTED.format(i_json[st.F_TITLE]), mode=TidyMode.STANDARD)
    else:
        # Otherwise, return an error.
        await TidyMessage.build(ctx, st.ERR_ALREADY_VOTED, mode=TidyMode.WARNING)


# Utility #


def get_item_json(item):
    """Helper method to get item data. Expects .json extension."""
    # Define the path.
    item_file = "model\\" \
                + st.ITEMS_FN + "\\" \
                + item

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


def check_item(item):
    """Checks the items folder to see if an item exists. If it does, returns the item name."""
    # Make sure the item name is properly formatted.
    items_dir = "model\\" \
                + st.ITEMS_FN
    item += ".json"

    # Load in file.
    i_names = os.listdir(items_dir)
    for i in i_names:
        if i.lower() == item.lower():
            return i
    return False


async def req(prompt, req_str, tidy=None, **kwargs):
    """Ask a request for the user and return that request as a list of inputs or return an escape character."""

    # Prepare the mode
    mode = TidyMode.STANDARD

    if kwargs.get("mode"):
        mode = kwargs.get("mode")

    # Ask the request.
    if not tidy:
        tidy = await TidyMessage.build(kwargs.get("ctx"), req_str, mode=mode)
    else:
        await tidy.rebuild(prompt, req_str)

    # Define check
    a = prompt.author
    c = prompt.channel

    def check(resp): return resp.author == a and resp.channel == c

    # Wait for response.
    rsp = await val.bot.wait_for("message", check=check)
    if rsp.content.lower() == val.escape:
        return val.escape, tidy
    return rsp, tidy


def get_app_token():
    with open('token.txt', 'r') as token:
        token = token.read()
    return token

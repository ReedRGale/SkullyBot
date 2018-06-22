# ----------- Script by ReedRGale ----------- #
# Strings used throughout the scripts. #


from model import util


# Help Messages #


ADD_BRIEF = "A command group for adding new things for me to remember!"
ADD_HELP = "This group contains all commands that tell me to add new things to my set of things to remember!"

EDIT_BRIEF = "A command group for editing stuff I remember!"
EDIT_HELP = "This group contains all commands that tell me to change information that I remember!"

DELETE_BRIEF = "A command for... forgetting things. ;...;"
DELETE_HELP = "This group contains all commands to forget information."

HELP_BRIEF = "Try calling 'skully, help [command]'! Also, if you ever want to escape a command early, " \
             "type 'nevermind, skully'."
HELP_HELP = "Good work. That is exactly how you check the detailed help docs of a command."


ADDITEM_BRIEF = "This is how you should add a new item to the list of items we might try to combine!"
ADDITEM_HELP = "To Call: 'skully, add item'\n\n" \
          "Call anywhere within the server to record a value. Basically, sir or ma'am, I'll ask you for something " \
          "you want to call this potential item, then I'll ask for its description so that I can keep it in " \
          "my memory for safekeeping. I'll be your virtual 'inventory' so to speak! ^...^"

ADDSOUL_BRIEF = "This is how Panur can add a new souls to the record of characters!"
ADDSOUL_HELP = "To Call: 'skully, add soul [character] [amount]'\n\n" \
          "Call anywhere within the server to add souls to a character. Basically, miss Pan, put in the character " \
          "and then input the value! ^...^ If a character doesn't yet exist, I'll create them with this command too! " \
          "I can also remove soul value in case of messups or odd circumstances by putting in negative numbers. " \
          " Ex: skully, add soul Alice 3"

ITEMS_BRIEF = "'Items' is how you can ask for either all the items I have or, all the details on one specific item!"
ITEMS_HELP = "To Call: 'skully, items' OR 'skully, items [item]'\n\n" \
             "Call anywhere within the server to retrieve item info!! This allows me to tell you all about what you've " \
             "made or intended to make using the descriptions you've given me!"

ET_BRIEF = "'Edit' is where you can tell me to change the details of items!"
ET_HELP = "To Call: 'skully, edit [item]'\n\n" \
          "Call anywhere within the server to edit an item!! Only the person who made the item, however, can edit " \
          "it, though... unless it's already in canon! Then... only a few people can access it to edit entries. " \
          "This is so the canon stuff doesn't get all muddled."

VE_BRIEF = "'Vote' is how you can tell me you really like an item and want it to be made canon!"
VE_HELP = "To Call: 'skully, vote [item]'\n\n" \
          "Call anywhere within the server to vote on an item!! I'll tally your vote toward this item, but " \
          "please only vote once. The goal of this is to know what item ideas are most popular, after all!! " \
          ">...<"

DE_BRIEF = "'Delete' is how you tell me to *gasp* remove items!!!"
DE_HELP = "To Call: 'skully, delete [item]'\n\n" \
          "Call anywhere within the server to delete an item you own!! Just, uh, be careful. Deleted items are " \
          "gone... forever!!"


# Informative #


INF_ITEM_ADDED = "Item stored away! If you ever want to look at it again, just call 'skully, items {}'. ^...^"
INF_EXIT_EDIT = "Whew. Glad we didn't do that then! Poke me again if you want to edit it though."
INF_VOTED = "Aaaand your vote is tallied. One step higher in popularity for {}!!"
INF_EXIT_DELETE = "Hah... you scared me for a moment, Observer!! Trust me, this item is safe with me!"
INF_ITEM_DELETED = "Its... it's gone now..."
INF_GROUP = "<Command-Group>"
INF_COMMAND = "<Command>"
INF_COMMAND_GROUP = "Here's everything I know about this group of commands: \n\n"
INF_HELP = "Here's what I know about '{}:' \n\n{}"
INF_TOP_LEVEL_COMMANDS = "Here's all the major command types. If you want to delve them further, " \
                         "just call 'skully, help <subcommand>'!\n\n"
INF_NO_CHARACTER_CREATION = "Got it! Let me know if you change your mind though!!"
INF_NO_ADDED_SOULS = "Alright! Let me know if you need me to add souls in the future though!!"
INF_NEW_SOUL_VALUE = "{} is now {} souls stronger! They have {} souls total, are level {} " \
                     "now and {} souls until levelup!"

ESCAPE = "I'll escape the command, but just because you asked nicely. ;>"
TIMEOUT = "So, you've taken a bit to continue this command. So... call me back when you know what you want to " \
          "do. Indecisiveness is a real bore. Ciao!"


REPEAT_ITEM = "Alright then! Let's try working through this again! As many times as it takes! >...<"
REPEAT_CONF = "I'm sorry, I didn't quite catch that!"

ADDSOUL_PREVIEW = "Is this okay?\n\n {}:\n\n**Level:** {} --> {}\n**Souls:** {} --> {}\n**Next Level:** {} --> {}"


# Confirmation #


ASK_ITEM_ACCEPTABLE = "So, how does this look? Is it acceptable?"
ASK_VOTELOSS_ACCEPTABLE = "Um, if you edit this, you might change how others see it. I'll have to, um, delete its " \
                      "votes. Is that... okay? >...<"
ASK_DELETE_ACCEPTABLE = "Are you... sure you want to delete this...? ;...;"
ESCAPE_SEQUENCE = "nevermind, skully"


# Requests #


REQ_TITLE = "So, you've got a new item for me, sir or ma'am? What is it going to be called?"
REQ_DESCRIPTION = "Alright... describe for me the item, if you would!!"
REQ_CHARACTER_CREATION = "So I don't know who this is... did you want me to make a new entry for this character?"


# Filepaths #


FLD_PATH = "path"
FLD_TTLE = "title"
FLD_CNTT = "content"
FLD_MODE = "mode"
FLD_PAGE = "page"
FLD_EDTBL = "editable"
FLD_NAME = "name"
FLD_SOUL = "souls"
COMM_UNF = "unaffiliated"

ITEMS_FN = "items"
GUILDS_FN = "guilds"
MODEL_FN = "model"
LOGS_FN = "logs"
CANONS_FN = "canons"
COMMANDS_FN = "commands"
GENERAL_FN = "general"
WS_FN = "willfordswap"
CHARACTER_FN = "character"


# Comparison Modes #


MODE_GT = ">"
MODE_GTE = ">="
MODE_LT = "<"
MODE_LTE = "<="
MODE_EQ = "=="


# Fields #


F_TITLE = "title"       # The name of the item
F_ITEM = "item"         # The description
F_OWNER = "owner"       # The submitter of the item idea
F_VOTERS = "voters"     # The voters for this item
F_COMP = "components"   # The base items that are suggested to make this item
F_ATTR = "attributes"   # Traits this item has inherited from basic items
F_CANON = "canon"       # Whether this item is in the canon or not
F_PROOFED = "proofed"   # Whether this item has been checked by someone official or not


# Errors #


ERR_EXTRA_ARGS = "Sorry sir, or ma'am. That's just a few too many arguments. I kind of just expected {}. Maybe " \
                 "try again with that?"
ERR_NONUNIQUE = "Um, an item with that name already exists? Sorry!! Could you rename it quickly?"
ERR_ITEM_NONEXIST = "Apologies, sir or ma'am! That item doesn't look like it exists!!"
ERR_NOT_YOURS = "Hey! This isn't yours!!!"
ERR_INVALID_TIDYMODE = "Mr. Programmer, it looks like you gave me a TidyMode I don't know how to work with. " \
                       "And now, some user is probably going 'huh? what's that?' You only have yourself to blame " \
                       "now, Mr. Programmer. After all, you wrote this error code."

ERR_ADD_WHAT = "Observer... add what thing...? >...<"
ERR_EDIT_WHAT = "Observer... edit what item...? >...<"
ERR_DELETE_WHAT = "Observer... delete what now...? >...<"
ERR_VOTE_WHAT = "Observer... vote what...? >...<"
ERR_CANT_VOTE_YOU_OWN = "Sir or ma'am... isn't voting for your own idea... kind of redundant? Like... didn't you " \
                        "make it because you wanted it? I mean, this is a serious question, Observer. But really. " \
                        "No. I'm not letting you vote on your own item."
ERR_NO_ARG_EDIT = "Umm... edit... what?"
ERR_REPEAT_VAL = "So, you don't repeat variables here. Please. You know the one I'm talking about. " \
                 "'{}.' Don't do that."
ERR_NOT_IN_ALIAS = "I don't know the word '{}' in this context. Maybe try again?"
ERR_ALREADY_VOTED = "I understand you're excited, sir or ma'am, but if you could refrain from voting for an item " \
                    "twice, I would greatly appreciate it!!"
ERR_NO_SUCH_CHILD = "Uhh, the command '{}' doesn't have a child command called '{}.'"
ERR_NO_SUCH_TYPE = "So, I looked, and I don't have any command in my database called '{}.' Not under '{}' anyway. " \
                   "Sorry fam."
ERR_TOO_FEW_ARGS = "Soooo, I'm looking for a few more arguments than that. Specifically, I'm looking for {} {}."
ERR_TOO_MANY_ARGS = "Bit overkill there. I'm looking for a little less than that. Specifically, {} {}. If you want to" \
                    " have two words in one word here, surround it with quotation marks like \"this is!\""
ERR_INEXACT_ARGS = "Noooot exactly. I'm looking for '{}' arg here. If you want to" \
                    " have two words in one word here, surround it with quotation marks like \"this is!\""
ERR_INVALID_TM_CONTENT = "Mr. Programmer, somehow you've failed to give me a string or an Embed to show our lovely " \
                         "users. Tut tut. Get on that."

# File Paths #
                                                            # Formatting String Args:

GUILDS_P = MODEL_FN + "\\" + GUILDS_FN                      # None
GUILD_P = GUILDS_P + "\\{}"                                 # Guild ID
CANONS_P = GUILD_P + "\\" + CANONS_FN                       # Guild ID
CANON_P = CANONS_P + "\\{}"                                 # Guild ID, Canon ID
C_LOGS_P = CANON_P + "\\" + LOGS_FN                         # Guild ID, Canon ID
COMMAND_C_LOGS_P = C_LOGS_P + "\\" + COMMANDS_FN            # Guild ID, Canon ID
MEM_COMMAND_C_LOGS_P = COMMAND_C_LOGS_P + "\\{}"            # Guild ID, Canon ID, Member ID
MEM_COMMAND_C_LOG_P = MEM_COMMAND_C_LOGS_P + "\\{}.json"    # Guild ID, Canon ID, Member ID, (Command Name + Number)
GENERAL_P = GUILD_P + "\\" + GENERAL_FN                     # Guild ID
G_LOGS_P = GENERAL_P + "\\" + LOGS_FN                       # Guild ID
COMMAND_G_LOGS_P = G_LOGS_P + "\\" + COMMANDS_FN            # Guild ID
MEM_COMMAND_G_LOGS_P = COMMAND_G_LOGS_P + "\\{}"            # Guild ID, Member ID
MEM_COMMAND_G_LOG_P = MEM_COMMAND_G_LOGS_P + "\\{}.json"    # Guild ID, Member ID, (Command Name + Number)


# Complex #


def bold(frmt):
    """Formats a string into a bold string"""
    return "**" + frmt + "**"


def itlc(frmt):
    """Formats a string into a italicized string"""
    return "_" + frmt + "_"


def item_entry(ctx, json):
    """Prints out an item in a nice format."""
    return "{} by {} :: Votes: {} \n\n{}".format(json[F_TITLE],
                                                 util.return_member(ctx, user_id=json[F_OWNER]),
                                                 len(json[F_VOTERS]),
                                                 json[F_ITEM])

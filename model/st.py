# ----------- Script by ReedRGale ----------- #
# Strings used throughout the scripts. #


from model import util


# Help Messages #


HP_BRIEF = "Try calling 'skully, help [command]'! Also, if you ever want to escape a command early, " \
           "type 'nevermind, skully'."
HP_HELP = "Good work. That is exactly how you check the detailed help docs of a command."


NI_BRIEF = "'NewItem' is how you should add a new item to the list of items we might try to combine!"
NI_HELP = "To Call: 'skully, newitem'\n\n" \
          "Call anywhere within the server to record a value. Basically, sir or ma'am, I'll ask you for something " \
          "you want to call this potential item, then I'll ask for its description so that I can keep it in " \
          "my memory for safekeeping. I'll be your virtual 'inventory' so to speak! ^...^"

IS_BRIEF = "'Items' is how you can ask for either all the items I have or, all the details on one specific item!"
IS_HELP = "To Call: 'skully, items' OR 'skully, items [item]'\n\n" \
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


REPEAT_ITEM = "Alright then! Let's try working through this again! As many times as it takes! >...<"
REPEAT_CONF = "I'm sorry, I didn't quite catch that!"


# Confirmation #


ASK_ITEM_ACCEPTABLE = "So, how does this look? Is it acceptable?"
ASK_VOTE_ACCEPTABLE = "Um, if you edit this, you might change how others see it. I'll have to, um, delete its " \
                      "votes. Is that... okay? >...<"
ASK_DELETE_ACCEPTABLE = "Are you... sure you want to delete this...? ;...;"


# Requests #


REQ_TITLE = "So, you've got a new item for me, sir or ma'am? What is it going to be called?"
REQ_ITEM = "Alright... describe for me the item, if you would!!"


# Filepaths #


ITEMS_FN = "items"


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
<<<<<<< HEAD
<<<<<<< HEAD
ERR_EDIT_WHAT = "Observer... edit what item...? >...<"
ERR_DELETE_WHAT = "Observer... delete what now...? >...<"
=======
ERR_EDIT_WHAT = "Observer... edit what item... >...<"
ERR_EDIT_WHAT = "Observer... delete what now... >...<"
>>>>>>> parent of a4ff330... Added rudimentary recipe storing functionality.
ERR_CANT_VOTE_YOU_OWN = "Sir or ma'am... isn't voting for your own idea... kind of redundant? Like... didn't you " \
                        "make it because you wanted it? I mean, this is a serious question, Observer. But really. " \
                        "No. I'm not letting you vote on your own item."
=======
ERR_EDIT_WHAT = "Observer... edit what item... >...<"
ERR_EDIT_WHAT = "Observer... delete what now... >...<"
>>>>>>> parent of 02eae38... Check to make sure people don't vote for their own item.
ERR_NO_ARG_EDIT = "Umm... edit... what?"
ERR_ALREADY_VOTED = "I understand you're excited, sir or ma'am, but if you could refrain from voting for an item " \
                    "twice, I would greatly appreciate it!!"

# Complex #


def item_entry(ctx, json):
    """Prints out an item in a nice format."""
    return "{} by {} :: Votes: {} \n\n{}".format(json[F_TITLE],
                                                 util.return_member(ctx, user_id=json[F_OWNER]),
                                                 len(json[F_VOTERS]),
                                                 json[F_ITEM])

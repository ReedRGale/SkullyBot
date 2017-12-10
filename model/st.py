# ----------- Script by ReedRGale ----------- #
# Strings used throughout the scripts. #


from model import util


# Help Messages #


HP_BRIEF = "Try calling 'skully, help [command]'! Also, if you ever want to escape a command early, " \
           "type 'nevermind, skully'."
HP_HELP = "Good work. That is exactly how you check the detailed help docs of a command."

NI_BRIEF = "'New Item' is how you should add a new item to the list of items we might try to combine!"
NI_HELP = "To Call: 'skully, new item'\n\n" \
          "Call anywhere within the server to record a value. Basically, sir or ma'am, I'll ask you for something " \
          "you want to call this potential item, then I'll ask for its description so that I can keep it in " \
          "my memory for safekeeping. I'll be your virtual 'inventory' so to speak! ^...^"

IS_BRIEF = "'Items' is how you can ask for either all the items I have or, all the details on one specific item!"
IS_HELP = "To Call: 'skully, items' OR 'skully, items [item]'\n\n" \
          "Call anywhere within the server to retrieve item info!! This allows me to tell you all about what you've " \
          "made or intended to make using the descriptions you've given me!"

EI_BRIEF = "'Edit Item' is where you can tell me to change the details of items!"
EI_HELP = "To Call: 'skully, edit item [item]'\n\n" \
          "Call anywhere within the server to edit an item!! Only the person who made the item, however, can edit " \
          "it, though... unless it's already in canon! Then... only a few people can access it to edit entries. " \
          "This is so the canon stuff doesn't get all muddled."

VI_BRIEF = "'Vote Item' is how you can tell me you really like an item and want it to be made canon!"
VI_HELP = "To Call: 'skully, vote item [item]'\n\n" \
          "Call anywhere within the server to vote on an item!! I'll tally your vote toward this item, but " \
          "please only vote once. The goal of this is to know what item ideas are most popular, after all!! " \
          ">...<"

DI_BRIEF = "'Delete Item' is how you tell me to *gasp* remove items!!!"
DI_HELP = "To Call: 'skully, delete item [item]'\n\n" \
          "Call anywhere within the server to delete an item you own!! Just, uh, be careful. Deleted items are " \
          "gone... forever!!"

NR_BRIEF = "'New Recipe' is where you tell me a yummy to remember!"
NR_HELP = "To Call: 'skully, new recipe'\n\n" \
          "Call anywhere within the server to record a recipe. Basically, sir or ma'am, I'll ask you its name " \
          "then instructions on how to make it! Then... you can ask me anytime for the instructions!!"

RS_BRIEF = "'Recipes' is how you can pull up a yummy!"
RS_HELP = "To Call: 'skully, recipes' OR 'skully, recipes [recipe]'\n\n" \
          "This is how you can ask me for the recipes you've recorded! I can either give you all of them, or " \
          "a specific one, if you tell me what it is!!"

ER_BRIEF = "'Edit Recipe' is where you can tell me to change the details of a recipe!"
ER_HELP = "To Call: 'skully, edit recipe [recipe]'\n\n" \
          "Call anywhere within the server to edit a recipe!! Only the person who made the recipe can edit " \
          "it, though! Don't try to change what isn't yours!!"

VR_BRIEF = "'Vote Recipe' is how you can tell me you really like a recipe and want others to make it!"
VR_HELP = "To Call: 'skully, vote recipe [recipe]'\n\n" \
          "Call anywhere within the server to vote on foodstuff!! I'll tally your vote toward it, but " \
          "you can only vote once!"

DR_BRIEF = "'Delete Recipe' is how you tell me to *sob* forget recipes!!!"
DR_HELP = "To Call: 'skully, delete recipe [recipe]'\n\n" \
          "Call anywhere within the server to delete a recipe you own!! Just, uh, be careful. Afterwards, it's " \
          "gone... forever!!"


# Informative #


INF_RECIPE_ADDED = "Recipe recorded! Hope you guys make this yum at some point!"
INF_ITEM_ADDED = "Item stored away! If you ever want to look at it again, just call 'skully, items {}'. ^...^"
INF_ITEM_ADDED = "One more yummy for the books! " \
                 "If you ever want to cook it, just call 'skully, recipes {}'. ^...^"
INF_EXIT_EDIT = "Whew. Glad we didn't do that then! Poke me again if you want to edit it though."
INF_VOTED = "Aaaand your vote is tallied. One step higher in popularity for {}!!"
INF_EXIT_DELETE = "Hah... you scared me for a moment, Observer!! Trust me, this item is safe with me!"
INF_ITEM_DELETED = "Its... it's gone now..."


REPEAT_DATA = "Alright then! Let's try working through this again! As many times as it takes! >...<"
REPEAT_CONF = "I'm sorry, I didn't quite catch that!"


# Confirmation #


ASK_ACCEPTABLE = "So, how does this look? Is it acceptable?"
ASK_VOTE_ACCEPTABLE = "Um, if you edit this, you might change how others see it. I'll have to, um, delete its " \
                      "votes. Is that... okay? >...<"
ASK_DELETE_ACCEPTABLE = "Are you... sure you want to delete this...? ;...;"


# Requests #


REQ_TITLE_R = "A new recipe!? What's it called?"
REQ_TITLE = "So, you've got a new item for me, sir or ma'am? What is it going to be called?"
REQ_ITEM = "Alright... describe for me the item, if you would!!"
REQ_RECIPE = "Alright... so, step by step, how do I make this foodstuff? ^...^"


# Filepaths #


ITEMS_FN = "items"
RECIPES_FN = "recipes"


# Fields #


F_TITLE = "title"       # The name of the item
F_ITEM = "item"         # The description
F_OWNER = "owner"       # The submitter of the item idea
F_VOTERS = "voters"     # The voters for this item
F_COMP = "components"   # The base items that are suggested to make this item
F_ATTR = "attributes"   # Traits this item has inherited from basic items
F_GHOST = "ghost"       # Components inherited that may be a ghost copy.
F_CANON = "canon"       # Whether this item is in the canon or not
F_PROOFED = "proofed"   # Whether this item has been checked by someone official or not
F_IMAGES = "images"     # Contains links to images of a recipe


# Errors #


ERR_EXTRA_ARGS = "Sorry sir, or ma'am. That's just a few too many arguments. I kind of just expected {}. Maybe " \
                 "try again with that?"
ERR_NONUNIQUE = "Um, an something with that name already exists? Sorry!! Could you rename it quickly?"
ERR_NONEXIST = "Apologies, sir or ma'am! Whatever that is... doesn't look like it exists!!"
ERR_NOT_YOURS = "Hey! This isn't yours!!!"
ERR_INVALID_TIDYMODE = "Mr. Programmer, it looks like you gave me a TidyMode I don't know how to work with. " \
                       "And now, some user is probably going 'huh? what's that?' You only have yourself to blame " \
                       "now, Mr. Programmer. After all, you wrote this error code."
ERR_EDIT_WHAT = "Observer... edit what item...? >...<"
ERR_DELETE_WHAT = "Observer... delete what now...? >...<"
ERR_CANT_VOTE_YOU_OWN = "Sir or ma'am... isn't voting for your own idea... kind of redundant? Like... didn't you " \
                        "make it because you wanted it? I mean, this is a serious question, Observer. But really. " \
                        "No. I'm not letting you vote on your own item."
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


def recipe_entry(ctx, json):
    """Prints out a recipe in a nice format."""
    return "{} by {} :: Votes: {} \n\n{}".format(json[F_TITLE],
                                                 util.return_member(ctx, user_id=json[F_OWNER]),
                                                 len(json[F_VOTERS]),
                                                 json[F_ITEM])

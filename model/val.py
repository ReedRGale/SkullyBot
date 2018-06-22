# ----------- Script by ReedRGale ----------- #
# Global values used in the scripts. #


# Imports #


from discord.ext import commands


# Timeout Times #


SHORT = 30
MEDIUM = 90
LONG = 180
FUCKING_NOVEL = 1800


# Links #


T_URLS_STANDARD = ["https://image.ibb.co/fvgnxw/chrome_2017_12_02_01_44_59.png"]
T_URLS_WARNING = ["https://image.ibb.co/ciiTLG/chrome_2017_12_06_00_39_54.png"]
A_URLS_STANDARD = ["https://image.ibb.co/nhRWPb/chrome_2017_12_05_22_29_14.png"]
A_URLS_WARNING = ["https://image.ibb.co/nhRWPb/chrome_2017_12_05_22_29_14.png"]
GITHUB_URL = "https://github.com/ReedRGale/SkullyBot"
AVATAR_STRING = "https://cdn.discordapp.com/avatars/{}/{}.jpg"


def p_avatar(tm):
    """Uses the TidyMessage to get context on the prompt of who's calling. Use that to get the avatar of the user."""
    return AVATAR_STRING.format(tm.prompt.author.id, tm.prompt.author.avatar)


def p_color(tm):
    return tm.prompt.author.color


# Variables #


calling = dict()
escape = "nevermind, skully"
bot = commands.Bot(command_prefix="skully, ", fetch_offline_members=True, owner_id=387875136159744001)

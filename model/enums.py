# ----------- Script by ReedRGale ----------- #
# Enumerator values used in the scripts. #


from enum import Enum


class TidyMode(Enum):
    STANDARD = 0
    WARNING = 1
    PROMPT = 2

    def __eq__(self, other):
        if self.__class__ is other.__class__:
            return self.value == other.value
        return NotImplemented
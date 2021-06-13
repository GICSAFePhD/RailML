from abc import ABC
from enum import Enum

class Usage(Enum):
    USING_START = 0
    USING_END = 1

class LrsMethod(Enum):
    ABSOLUTE = 0
    INTERPOLATION = 1
    RELATIVE = 2

class ApplicationDirection(Enum):
    BOTH = "both"
    NORMAL = "normal"
    REVERSE = "reverse"

class Orientation(Enum):
    LEFT = -1
    RIGHT = 1
    
class Navigability(Enum):
    AB = "AB"
    BA = "BA"
    BOTH = "both"
    NONE = "none"


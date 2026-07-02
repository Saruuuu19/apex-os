from enum import Enum


class SetType(str, Enum):
    WARM_UP = "warm_up"
    NORMAL = "normal"
    DROP_SET = "drop_set"
    FAILURE = "failure"

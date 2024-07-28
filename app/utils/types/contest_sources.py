from enum import Enum
from app.data_fetchers.code_chef import CodeChef
from app.data_fetchers.code_forces import CodeForces
from app.data_fetchers.coding_ninjas import CodingNinjas
from app.data_fetchers.gfg import GFG
from app.data_fetchers.leet_code import LeetCode


class ContestSource(Enum):
    CODE_CHEF = ("Code Chef", CodeChef())
    CODE_FORCES = ("Code Forces", CodeForces())
    CODE_NINJAS = ("Code Ninjas", CodingNinjas())
    GFG = ("Geeks For Geeks", GFG())
    LEET_CODE = ("Leet Code", LeetCode())

    def __init__(self, name: str, fetcher):
        self.source_name = name
        self.fetcher = fetcher

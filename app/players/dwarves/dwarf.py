from abc import ABC, abstractmethod

from app.players.player import Player


class Dwarf(Player, ABC):
    """""Base class for Dwarves"""""
    def __init__(self, nickname: str, favourite_dish: str) -> None:
        super().__init__(nickname=nickname)
        self._favourite_dish = favourite_dish

    def eat_favourite_dish(self) -> None:
        print(f"{self.nickname} is eating {self._favourite_dish}")
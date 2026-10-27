"""Сумісні імпорти персонажів з окремих модулів."""

from .enemy import Enemy
from .npc import NPC
from .player import Player

__all__ = ["Player", "Enemy", "NPC"]

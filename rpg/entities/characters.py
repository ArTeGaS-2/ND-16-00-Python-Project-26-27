"""Ігрові персонажі."""

from .base import Entity


class Player(Entity):
    """Персонаж гравця."""

    pass


class Enemy(Entity):
    """Ворожа сутність."""

    pass


class NPC(Entity):
    """Неігровий персонаж."""

    pass

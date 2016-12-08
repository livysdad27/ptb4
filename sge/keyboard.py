# Copyright (C) 2012-2014 Julie Marchant <onpon4@riseup.net>
# 
# This file is part of the Pygame SGE.
# 
# The Pygame SGE is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# The Pygame SGE is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
# 
# You should have received a copy of the GNU Lesser General Public License
# along with the Pygame SGE.  If not, see <http://www.gnu.org/licenses/>.

"""
This module provides functions related to keyboard input.
"""

from __future__ import division
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

import pygame

import sge


__all__ = ["get_pressed", "get_modifier", "get_focused", "set_repeat",
           "get_repeat_enabled", "get_repeat_interval", "get_repeat_delay"]

_repeat_enabled = False


def get_pressed(key):
    """
    Return whether or not a key is pressed.

    See the documentation for :class:`sge.input.KeyPress` for more
    information.
    """
    key = key.lower()
    if key in sge.KEYS:
        return pygame.key.get_pressed()[sge.KEYS[key]]
    else:
        return False


def get_modifier(key):
    """
    Return whether or not a modifier key is being held.

    Arguments:

    - ``key`` -- The identifier string of the modifier key to check; see
      the table below.

    ================= =================
    Modifier Key Name Identifier String
    ================= =================
    Alt               ``"alt"``
    Left Alt          ``"alt_left"``
    Right Alt         ``"alt_right"``
    Ctrl              ``"ctrl"``
    Left Ctrl         ``"ctrl_left"``
    Right Ctrl        ``"ctrl_right"``
    Meta              ``"meta"``
    Left Meta         ``"meta_left"``
    Right Meta        ``"meta_right"``
    Shift             ``"shift"``
    Left Shift        ``"shift_left"``
    Right Shift       ``"shift_right"``
    Mode              ``"mode"``
    Caps Lock         ``"caps_lock"``
    Num Lock          ``"num_lock"``
    ================= =================
    """
    key = key.lower()
    if key in sge.MODS:
        return pygame.key.get_mods() & sge.MODS[key]
    else:
        return False


def get_focused():
    """Return whether or not the game has keyboard focus."""
    return pygame.key.get_focused()


def set_repeat(enabled=True, interval=0, delay=0):
    """
    Set repetition of key press events.

    Arguments:

    - ``enabled`` -- Whether or not to enable repetition of key press
      events.
    - ``interval`` -- The time in milliseconds in between each repeated
      key press event.
    - ``delay`` -- The time in milliseconds to wait after the first key
      press event before repeating key press events.

    If ``enabled`` is set to true, this causes a key being held down to
    generate additional key press events as long as it remains held
    down.
    """
    global _repeat_enabled
    _repeat_enabled = enabled
    if enabled:
        pygame.key.set_repeat(delay, interval)
    else:
        pygame.key.set_repeat()


def get_repeat_enabled():
    """
    Return whether or not repetition of key press events is enabled.

    See the documentation for :func:`sge.keyboard.set_repeat` for more
    information.
    """
    return _repeat_enabled


def get_repeat_interval():
    """
    Return the interval in between each repeated key press event.

    See the documentation for :func:`sge.keyboard.set_repeat` for more
    information.
    """
    return pygame.key.get_repeat()[1]


def get_repeat_delay():
    """
    Return the delay before repeating key press events.

    See the documentation for :func:`sge.keyboard.set_repeat` for more
    information.
    """
    return pygame.key.get_repeat()[0]

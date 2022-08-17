#!/usr/bin/autokey
# -*- coding: utf-8 -*-
""" Optimal distribution of skill points for the game Gemcraft 2: Chasing Shadows.

This script is based on the tables, calculations and theories in the thread
https://steamcommunity.com/sharedfiles/filedetails/?id=486419356

You need https://github.com/autokey/autokey to use this script.
You also need to have "xte" installed on your system.

Parameters:
Before executing this script, please modify the following variables in the source code:
    skill_points: Use your current skill points here.
    skill_rest: How many of your skill points should remain after the procedure.

Execution:
    * Set the two parameters
    * Define a hotkey for the script in Autokey
    * Switch to the skill page in the game
    * Now run the script by pressing the hotkey
    * Have fun
"""
__author__ = "Harald Stowasser"
__copyright__ = "2022 Harald Stowasser"
__credits__ = ["12345ieee"]
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Harald Stowasser"
__email__ = "harald@stowasser.tv"
__status__ = "Production"

import math, sys, os

abspath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abspath + '/module')
from gem_tools import gem_tools

tools = gem_tools(keyboard, system, time, mouse, store)

skill_points = 18540
skill_rest = 2000

print("Set Skills")


class SkillZ:
    """Calculator for the distribution of skill points

    Args:
        n (int): How many skill points should be distributed

    Attributes:
        xTrueColors (int): skill points
        xBloodbound (int): skill points
        xLeech (int): skill points
        xTraps (int): skill points
        xCriticalHit (int): skill points
        xResonance (int): skill points
        xAmps (int): skill points
    """

    # These constants regulate the distribution of skills
    fTrueColors = 1  # type: Final[float]
    fBloodbound = 1 / 1.05  # type: Final[float]
    fLeech = 1 / 1.25  # type: Final[float]
    fTraps = 1 / 1.85  # type: Final[float]
    fCriticalHit = 1 / 2.75  # type: Final[float]
    fResonance = 1 / 3.85  # type: Final[float]
    fAmps = 1 / 2.1  # type: Final[float]

    def __calc(self, n):
        """Calculates the ratios."""
        self.xTrueColors = int(n * SkillZ.fTrueColors)
        self.xBloodbound = int(n * SkillZ.fBloodbound)
        self.xLeech = int(n * SkillZ.fLeech)
        self.xTraps = int(n * SkillZ.fTraps)
        self.xCriticalHit = int(n * SkillZ.fCriticalHit)
        self.xResonance = int(n * SkillZ.fResonance)
        self.xAmps = int(n * SkillZ.fAmps)

    def __init__(self, hp):
        self.all = SkillZ.fTrueColors + SkillZ.fBloodbound + SkillZ.fLeech + SkillZ.fTraps \
                   + SkillZ.fCriticalHit + SkillZ.fResonance + SkillZ.fAmps
        n = self.i_gaus(hp / self.all)
        self.__calc(n)
        aprox = n / 2
        for t in range(7):
            if hp - self.used_mana() > 0:
                n = n + aprox
            else:
                n = n - aprox
            aprox = aprox / 2
            self.__calc(n)
        if hp - self.used_mana() < 0:
            n = n - 0.5
            self.__calc(n)

    def gaus(self, n):
        """The consumption of skill points follows the Gaussian sum formula"""
        return (n * (n + 1)) / 2

    def i_gaus(self, n):
        """inverse function to the Gaussian summation formula"""
        return int(math.sqrt(n * 2))

    def __str__(self):
        return "{} {} {} {} {} {} {}".format(self.xTrueColors, self.xBloodbound, self.xLeech, self.xTraps,
                                             self.xCriticalHit, self.xResonance,
                                             self.xAmps)

    def used_mana(self):
        """calculates the used skill points Is needed to gradually approach the optimum."""
        return self.gaus(self.xTrueColors) + self.gaus(self.xBloodbound) + self.gaus(self.xLeech) \
               + self.gaus(self.xTraps) + self.gaus(self.xCriticalHit) + self.gaus(self.xResonance) \
               + self.gaus(self.xAmps)

    def __iter__(self):
        return iter([self.xTrueColors, self.xBloodbound, self.xLeech, self.xTraps, self.xCriticalHit, self.xResonance,
                     self.xAmps])


def schklik(x, y, nr):
    """Set the skill level by clicking the button.

    Args:
        x (int): horizontal position of the skill field. No pixel value!
        y (int): vertical position of the skill field. No pixel value!
        nr (int): Set to what value
    """
    tens = int(nr / 10)
    xx = 360 + (x - 1) * 298
    yy = 155 + (y - 1) * 157
    s = " 'usleep 500000'"
    command = s + " 'mousemove " + str(xx) + " " + str(yy) + "'" + s
    if tens > 0:
        command += " 'keydown Shift_L'"
        for t in range(tens):
            command += " 'mouseclick 1'" + s
        command += " 'keyup Shift_L'"
    singl = nr % 10
    for t in range(singl):
        command += " 'mouseclick 1'" + s
    tools.xte(command)


time.sleep(2)
mouse.click_relative(662, 975, 1)  # reset all the skill points

sk = SkillZ(skill_points - skill_rest)
print(sk)
schklik(1, 1, sk.xTrueColors)
schklik(5, 5, sk.xTraps)
schklik(2, 2, sk.xLeech)
schklik(2, 4, sk.xBloodbound)
schklik(3, 2, sk.xCriticalHit)
schklik(5, 1, sk.xResonance)
schklik(1, 5, sk.xAmps)

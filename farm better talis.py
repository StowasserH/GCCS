#!/usr/bin/autokey
"""This script builds gems """
import sys, os

__author__ = "harald@stowasser.tv"
__copyright__ = "MIT"

abspath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abspath + '/module')
from gem_tools import gem_tools

tools = gem_tools(keyboard, system, time, mouse, store)

print("Better talismanfarm")

monsters = True


def runStart():
    tools.tinySleep()
    mouse.click_relative(964, 548, 1)
    time.sleep(5)
    mouse.click_relative(800, 917, 1)
    tools.trait(1, 1)
    tools.trait(1, 2)
    tools.trait(1, 3)
    tools.trait(2, 3)
    tools.trait(3, 1)
    tools.trait(3, 2)
    tools.trait(3, 3)
    # Haunting:
    mouse.click_relative(1135, 325, 1)
    # Glaring:
    # mouse.click_relative(796, 327, 1)
    tools.tinySleep()
    tools.xte("'mousemove 1327 203' 'mouseclick 1' 'sleep 1' 'mouseclick 1' 'sleep 1' 'mouseclick 1' 'sleep 1'")
    tools.tinySleep()
    tools.xte("'mousemove 1147 923' 'mouseclick 1'")
    time.sleep(10)


def runLoop():
    laginess = 0
    tools.tinySleep()
    mouse.click_relative(964, 548, 1)
    time.sleep(5)
    tools.xte("'mousemove 1327 203' 'mouseclick 1' 'sleep 1' 'mouseclick 1' 'sleep 1' 'mouseclick 1' 'sleep 1'")
    tools.tinySleep()
    # Haunting:
    tools.xte("'mousemove 1135 325' 'mouseclick 1'")
    # Glaring:
    # mouse.click_relative(796, 327, 1)
    tools.xte("'mousemove 1147 923' 'mouseclick 1'")
    time.sleep(10)


def reserve_place():
    print("reserve_place")
    # Mana Tunel
    tools.wall(10, 9)
    tools.walls(11, 7, 11, 9)
    tools.walls(14, 7, 14, 10)
    tools.walls(15, 7, 16, 7)
    tools.walls(16, 4, 17, 4)
    tools.walls(18, 4, 21, 4)
    tools.walls(22, 5, 25, 5)
    tools.walls(24, 6, 27, 6)
    tools.walls(24, 9, 27, 9)
    tools.walls(27, 10, 27, 14)
    tools.walls(29, 18, 29, 19)
    tools.walls(30, 10, 30, 19)
    # Killtunnel
    tools.walls(40, 11, 40, 18)
    tools.walls(43, 11, 43, 18)
    tools.wall(39, 17)
    print("reserve_place_done")


def buildSlowgem():
    tools.getGem(2, 2)
    tools.getGem(9, 2)
    tools.combine(1, 2, 2, 2)
    tools.getGem(4, 1)
    tools.combine(1, 1, 2, 2)


def buildManagem():
    tools.getGem(7, 2)
    tools.getGem(9, 2)
    tools.combine(1, 2, 2, 2)
    tools.getGem(4, 1)
    tools.combine(1, 1, 2, 2)


def buildKillgem():
    tools.getGem(8, 4)
    tools.getGem(9, 4)
    tools.combine(1, 4, 2, 4)
    tools.getGem(4, 1)
    tools.combine(1, 1, 2, 4)


def iceField(x, y):
    tools.tinySleep()
    keyboard.send_keys("1")
    tools.tinySleep()
    tools.xte("'mousemove " + str(x) + " " + str(y) + " ' 'mouseclick 1'")
    tools.tinySleep()


def send_it(nr):
    y = 75 + 185 * nr
    tools.xte("'mousemove 40 " + str(y) + "' 'mouseclick 1'")
    tools.tinySleep()


def updateKilltunel(nr):
    tools.ugradeGem(39, 12, nr)
    tools.ugradeGem(39, 14, nr)
    tools.ugradeGem(39, 16, nr)
    tools.ugradeGem(43, 12, nr)
    tools.ugradeGem(43, 14, nr)
    tools.ugradeGem(43, 16, nr)


def updateManasLast(nr):
    tools.ugradeGem(40, 19, nr)
    tools.ugradeGem(38, 18, nr)
    tools.ugradeGem(36, 18, nr)
    tools.ugradeGem(34, 19, nr)
    tools.ugradeGem(32, 20, nr)
    tools.ugradeGem(30, 20, nr)
    tools.ugradeGem(27, 18, nr)
    tools.ugradeGem(28, 16, nr)
    tools.ugradeGem(28, 14, nr)


def updateManasFront(nr):
    tools.ugradeGem(28, 12, nr)
    tools.ugradeGem(28, 10, nr)
    tools.ugradeGem(26, 7, nr)
    tools.ugradeGem(24, 7, nr)
    tools.ugradeGem(22, 6, nr)
    tools.ugradeGem(20, 5, nr)
    tools.ugradeGem(18, 5, nr)
    tools.ugradeGem(16, 5, nr)
    tools.ugradeGem(14, 10, nr)
    tools.ugradeGem(12, 6, nr)
    tools.ugradeGem(12, 8, nr)
    tools.ugradeGem(12, 10, nr)
    tools.ugradeGem(10, 10, nr)


def updateManaAmps(nr):
    tools.ugradeGem(30, 10, nr)
    tools.ugradeGem(30, 12, nr)
    tools.ugradeGem(30, 14, nr)
    tools.ugradeGem(30, 16, nr)
    tools.ugradeGem(37, 16, nr)
    tools.ugradeGem(26, 13, nr)
    tools.ugradeGem(26, 12, nr)
    tools.ugradeGem(26, 9, nr)
    tools.ugradeGem(25, 10, nr)
    tools.ugradeGem(25, 5, nr)
    tools.ugradeGem(10, 8, nr)
    tools.ugradeGem(29, 18, nr)


def prepField():
    print("prepField")
    reserve_place()

    buildSlowgem()
    keyboard.send_keys("r")
    tools.grid_click(10, 10)
    tools.drag_stash2grid(2, 2, 10, 10)

    buildManagem()
    keyboard.send_keys("r")
    tools.grid_click(12, 10)
    tools.drag_stash2grid(2, 2, 12, 10)

    tools.dup(12, 10, 12, 8)
    tools.dup(12, 10, 12, 6)
    tools.dup(12, 10, 14, 5)

    tools.dup(10, 10, 16, 5)
    tools.dup(12, 10, 18, 5)
    tools.dup(12, 10, 20, 5)
    tools.dup(12, 10, 22, 6)
    tools.dup(12, 10, 24, 7)


def startPhase():
    global monsters

    print("startPhase")
    tools.fastBomb()
    print("go on:")
    tools.starte()

    time.sleep(3)
    tools.dup(10, 10, 26, 7)
    tools.dup(12, 10, 28, 10)
    tools.dup(12, 10, 28, 12)

    buildKillgem()
    keyboard.send_keys("r")
    tools.grid_click(41, 14)
    tools.grid_click(41, 14)

    tools.dup(12, 10, 28, 14)
    tools.dup(12, 10, 28, 16)
    tools.dup(10, 10, 41, 16)

    tools.fastBomb()
    tools.dup(10, 10, 27, 18)
    tools.dup(12, 10, 30, 20)
    tools.dup(12, 10, 32, 20)
    tools.dup(12, 10, 34, 19)
    tools.dup(12, 10, 36, 18)

    tools.stope()
    if monsters:
        tools.tower(45, 14, 8, 5)
        command = " 'sleep 2'"
        command += " 'mousemove 1420 514' 'sleep 1' 'mousedown 3'"
        command += " 'sleep 2'"
        command += " 'mousemove 1334 592' 'sleep 1' 'mouseup 3'"
        command += " 'sleep 2'"
        tools.xte(command)
        tools.amp(45, 12, 8, 5)
        tools.amp(45, 16, 8, 5)
        tools.ugradeGem(45, 14, 6)
    iceField(1154, 604)
    tools.ugradeGem(41, 14, 4, "4")
    tools.fastBomb(10)
    tools.starte()


def warmupPhase():
    tools.amp(39, 12, 8, 3)
    tools.amp(39, 14, 8, 3)
    tools.amp(39, 16, 8, 3)
    tools.amp(43, 12, 8, 3)
    tools.amp(43, 14, 8, 3)
    tools.amp(43, 16, 8, 3)

    tools.fastBomb(20)

    tools.amp(29, 18, 7, 3)
    tools.amp(30, 16, 7, 3)
    tools.amp(30, 14, 7, 3)
    tools.amp(30, 12, 7, 3)
    tools.amp(30, 10, 7, 3)

    tools.fastBomb(20)
    tools.dup(12, 10, 38, 18)
    tools.dup(12, 10, 40, 19)
    tools.ugradeGem(40, 19, 1, "6")

    tools.amp(24, 5, 7, 5)
    tools.amp(24, 9, 7, 5)
    tools.amp(26, 9, 7, 5)
    tools.amp(26, 11, 7, 5)
    tools.amp(26, 13, 7, 5)
    tools.fastBomb(20)
    tools.amp(10, 8, 7, 5)
    tools.amp(37, 16, 7, 5)
    iceField(1154, 604)
    tools.ugradeGem(41, 14, 5)
    tools.ugradeGem(41, 16, 5, "5")
    tools.fastBomb(20)


def endPhase():
    tools.lag_delay = 0.1
    updateKilltunel(4)
    tools.fastBomb(20)
    updateManasLast(1)
    tools.fastBomb(20)
    tools.ugradeGem(30, 10, 2)
    tools.ugradeGem(30, 12, 2)
    tools.ugradeGem(30, 14, 2)
    tools.ugradeGem(30, 16, 2)
    tools.ugradeGem(29, 18, 2)
    tools.fastBomb(20)
    updateManaAmps(2)
    tools.fastBomb(20)
    iceField(1154, 604)
    tools.ugradeGem(41, 14, 5)
    tools.ugradeGem(41, 16, 5)
    time.sleep(4)
    tools.fastBomb(20)
    updateManasFront(1)
    tools.fastBomb(20)

    command = " 'sleep 1'"
    command += " 'keydown Control_L'"
    command += " 'sleep 1'"
    command += " 'mousemove 31, 886' 'sleep 1' 'mouseclick 1'"
    command += " 'sleep 1'"
    command += " 'keyup Control_L'"
    tools.xte(command)

    tools.tinySleep()
    mouse.click_relative(155, 44, 1)
    tools.tinySleep()

    for i in range(5):
        updateKilltunel(2)
        time.sleep(4)
        updateManasLast(2)
        time.sleep(4)
        updateManaAmps(2)
        time.sleep(4)
        updateManasFront(2)
        time.sleep(4)
        iceField(1154, 604)
        tools.ugradeGem(41, 14, 3)
        tools.ugradeGem(41, 16, 2)
        if monsters:
            tools.ugradeGem(46, 14, 4)
            tools.ugradeGem(45, 12, 2)
            tools.ugradeGem(45, 16, 2)

    for i in range(14):
        if monsters:
            tools.ugradeGem(46, 14, 2)
            tools.ugradeGem(45, 12, 1)
            tools.ugradeGem(45, 16, 1)
            tools.ugradeGem(43, 12, 1)
            tools.ugradeGem(43, 14, 1)
            tools.ugradeGem(43, 16, 1)
        else:
            tools.ugradeGem(41, 14, 2)
            tools.ugradeGem(41, 16, 1)
            updateKilltunel(1)
        time.sleep(10)


# _______________________________________________________________________
#
time.sleep(2)
# runStart()
for i in range(12):
    tools.stop_counter = 0
    tools.bomb_count = 1
    tools.lag_delay = 0

    prepField()
    startPhase()
    warmupPhase()
    endPhase()
    tools.tinySleep()
    tools.xte("'mousemove 1699 987' 'mouseclick 1'")
    time.sleep(10)
    runLoop()

print("ende")

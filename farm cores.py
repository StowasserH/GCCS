#!/usr/bin/autokey
"""This script builds gems """
__author__ = "harald@stowasser.tv"
__copyright__ = "MIT"

# based on:
# Gemcraft: Chasing Shadows - Shadow core farming
# Waervyn's World https://www.youtube.com/watch?v=owmorwxSjvA


import math, sys, os

abspath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abspath + '/module')
from gem_tools import gem_tools

tools = gem_tools(keyboard, system, time, mouse, store)

print("Core Farmer")

startloops = 2
endloops = 8
breakAtEnd = True


def runStart():
    print("set up traits")
    tools.tinySleep()
    time.sleep(5)
    tools.xte_click(800, 917)
    tools.trait(1, 2)
    tools.trait(3, 3)
    # Looming is good for getting cores.
    tools.xte_click(435, 325)
    tools.tinySleep()
    tools.xte_click(1147, 923)
    time.sleep(8)


def runLoop():
    laginess = 0
    tools.tinySleep()
    mouse.click_relative(964, 548, 1)
    time.sleep(5)
    mouse.click_relative(1147, 923, 1)
    time.sleep(8)


def buildKillgem(q=5):
    tools.getGem(8, q)
    tools.getGem(1, q)
    tools.combine(1, q, 2, q)
    tools.getGem(4, 1)
    tools.combine(1, 1, 2, q)


def send_it(nr):
    y = 75 + 185 * nr
    tools.xte(" 'mousemove 40 " + str(y) + "' 'mouseclick 1'")
    tools.tinySleep()


def ups():
    tools.ugradeGem(24, 10, 1)
    tools.ugradeGem(22, 10, 1)
    tools.ugradeGem(22, 8, 1)
    tools.ugradeGem(24, 8, 1)
    tools.ugradeGem(26, 8, 1)
    tools.ugradeGem(26, 10, 1)


def delete_talisman():
    print("delete_talisman")
    time.sleep(4)
    tools.xte_click(1719, 234)
    time.sleep(4)
    for x in range(6):
        for y in range(4):
            x1 = 1265 + x * 90
            y1 = 460 + y * 90
            command = " 'mousemove " + str(x1) + " " + str(y1) + "' 'usleep 100'"
            command += " 'keydown x' 'usleep 100' 'keyup x' 'usleep 100'"
            tools.xte(command)
    time.sleep(2)
    tools.tinySleep()
    tools.xte_click(1706, 976)
    tools.tinySleep()
    time.sleep(2)


def start_fast():
    command = " 'usleep 200000'"
    command += " 'keydown Control_L'"
    command += " 'usleep 100000'"
    command += " 'mousemove 31 886' 'usleep 200000' 'mouseclick 1'"
    command += " 'usleep 200000'"
    command += " 'keyup Control_L'"
    command += " 'usleep 100000'"
    tools.xte(command)
    time.sleep(2)
    mouse.click_relative(157, 45, 1)


def main_run():
    global endloops
    global startloops
    global talis
    time.sleep(2)
    tools.tinySleep()
    tools.grid_drag(24, 10, 27, 26)
    buildKillgem()
    tools.grid_click(24, 10)
    tools.amp(22, 10, 8, 1)
    tools.amp(22, 8, 8, 1)
    tools.amp(24, 8, 8, 1)
    tools.amp(26, 8, 8, 1)
    tools.amp(26, 10, 8, 1)
    ups()
    ups()
    tools.tinySleep()
    time.sleep(2)

    command = " 'mousemove 789 395' 'usleep 200000' 'mousedown 3'"
    command += " 'sleep 1'"
    command += " 'mousemove 704 474' 'usleep 200000' 'mouseup 3'"
    tools.xte(command)
    time.sleep(2)

    start_fast()

    for i in range(startloops):
        tools.tinySleep()
        time.sleep(5)
        ups()
    time.sleep(10)
    tools.tinySleep()

    tools.xte_click(979, 979)

    time.sleep(5)
    start_fast()

    for i in range(endloops):
        tools.tinySleep()
        time.sleep(5)
        ups()

    time.sleep(10)

    if breakAtEnd:
        # End the Endurance-Mode if it is still running
        tools.xte_click(1885, 30)
        time.sleep(1)
        tools.xte_click(1047, 972)
        tools.tinySleep()
        tools.xte_click(1047, 972)
        time.sleep(1)
        tools.xte_click(1550, 953)
        time.sleep(2)

    tools.xte_click(1680, 984)

    time.sleep(6)
    tools.tinySleep()

    talis += 1
    if talis == 2:
        delete_talisman()
        talis = 0

    tools.xte_click(960, 548)

    time.sleep(4)
    tools.tinySleep()
    tools.xte_click(1148, 922)
    time.sleep(8)
    tools.tinySleep()


# delete_talisman()
talis = 0
runStart()
while not store.GLOBALS.get("STOP", False):
    main_run()
store.set_global_value("STOP", False)
print("ende")

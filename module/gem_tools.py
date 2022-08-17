#!/usr/bin/autokey
# -*- coding: utf-8 -*-
""" Collection of the most important functions for Gemcraft

Usage:
In AutoKey, using include is problematic. However, the following workaround works:

abspath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abspath + '/module')
from gem_tools import gem_tools
tools = gem_tools(keyboard, system, time, mouse, store)

"""
__author__ = "Harald Stowasser"
__copyright__ = "2022 Harald Stowasser"
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = "Harald Stowasser"
__email__ = "harald@stowasser.tv"
__status__ = "Production"


class gem_tools:
    """the most important functions for Gemcraft

    Args:
        keyboard :Standard module in AutoKey
        system :Standard module in AutoKey
        time :Standard module in AutoKey
        mouse :Standard module in AutoKey
        store :Standard module in AutoKey
    Attributes:
        lag_delay  (float): Gemcraft sometimes becomes very slow when there are many enemies on screen.
            This value can then be increased to adjust any waiting times.
        stop_counter (int): The number of starts and stops is counted. A program will only continue if exactly the same
            number of starts follow stops. Thus, subfunctions can use Start and Stop without the risk of starting the
            program prematurely.
        bomb_count (int): The number of bombs used to anger the monsters is remembered here. So that this value can be
            automatically adjusted during the run.
        end_script (boolean): This variable can be used (like store.GLOBALS["STOP"]) to terminate the program prematurely.
    """
    def __init__(self, keyboard, system, time, mouse, store):
        self.lag_delay = 0
        self.stop_counter = 0
        self.bomb_count = 1
        self.end_script = False
        self.keyboard = keyboard
        self.system = system
        self.time = time
        self.mouse = mouse
        self.store = store
        self.store.set_global_value("STOP", False)

    def amp(self, x, y, kb, quali):
        self.keyboard.send_keys("a")
        self.grid_click(x, y)
        self.getGem(kb, quali, 1)
        self.grid_click(x, y)

    def checkend(self):
        if self.end_script or self.store.GLOBALS.get("STOP", False):
            # Reset the global variable, otherwise the next script will be aborted immediately.
            self.store.set_global_value("STOP", False)
            print("Stop is called... exiting")
            self.stope()
            exit(1)

    def calcGrid(self, x, y):
        return 85 + (x - 1) * 30, 110 + (y - 1) * 30

    def calcGem(self, x, y):
        return 1760 + (x - 1) * 50, 830 - (y - 1) * 50

    def combine(self, x, y, xx, yy):
        self.tinySleep()
        self.keyboard.send_keys("g")
        x1, y1 = self.calcGem(x, y)
        xx1, yy1 = self.calcGem(xx, yy)
        self.tinySleep()
        self.drag(x1, y1, xx1, yy1)

    def drag(self, x, y, xx, yy):
        command = " 'mousemove " + str(x) + " " + str(y) + "' 'mousedown 1'"
        command += " 'mousemove " + str(xx) + " " + str(yy) + "' 'mouseup 1'"
        self.xte(command)

    def drag_stash2grid(self, sx, sy, gx, gy):
        x2, y2 = self.calcGem(sx, sy)
        xx2, yy2 = self.calcGrid(gx, gy)
        self.drag(x2, y2, xx2, yy2)

    def drag_stash(self, x, y, xx, yy):
        # print("self.drag_stash {} {} > {} {}".format(x, y, xx, yy))
        self.tinySleep()
        x1, y1 = self.calcGem(x, y)
        xx1, yy1 = self.calcGem(xx, yy)
        self.drag(x1, y1, xx1, yy1)

    def dup(self, x, y, xx, yy):
        self.keyboard.send_keys("r")
        self.grid_click(xx, yy)
        self.dup_grid(x, y)
        # self.drag_stash2grid(3,1, xx,yy)
        self.grid_click(xx, yy)

    def dup_grid(self, x, y):
        x2, y2 = self.calcGrid(x, y)
        self.tinySleep()
        command = " 'mousemove " + str(x2) + " " + str(y2) + "'"
        self.xte(command)
        self.keyboard.send_keys("d")

    def fastBomb(self, quali=5, send=True, nr=5):
        self.tinySleep()
        self.stope()
        self.tinySleep()
        s = " 'usleep 400000'"
        self.getGem(7, 1, 1)
        command = "'key b'"
        while quali > self.bomb_count:
            command += s + " 'key Up'"
            self.bomb_count += 1
        while quali < self.bomb_count:
            command += s + " 'key Down'"
            self.bomb_count -= 1
        self.tinySleep()
        command += s + " 'keydown Shift_L'"
        y = 1000
        for i in range(nr):
            command += s + " 'mousemove 40 " + str(y) + "'" + s + " 'mouseclick 1'"
            y -= 185
        command += s + " 'keyup Shift_L'"
        if send:
            command += s + " 'mousemove 40 1000'" + s + "  'mouseclick 1'"
        command += s + " 'mousemove 1760 828'" + s + " 'key x'"
        self.xte(command)
        self.starte()

    def grid_drag(self, x, y, xx, yy):
        x2, y2 = self.calcGrid(x, y)
        xx2, yy2 = self.calcGrid(xx, yy)
        self.drag(x2, y2, xx2, yy2)

    def grid_click(self, x, y):
        self.tinySleep()
        x2, y2 = self.calcGrid(x, y)
        self.xte(" 'mousemove " + str(x2) + " " + str(y2) + "' 'usleep 20000' 'mouseclick 1'")
        self.tinySleep()

    def getGem(self, kb, quali, quanti=1):
        keycodes = ("87", "88", "89", "83", "84", "85", "79", "80", "81")
        for i in range(quanti):
            self.keyboard.send_keys("<numlock>+<code" + keycodes[kb - 1] + ">")
            x1, y1 = self.calcGem(1, quali)
            self.mouse.click_relative(x1, y1, 1)
            self.tinySleep()

    def starte(self, ):
        # print("***** Starte ")
        self.tinySleep()
        if self.stop_counter == 0:
            self.mouse.click_relative(112, 42, 1)
            # print("  start");
        else:
            pass
            # print("  stopcount=" + str(self.stopcounter));
        self.tinySleep()
        self.stop_counter += 1

    def stope(self):
        # print("Stope  *****")
        # print("  stopcount=" + str(self.stopcounter));
        self.tinySleep()
        self.mouse.click_relative(41, 46, 1)
        self.tinySleep()
        self.stop_counter -= 1

    def tinySleep(self):
        self.time.sleep(0.05 + self.lag_delay)
        self.checkend()

    def trait(self, x, y, nr=7):
        for i in range(nr):
            self.mouse.click_relative(490 + (x - 1) * 300, 430 + (y - 1) * 155, 1)
            self.tinySleep()
        self.time.sleep(0.5)

    def tower(self, x, y, kb, quali):
        self.keyboard.send_keys("t")
        self.grid_click(x, y)
        self.getGem(kb, quali, 1)
        self.grid_click(x, y)

    def ugradeGem(self, x, y, nr, inject=False):
        x2, y2 = self.calcGrid(x, y)
        self.xte("'mousemove " + str(x2) + " " + str(y2) + "'")
        for i in range(nr):
            self.keyboard.send_keys("u")
            self.time.sleep(0.05)
        if inject:
            self.keyboard.send_keys(inject)
            self.tinySleep()

    def wall(self, x, y):
        self.keyboard.send_keys("w")
        self.grid_click(x, y)

    def walls(self, x, y, xx, yy):
        self.keyboard.send_keys("w")
        self.grid_drag(x, y, xx, yy)

    def xte(self, command):
        # print(command)
        self.tinySleep()
        dummy_string = "" + self.system.exec_command("xte " + command + " && echo 'done'", True)
        self.tinySleep()
        return dummy_string

    def prtest(self):
        print("text")

    def xte_click(self, x, y):
        self.xte(" 'mousemove " + str(x) + " " + str(y) + "' 'usleep 100000' 'mouseclick 1'")

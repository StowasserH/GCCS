#!/usr/bin/autokey
"""This script builds gems """
import sys, os

__author__ = "harald@stowasser.tv"
__copyright__ = "MIT"

abspath = os.path.abspath(os.path.dirname(__file__))
sys.path.append(abspath + '/module')
from gem_tools import gem_tools

print("Build Gems")

tools = gem_tools(keyboard, system, time, mouse, store)


def makegem(word):
    kb = 0
    quali = 1
    print("make " + word)
    if "o" in word:
        kb = 7
    elif "r" in word:
        kb = 4
    elif "y" in word:
        kb = 8
    elif "b" in word:
        kb = 1
    if word[0] in "123456789":
        quali = int(word[0])
    tools.getGem(kb, quali)
    return quali


def stackpos(nr):
    return (nr % 3) + 1, 12 - int(nr / 3)


# "2o+o+o+o+o+o+2o+(2o+b)
def parseGem(input, start_stack=0):
    global lst_quali
    commands = "()+"
    # I will not check the screen if a gem is allread in the position
    # So I will use this array to remember.
    stack_emty = [True]
    stack = start_stack
    word = ""
    for letter in input + "+":
        tools.checkend()
        if letter not in commands:
            word += letter
        else:
            if word:
                line = makegem(word)
                x, y = stackpos(stack)
                if stack_emty[stack - start_stack]:
                    tools.drag_stash(1, line, x, y)
                    stack_emty[stack - start_stack] = False
                else:
                    tools.combine(1, line, x, y)
                word = ""
            if letter == "(":
                stack += 1
                stack_emty.append(True)
            elif letter == ")":
                x, y = stackpos(stack)
                stack -= 1
                xx, yy = stackpos(stack)
                if stack_emty[stack - start_stack]:
                    tools.drag_stash(x, y, xx, yy)
                    stack_emty[stack - start_stack] = False
                else:
                    tools.combine(x, y, xx, yy)
                stack_emty.pop()
            elif letter == "+":
                pass


mana32 = "2o+o+o+o+o+o+2o+(2o+b)+(2o+(o+r)+b+2b)+(2b+b+b+b+b+2b+(2o+b+2b))"
mana_amp6 = "2o+o+o+2o"
mana_amp32 = "2o+o+o+o+o+o+2o+2o+(2o+o+2o)"
mana_amp32_2 = "2o+o+o+o+o+o+o+(2o+o)+(2o+o+2o)"
kill32 = "2b+b+b+2b+2b+(2b+b)+(rb+y+b+(2b+b))+(2y+y+y+yb+(yb+b)+(yb+b+2b))"
kill_amp6 = "2y"
kill_amp32 = "2y+y+y+y+2y+(2y+2y)"
# hä?kill16="2k+k+k+k+k+2k+(2k+k)+(2k+k+2k)"
mana64 = "(((2o+o+o+o+o+o+o+(2o+o)+(2o+o)+(2o+o+o+(o+b))+(2o+o+(o+b)+b))+"
mana64 += "(2o+o+o+(o+r+b)+b+(o+b+b+2b)))+"
mana64 += "(2b+b+b+b+b+2b+(o+b+b+2b)+"
mana64 += "(2o+o+o+(o+b)+b+(o+b+b+2b))))"
mana128 = "((((2o+o+o+o+o+o+o+(2o+o)+(2o+o)+(2o+o+o)+(2o+o+o+o)+(2o+o+o+o+o+(2o+b)))+"
mana128 += "(2o+o+o+o+o+(2o+b)+(2o+b+2b)))+"
mana128 += "((2o+o+o+o+o+o+(2o+b)+(2o+b+2b))+"
mana128 += "((2b+b+b+2b)+(2o+b+2b))))+"
mana128 += "((((2b+b+b+b+b+2b+2b+(2b+b))+(2b+b+b+2b))+"
mana128 += "(2b+b+b+2b+((2o+b)+2b)))+"
mana128 += "(((2o+o+o+o+o+o+(2o+b))+(2o+b+2b))+"
mana128 += "((2b+b+b+2b)+(2o+b+2b)))))"

kill64 = "(((((((((2b+b)+b)+b)+2b)+(2b+b))+((2b+b)+b))+"
kill64 += "(((2b+b)+b)+((y+b)+b)))+"
kill64 += "((((2b+b)+b)+((y+b)+b))+"
kill64 += "((2y+b)+((y+b)+b))))+"
kill64 += "(((((((2y+y)+y)+2y)+((y+r)+y))+(2y+b))+"
kill64 += "((2y+b)+((y+b)+b)))+"
kill64 += "((((2b+b)+b)+((y+b)+b))+"
kill64 += "((2y+(y+b))+b))))"

time.sleep(2)
parseGem(mana64)
parseGem(mana_amp32, 1)
parseGem(kill64, 2)
parseGem(kill_amp32, 3)

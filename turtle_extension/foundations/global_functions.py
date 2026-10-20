from time import sleep as rest
from turtle import TurtleGraphicsError
from typing import Final

import uf

from ..turtle_heart import ChainTurtle, tl
from .global_variables import UV, t_shape

_screen = None

#* Retrieves the turtle screen [[turtle.py#Screen]] if one has been made,
#* else, a new screen is initialized
def get_screen():
    global _screen

    if _screen is None:
        _screen = tl.Screen()
        _screen.getcanvas().winfo_toplevel().state("zoomed")
        _screen.tracer(0)

    return _screen

#* Updates the current turtle screen if one exists,
#* else a new one is created and updated
def SU():
    get_screen().update()

#* Keeps the turtle window open if one exists,
#* else a new one is created and kept open
def mainloop():
    get_screen().mainloop()

#* Creates a chosen number of turtles with different modes,
#* also known as the turtle factory by the developer
def tls_color(**options):

    tl_num_name: Final = "tl_num"
    entry_name: Final = "entry"
    index_name: Final = "index"

    if tl_num_name in options:
        tl_num = options[tl_num_name]
        uf.int_validate()(tl_num, tl_num_name)
        uf.Positive()(tl_num, tl_num_name)
        turtles_num_count = tl_num

    elif entry_name in options:
        entry = options[entry_name]
        uf.str_validate()(entry, entry_name)
        turtles_num_count = uf.get_num(int, entry, MIN=1)

    elif index_name in options:
        index = options[index_name]
        uf.int_validate()(index, index_name)
        uf.Positive()(index, index_name)
        turtles_num_count = index
    else:
        print("NONE of the entered options exist!")
        return None

    tls: list[ChainTurtle] = []

    for color_num in range(turtles_num_count):
        while True:
            color_iteration: str = input(f"Enter turtle color {color_num + 1}: ")
            try:
                turtle: ChainTurtle = ChainTurtle().color(color_iteration).shape(t_shape())
                if index_name in options:
                    UV["tls"].append(turtle)
                else:
                    tls.append(turtle)
                break

            except TurtleGraphicsError:
                print("Enter a VALID color!"); rest(2)

    if index_name in options:
        return len(UV["tls"]) - 1

    elif entry_name in options:
        return tls, turtles_num_count

    elif tl_num_name in options:
        return tls
    return None

#* Resets the provided turtle list,
#* deletes all turtle drawings and the turtles themselves
def reset_tls(tls_list):

    tls_list_name: Final = "tls_list"
    uf.TypeValidate(list)(tls_list, name=tls_list_name)
    uf.SequenceValidate(ChainTurtle, ...)(tls_list, name=tls_list_name)

    for t in tls_list:
        t.clear().ht()
    tls_list.clear()
    return tls_list
# ⚓ Anchor for this module: [[global-functions-anchor|global_functions.py]] 

import turtle as turtles
import typing as tp
from time import sleep as rest

import uf

from .. import turtle_heart as tls_heart
from . import global_variables as glb_var

_screen = None


# ⚓ get_screen anchor: [[get-screen-anchor|get_screen()]] 
#* 📝 Retrieves the turtle screen [[turtle.py#Screen]] if one has been made,
#* 📝 else, a new screen is initialized
def get_screen():
    global _screen

    if _screen is None:
        _screen = tls_heart.tl.Screen()
        _screen.getcanvas().winfo_toplevel().state("zoomed")
        _screen.tracer(0)

    return _screen


# ⚓ SU anchor: [[SU-anchor|SU()]] 
 #* 📝 Updates the current turtle screen if one exists,
 #* 📝 else a new one is created and updated
def SU():
    get_screen().update()


# ⚓ mainloop anchor: [[mainloop-anchor|mainloop()]] 
 #* 📝 Keeps the turtle window open if one exists,
 #* 📝 else a new one is created and kept open
def mainloop():
    get_screen().mainloop()


# ⚓ tls_color anchor: [[tls-color-anchor|tls_color()]] 
 #* 📝 Creates a chosen number of turtles with different modes,
 #* 📝 also known as the turtle factory by the developer
def tls_color(**options):

    tl_num_name: tp.Final = "tl_num"
    entry_name: tp.Final = "entry"
    index_name: tp.Final = "index"

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

    tls: list[tls_heart.ChainTurtle] = []

    for color_num in range(turtles_num_count):

        while True:
            color_iteration: str = input(f"Enter turtle color {color_num + 1}: ")

            try:
                turtle: tls_heart.ChainTurtle = (
                    tls_heart.ChainTurtle()
                    .color(color_iteration)
                    .shape(glb_var.t_shape())
                )
                if index_name in options:
                    glb_var.UV["tls"].append(turtle)

                else:
                    tls.append(turtle)

                break

            except turtles.TurtleGraphicsError:
                print("Enter a VALID color!")
                rest(2)

    if index_name in options:
        return len(glb_var.UV["tls"]) - 1

    elif entry_name in options:
        return tls, turtles_num_count

    elif tl_num_name in options:
        return tls
    
    return None


# ⚓ reset_tls anchor: [[reset-tls-anchor|reset_tls()]] 
#* 📝 Resets the provided turtle list,
#* 📝 deletes all turtle drawings and the turtles themselves
def reset_tls(tls_list):

    tls_list_name: tp.Final = "tls_list"
    
    uf.TypeValidate(list)(tls_list, name=tls_list_name)
    uf.SequenceValidate(tls_heart.ChainTurtle, ...)(tls_list, name=tls_list_name)

    for t in tls_list:
        t.clear().ht()
    tls_list.clear()

    return tls_list
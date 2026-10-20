"""
This package is part of the GeometricalDomination project ecosystem.

It contains a chainable turtle class called ChainTurtle and a collection of extra provided features along with it:

1. tls_color -> this function make a list of colored turtles and returns it
2. get_screen -> turtle screen initializer function
3. SU -> screen update function

And a lot more.

Author: Miah M. Sabiq
"""

#* Imports foundational functions across numerous files
from .foundations import (
   CUSTOM_SHAPES,       #* [[custom_turtle_shapes.py]]
   get_UserShape_dict,  #* [[custom_turtle_shapes.py#get_UserShape_dict]]

   get_screen,          #* [[global_functions.py#get_screen]]
   mainloop,            #* [[global_functions.py#mainloop]]
   reset_tls,           #* [[global_functions.py#reset_tls]]
   SU,                  #* [[global_functions.py#SU]]
   tls_color,           #* [[global_functions.py#tls_color]]

   t_now,               #* [[global_variables.py#t_now]]
   t_shape,             #* [[global_variables.py#t_shape]]
   UV,                  #* [[global_variables.py]]

   TurtleFct,           #* [[TurtleFct]]
   UserShape,           #* [[UserShape]]
)

#* Imports core mechanisms of this package:
#*  [[ChainTurtle]] and [[turtle.py]] from [[turtle_skeleton.py]]
from .turtle_heart import (
   ChainTurtle,         #* [[ChainTurtle]]
   tl,                  #* [[turtle.py]]
)


#* Specifies all available functions and dictionaries through wild card import
__all__ = [
    "UV",
    "t_now",
    "t_shape",

    "get_screen",
    "SU",
    "mainloop",
    "tls_color",
    "reset_tls",

    "UserShape",
    "get_UserShape_dict",
    "CUSTOM_SHAPES",

    "TurtleFct",


   "ChainTurtle",
   "tl",
]
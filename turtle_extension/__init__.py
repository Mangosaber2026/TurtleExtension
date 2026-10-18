"""
This package is part of the GeometricalDomination project ecosystem.

It contains a chainable turtle class called ChainTurtle and a collection of extra provided features along with it:

1. tls_color -> this function make a list of colored turtles and returns it
2. get_screen -> turtle screen initializer function
3. SU -> screen update function

And a lot more.

Author: Miah M. Sabiq
"""

from .foundations import (
   CUSTOM_SHAPES,
   SU,
   UV,
   TurtleFct,
   UserShape,
   get_screen,
   get_UserShape_dict,
   mainloop,
   reset_tls,
   t_now,
   t_shape,
   tls_color,
)
from .turtle_heart import (
   ChainTurtle,
   tl,
)

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
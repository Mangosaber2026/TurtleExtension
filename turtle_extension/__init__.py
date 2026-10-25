"""
This package is part of the GeometricalDomination project ecosystem.

It contains a chainable turtle class called ChainTurtle and a collection of extra provided features along with it:

1. tls_color -> this function make a list of colored turtles and returns it
2. get_screen -> turtle screen initializer function
3. SU -> screen update function

And a lot more.

Author: Miah M. Sabiq
"""

 #* 📝 Imports foundational functions across numerous files
from .foundations import (  # noqa: I001
   CUSTOM_SHAPES,        
   # 🔗 Link to source code: [[#CUSTOM-SHAPES-anchor|dictionary CUSTOM_SHAPES]] 
   get_UserShape_dict,   
   # 🔗 Link to source code: [[#get-UserShape-dict-anchor|get_UserShape_dict()]] 
   get_screen,           
   # 🔗 Link to source code: [[#get-screen-anchor|get_screen()]] 
   mainloop,             
   # 🔗 Link to source code: [[#mainloop-anchor|mainloop()]] 
   reset_tls,            
   # 🔗 Link to source code: [[#reset-tls-anchor|reset_tls()]] 
   SU,                   
   # 🔗 Link to source code: [[#SU-anchor|SU()]] 
   tls_color,            
   # 🔗 Link to source code: [[#tls-color-anchor|tls_color()]] 

   t_now,                
   # 🔗 Link to source code: [[#t-now-anchor|t_now()]] 
   t_shape,              
   # 🔗 Link to source code: [[#t-shape-anchor|t_shape()]] 
   UV,                   
   # 🔗 Link to source code: [[#UV-anchor|dictionary UV]] 

   TurtleFct,           
   # 🔗 Link to source code: [[#TurtleFct-anchor|class TurtleFct]] 
   UserShape,            
   # 🔗 Link to source code: [[#UserShape-anchor|class UserShape]] 
)

 #* 📝 Imports core mechanisms of this package:
 #* 📝 [[#ChainTurtle-anchor|ChainTurtle]] and turtle.py from [[#turtle-skeleton-anchor|turtle_skeleton.py]] 
from .turtle_heart import (
   ChainTurtle,          
   # 🔗 Link to source code: [[#ChainTurtle-anchor|class ChainTurtle]] 
   tl,                   
)


 #* 📝 Specifies all available functions and dictionaries through wild card import
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
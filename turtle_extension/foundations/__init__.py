# ⚓ Anchor for this module: [[foundations-anchor|foundations.__init__.py]] 


#* 📝 Imports function, class and dictionary from [[#custom-turtle-shapes-anchor|custom_turtle_shapes.py]] 
from .custom_turtle_shapes import (  # noqa: I001
    CUSTOM_SHAPES,
    # 🔗 Link to source code: [[#CUSTOM-SHAPES-anchor|constant CUSTOM_SHAPES]] 
    UserShape,
    # 🔗 Link to source code: [[#UserShape-anchor|class UserShape]] 
    get_UserShape_dict,
    # 🔗 Link to source code: [[#get-UserShape-dict-anchor|get_UserShape_dict()]] 
)

#* 📝 Imports fundamental turtle functions from [[#global-functions-anchor|global_functions.py]] 
from .global_functions import (
    SU,
    # 🔗 Link to source code: [[#SU-anchor|SU()]] 
    get_screen,
    # 🔗 Link to source code: [[#get-screen-anchor|get_screen()]] 
    mainloop,
    # 🔗 Link to source code: [[#mainloop-anchor|mainloop()]] 
    reset_tls,
    # 🔗 Link to source code: [[#reset-tls-anchor|reset_tls()]] 
    tls_color,
    # 🔗 Link to source code: [[#tls-color-anchor|tls_color()]] 
)

#* 📝 Imports universal dictionary and related functions from [[#global-variables-anchor|global_variables.py]] 
from .global_variables import (
    UV,
    # 🔗 Link to source code: [[#UV-anchor|dictionary UV]]  
    t_now,
    # 🔗 Link to source code: [[#t-now-anchor|t_now()]] 
    t_shape,
    # 🔗 Link to source code: [[#t-shape-anchor|t_shape()]] 
)

#* 📝 Imports class from [[#turtle-functions-anchor|turtle_functions.py]]
from .turtle_functions import (
    TurtleFct,
    # 🔗 Link to source code: [[#TurtleFct-anchor|class TurtleFct]] 
)


#* 📝 Specifies functions, classes, and dictionaries available in foundations package
#* 📝 through wild card import
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
]
#* Imports function, class and dictionary from [[custom_turtle_shapes.py]]
from .custom_turtle_shapes import (
    CUSTOM_SHAPES,
    UserShape,
    get_UserShape_dict,
)

#* Imports fundamental turtle functions from [[global_functions.py]]
from .global_functions import (
    SU,
    get_screen,
    mainloop,
    reset_tls,
    tls_color,
)

#* Imports universal dictionary and related functions from [[global_variables.py]]
from .global_variables import (
    UV,
    t_now,
    t_shape,
)

#* Imports class from [[turtle_functions.py]]
from .turtle_functions import (
    TurtleFct,
)


#* Specifies functions, classes, and dictionaries available in foundations package
#* through wild card import
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
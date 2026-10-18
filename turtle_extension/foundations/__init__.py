from .custom_turtle_shapes import (
    CUSTOM_SHAPES,
    UserShape,
    get_UserShape_dict,
)
from .global_functions import (
    SU,
    get_screen,
    mainloop,
    reset_tls,
    tls_color,
)
from .global_variables import (
    UV,
    t_now,
    t_shape,
)
from .turtle_functions import (
    TurtleFct,
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
]
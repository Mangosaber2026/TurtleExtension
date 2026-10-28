"""
This module contains a dictionary (UV) which contains important info about turtles and user_drawing_ft().

Other functions:

t_now() -> lets users take the current UV turtle

t_shape() -> lets users take the current turtle shape
"""
 #* 📝 File type: Python type stub (.pyi)
 #* 📝 Purpose: Describes the module's interface for documentation,
 #* 📝         editor support, and static type checking.
 #* 📝 Runtime: Contains no implementation; see the corresponding
 #* 📝         .py file for executable code.

from typing import Any  # noqa: I001

from .. import turtle_heart as tls_heart 


 #* 📝 The type for the UV dictionary
UV: dict[str, Any]

def t_now() -> tls_heart.ChainTurtle:
    """
    This function returns the current UV turtle

    >>> turtle = ChainTurtle()
    >>> UV["tls"].append(turtle)
    >>> t_now()
    ChainTurtle()

    :return: ChainTurtle
    """

def t_shape() -> str:
    """
    This function returns the current UV turtle shape

    >>> UV['tls_shape'] = 'turtle'
    >>> t_shape()
    'turtle'

    :return: string
    """

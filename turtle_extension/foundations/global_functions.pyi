"""
This module contains a very useful function: tls_color, which lets the user create any number of turtles with
colors and get a list with them.
"""

import turtle as tls  # noqa: I001

from .. import turtle_heart as tls_heart


def get_screen() -> tls._Screen:
    """
    Initiates the turtle screen when the function is called.

    :return: turtle screen object
    """

def SU() -> None:
    """
    This function updates the turtle screen.

    :return: None
    """

def mainloop() -> None:
    """
    This function keeps the turtle screen open.

    :return: None
    """

type TurtleListType = list[tls_heart.ChainTurtle]

def tls_color(**options) -> int | tuple[TurtleListType, int] | TurtleListType | None:
    """
    This function creates a turtle list with their colors or adds newly creates turtles to the UV["tls"] list
    to be used for the user_drawing_ft()

    USERS NOTICE: it is HIGHLY recommended to NOT enter a turtles count of MORE than a few hundred (max. 200) unless required!!!

    :param options: tl_num -> number of turtles to create, entry -> input string, index -> number of turtles to be created for user_drawing_ft()
    & it returns the index of the last turtle

    :return: tls_num: turtle list with colored turtles, entry: list with colored turtles + number of turtles ,otherwise: index of last turtle
    """

def reset_tls(tls_list: TurtleListType) -> list:
    """
    This function deletes the drawings of given turtle list + turtles

    >>> tls = [ChainTurtle(), ChainTurtle()]
    
    >>> reset_tls(tls)
    []

    :return: empty tls_list
    """
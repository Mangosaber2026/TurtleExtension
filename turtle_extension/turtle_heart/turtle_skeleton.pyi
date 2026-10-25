"""
This module contains the class ChainTurtle() which is the foundational object around which this entire software has been made.
"""

import turtle  # noqa: I001
from collections.abc import Callable
from numbers import Real
import typing as tp


tl = turtle

class ChainTurtle(tl.Turtle):
    """
    This class adds chaining functionality to turtle.Turtle
    
    """
    @tp.override
    def forward(self, distance: Real) -> ChainTurtle: ...

    fd = forward

    def fd_inv(self, distance: Real) -> ChainTurtle:
        """
        Makes the turtle go forward with no trace.

        :param distance: distance in pixels

        :return: ChainTurtle()
        """

    @tp.override
    def backward(self, distance: Real) -> ChainTurtle: ...

    bk = backward
    back = backward     # type: ignore

    def bk_inv(self, distance: Real) -> ChainTurtle:
        """
        Makes the turtle go backward with no trace.

        :param distance: distance in pixels

        :return: ChainTurtle()
        """

    @tp.override
    def right(self, angle: Real) -> ChainTurtle: ...

    rt = right

    @tp.override
    def left(self, angle: Real) -> ChainTurtle: ...

    lt = left

    @tp.override
    def goto(self, x_val: Real, y_val: Real) -> ChainTurtle: ...

    setpos = goto
    setposition = goto

    @tp.override
    def penup(self) -> ChainTurtle: ...

    pu = penup
    up = penup

    @tp.override
    def pendown(self) -> ChainTurtle: ...

    pd = pendown
    down = pendown

    @tp.override
    def setheading(self, direction: Real) -> ChainTurtle: ...

    @tp.override
    def home(self) -> ChainTurtle: ...

    def home_inv(self) -> ChainTurtle:
        """
        Sets the position of the turtle to home (0, 0) without trace, heading = 0 .

        :return: ChainTurtle()
        """

    @tp.override
    def begin_fill(self) -> ChainTurtle: ...

    @tp.override
    def end_fill(self) -> ChainTurtle: ...

    @tp.override
    def circle(self,
               radius: Real,
               extent: Real | None = None,
               steps: int | None = None) -> ChainTurtle:
        """
        Makes the turtle draw a circle

        :param radius: radius in pixels

        :param extent: angle to be drawn in degrees, default = full circle

        :param steps: number of straight-line segments used to approximate the arc

        :return: ChainTurtle()
        """

    def circle_fill(self,
                    radius: Real,
                    angle: Real | None = None,
                    sides: int | None = None) -> ChainTurtle:
        """
        Makes the turtle draw a circle and fills it

        :param radius: radius in degrees

        :param angle: angle in degrees

        :param sides: number of sides

        :return: ChainTurtle()
        """

    @tp.override
    def dot(self, radius: Real) -> ChainTurtle: ...

    @tp.overload
    def color(self, turtle_color: str) -> ChainTurtle:
        """
        Lets the user change the color of the turtle's trace and the turtle's fill

        :param turtle_color: a valid turtle color

        :return: ChainTurtle()
        """

    @tp.overload
    def color(self, turtle_color: None = None) -> str:
        """
        Lets the user retrieve the current turtle's color

        :return: current turtle color -> str
        """

    @tp.override
    def teleport(self, x: Real, y: Real, *, fill_gap: bool = False) -> ChainTurtle:
        """
        Makes the turtle to go a specific coordinate with no trace

        :param x: horizontal (x) position in pixels

        :param y: vertical (y) position in pixels

        :return: ChainTurtle()
        """
    @tp.overload
    def shape(self, shape_name: str) -> ChainTurtle: ...

    @tp.overload
    def shape(self) -> str: ...

    @tp.override
    def undo(self) -> ChainTurtle: ...

    @tp.override
    def clear(self) -> ChainTurtle: ...

    @tp.override
    def hideturtle(self) -> ChainTurtle: ...

    ht = hideturtle

    @tp.override
    def showturtle(self) -> ChainTurtle: ...

    @tp.override
    def begin_poly(self) -> ChainTurtle: ...

    @tp.override
    def end_poly(self) -> ChainTurtle:  ...

    @tp.override
    def get_poly(self) -> tp.Sequence[tuple[float, float]] | None: ...

    @classmethod
    def list_methods(cls) -> dict[str, Callable]:
        """
        Creates a dictionary with all ChainTurtle methods and returns it
        
        :return: dictionary
        """
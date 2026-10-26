# ⚓ Anchor for this module: [[turtle-skeleton-anchor|turtle_skeleton.py]] 

import turtle as tl
import typing as tp

import uf


# ⚓ ChainTurtle anchor: [[ChainTurtle-anchor|class ChainTurtle]] 
 #* 📝 Class for chaining the conventional turtle functions
class ChainTurtle(tl.Turtle):

    # ⚓ fd anchor: [[ChainTurtle-forward-anchor|forward()]] 
    #* 📝 Moves the turtle forward
    @tp.override
    def forward(self, distance):
        super().fd(distance)
        return self

    fd = forward


    # ⚓ fd_inv anchor: [[ChainTurtle-fd-inv-anchor|fd_inv()]] 
    #* 📝 Moves the turtle forward invisibly
    def fd_inv(self, distance):

        was_down = self.isdown()
        self.pu().fd(distance)

        if was_down:
            self.pd()

        return self
    

    # ⚓ anchor: [[ChainTurtle-backward-anchor|backward()]] 
    #* 📝 Moves the turtle backward
    @tp.override
    def backward(self, distance):
        super().bk(distance)
        return self

    bk = backward
    back = backward     # type: ignore[ReportAssignmentType]


    # ⚓ anchor: [[ChainTurtle-bk-inv-anchor|bk_inv]] 
    #* 📝 Moves the turtle backward invisibly
    def bk_inv(self, distance):

        was_down = self.isdown()
        self.pu().bk(distance)

        if was_down:
            self.pd()

        return self


    # ⚓ anchor: [[ChainTurtle-right-anchor|right()]] 
    #* 📝 Turns the turtle to the right
    @tp.override
    def right(self, angle):
        super().rt(angle)
        return self

    rt = right


    # ⚓ anchor: [[ChainTurtle-left-anchor|left()]] 
    #* 📝 Turns the turtle to the left
    @tp.override
    def left(self, angle):
        super().lt(angle)
        return self

    lt = left


    # ⚓ anchor: [[ChainTurtle-goto-anchor|goto()]] 
    #* 📝 Makes the turtle go to a specific coordinate
    @tp.override
    def goto(self, x_val, y_val):
        super().setpos(x_val, y_val)
        return self

    setpos = goto
    setposition = goto


    # ⚓ anchor: [[ChainTurtle-penup-anchor|penup()]] 
    #* 📝 Lifts up the pen, turtle stops drawing
    @tp.override
    def penup(self):
        super().pu()
        return self

    pu = penup
    up = penup


    # ⚓ anchor: [[ChainTurtle-pendown-anchor|pendown()]] 
    #* 📝 Puts the pen down, turtle starts drawing
    @tp.override
    def pendown(self):
        super().pd()
        return self

    pd = pendown
    down = pendown


    # ⚓ anchor: [[ChainTurtle-setheading-anchor|setheading()]] 
    #* 📝 Sets the turtles direction starting east (right)
    @tp.override
    def setheading(self, direction):
        super().seth(direction)
        return self

    seth = setheading


    # ⚓ anchor: [[ChainTurtle-home-anchor|home()]] 
    #* 📝 Sets the turtle to (0, 0) and heading = 0 -> east (right)
    @tp.override
    def home(self):
        super().home()
        return self


    # ⚓ anchor: [[ChainTurtle-home-inv-anchor|home_inv()]] 
    #* 📝 Sets the turtle to (0, 0) and heading = 0 -> east (right) traceless
    def home_inv(self):

        was_down = self.isdown()
        self.pu().home()

        if was_down:
            self.pd()

        return self


    # ⚓ anchor: [[ChainTurtle-begin-fill-anchor|begin_fill()]] 
    #* 📝 Starts the fill of a shape
    @tp.override
    def begin_fill(self):
        super().begin_fill()
        return self


    # ⚓ anchor: [[ChainTurtle-end-fill-anchor|end_fill()]] 
    #* 📝 Ends the fill of a shape -> it gets colored
    @tp.override
    def end_fill(self):
        super().end_fill()
        return self


    # ⚓ anchor: [[ChainTurtle-circle-anchor|circle()]] 
    #* 📝 Draws a circle with given radius
    @tp.override
    def circle(self, radius, extent=None, steps=None):
        super().circle(radius, extent, steps)
        return self


    # ⚓ anchor: [[ChainTurtle-circle-fill-anchor|circle_fill()]] 
    #* 📝 Draws a filled circle with given radius
    def circle_fill(self, radius, angle = None, sides = None):
        self.begin_fill().circle(radius,angle,sides).end_fill()
        return self


    # ⚓ anchor: [[ChainTurtle-dot-anchor|dot()]] 
    #* 📝 Draws a colored with given diameter
    @tp.override
    def dot(self, size):
        super().dot(size)
        return self


    # ⚓ anchor: [[ChainTurtle-color-anchor|color()]] 
    #* 📝 Changes the turtle color
    @tp.override
    def color(self, turtle_color):
        super().color(turtle_color)
        return self
    

    # ⚓ anchor: [[ChainTurtle-teleport-anchor|teleport()]] 
    #* 📝 Teleports the turtle to a given coordinate
    @tp.override
    def teleport(self, x, y, *, fill_gap: bool = False):
        super().teleport(x, y, fill_gap=fill_gap)
        return self


    # ⚓ anchor: [[ChainTurtle-shape-anchor|shape()]] 
    #* 📝 Changes the turtle's shape with a given name
    @tp.override
    def shape(self, shape_name = None):
        if shape_name is None:
            return super().shape()

        super().shape(shape_name)
        return self


    # ⚓ anchor: [[ChainTurtle-undo-anchor|undo()]] 
    #* 📝 Undoes the last turtle action
    @tp.override
    def undo(self):
        super().undo()
        return self


    # ⚓ anchor: [[ChainTurtle-clear-anchor|clear()]] 
    #* 📝 Clears the turtle's drawings on the screen
    @tp.override
    def clear(self):
        super().clear()
        return self


    # ⚓ anchor: [[ChainTurtle-hideturtle-anchor|hideturtle()]] 
    #* 📝 Hides the turtle on the turtle screen
    @tp.override
    def hideturtle(self):
        super().ht()
        return self

    ht = hideturtle


    # ⚓ showturtle anchor: [[ChainTurtle-showturtle-anchor|showturtle()]] 
    #* 📝 Shows the turtle on the turtle screen
    @tp.override
    def showturtle(self):
        super().showturtle()
        return self

    st = showturtle


    # ⚓ anchor: [[ChainTurtle-begin-poly-anchor|begin_poly()]] 
    #* 📝 Begins recording the coordinates of a polygon to be drawn
    @tp.override
    def begin_poly(self):
        super().begin_poly()
        return self


    # ⚓ anchor: [[ChainTurtle-end-poly-anchor|end_poly()]] 
    #* 📝 Ends the recording of the coordinates of a polygon that has been drawn
    @tp.override
    def end_poly(self):
        super().end_poly()
        return self


    # ⚓ anchor: [[ChainTurtle-get-poly-anchor|get_poly()]] 
    #* 📝 Retrieves the coordinates of a drawn polygon and returns it
    @tp.override
    def get_poly(self) -> tp.Sequence[tuple[float, float]] | None:
        return super().get_poly()


    # ⚓ anchor: [[ChainTurtle-list-methods-anchor|list_methods()]] 
    #* 📝 Creates and returns a dictionary with all [[ChainTurtle]] functions
    @classmethod
    def list_methods(cls):
        return uf.classes_to_dict(cls)
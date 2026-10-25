"""
This module contains the class TurtleFct which lets the user change the turtle shape to a customized one.
"""

from .. import turtle_heart as tls_heart    # noqa: I001


class TurtleFct:
   """
	This class contains a function that lets users change
   the shape of the turtles that will be created in the future with tls_color.
   """
   @classmethod
   def change_shape(
      cls,
      tls_num: tls_heart.ChainTurtle | None = None
      ) -> tls_heart.ChainTurtle | str:
      """
      This function lets the user choose different turtles shapes, including a custom option.

      :param tls_num: ChainTurtle() or None

	   :return: ChainTurtle() if tls_num is a ChainTurtle(), otherwise None
      """

   @staticmethod
   def user_tls_shape_ft(
      tls_num: tls_heart.ChainTurtle | None = None
      ) -> tls_heart.ChainTurtle | str:
      """
      This function lets the user create custom turtle shapes.

      :param tls_num: ChainTurtle() or None
        
      :return: ChainTurtle() if tls_num is a ChainTurtle(), otherwise None
      """
"""
This module contains the class TurtleFct which lets the user change the turtle shape to a customized one.
"""
 #* 📝 File type: Python type stub (.pyi)
 #* 📝 Purpose: Describes the module's interface for documentation,
 #* 📝         editor support, and static type checking.
 #* 📝 Runtime: Contains no implementation; see the corresponding
 #* 📝         .py file for executable code.

from .. import turtle_heart as tls_heart    # noqa: I001


#* 📝 Type for tls_num parameter
type TlsNumType = tls_heart.ChainTurtle | None

#* 📝 Type for custom turtle shape change function return
type TurtleOrStr = tls_heart.ChainTurtle | str


class TurtleFct:
   """
	This class contains a function that lets users change
   the shape of the turtles that will be created in the future with tls_color.
   """
   @classmethod
   def change_shape(
      cls,
      tls_num: TlsNumType = None
      ) -> TurtleOrStr:
      """
      This function lets the user choose different turtles shapes, including a custom option.

      :param tls_num: ChainTurtle() or None

	   :return: ChainTurtle() if tls_num is a ChainTurtle(), otherwise None
      """

   @staticmethod
   def user_tls_shape_ft(
      tls_num: TlsNumType = None
      ) -> TurtleOrStr:
      """
      This function lets the user create custom turtle shapes.

      :param tls_num: ChainTurtle() or None
        
      :return: ChainTurtle() if tls_num is a ChainTurtle(), otherwise None
      """
"""
This module contains the class Usershape which contains functions to make a customized turtle shape.
"""
 #* 📝 File type: Python type stub (.pyi)
 #* 📝 Purpose: Describes the module's interface for documentation,
 #* 📝         editor support, and static type checking.
 #* 📝 Runtime: Contains no implementation; see the corresponding
 #* 📝         .py file for executable code.

import collections.abc as cabc  # noqa: I001
import numbers as num


#* 📝 Type for any real number
type RealType = float | int | num.Real

 #* 📝 The type returned by each turtle shape changer function from UserShape
type ReturnShapeType = cabc.Sequence[tuple[RealType, RealType]] | None

 #* 📝 The type of the dictionary derived from UserShape
type UserShapeDictType = dict[
    str,
    cabc.Callable[[], ReturnShapeType]
]


class UserShape:
    """
    This class contains different custom turtle shape maker functions
    """
    @staticmethod
    def custom_circle() -> ReturnShapeType:
        """
        Creates a custom circle turtle shape.

        :return: the custom shape
        """

    @staticmethod
    def custom_square() -> ReturnShapeType:
        """
        Creates a custom square turtle shape.

        :return: the custom shape
        """

    @staticmethod
    def custom_triangle() -> ReturnShapeType:
        """
        Creates a custom equilateral triangle turtle shape.

        :return: the custom shape
        """

    @staticmethod
    def custom_poly() -> ReturnShapeType:
        """
        Creates a custom regular polygon turtle shape.

        :return: the custom shape
        """

    @staticmethod
    def custom_SOD() -> ReturnShapeType:
        """
        Creates a custom star of David turtle shape.

        :return: the custom shape
        """

    @classmethod
    def list_shapes(cls) -> UserShapeDictType:
        """
        Creates a dictionary with the functions in UserShape and returns it.

        :return: dictionary containing function names -> function
        """

def get_UserShape_dict() -> UserShapeDictType:
    """
    Takes all custom turtle functions in UserShape and returns a dictionary with them.

    :return: dictionary mapping function names to functions
    """

CUSTOM_SHAPES: UserShapeDictType
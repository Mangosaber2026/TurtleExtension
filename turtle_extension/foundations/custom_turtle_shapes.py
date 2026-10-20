from numbers import Real

import uf

from ..turtle_heart import tl


#* Class containing all premade turtle shape functions
@uf.cls_deco_superposition(staticmethod)
class UserShape:
    def custom_circle():
        radius: Real = uf.get_num(float, "Enter the radius: ")
        tl.begin_poly()
        tl.circle(radius)
        tl.end_poly()
        return tl.get_poly()

    def custom_square():
        length: Real = uf.helper.length_float()
        tl.begin_poly()

        for _ in range(4):
            tl.fd(length)
            tl.lt(90)

        tl.end_poly()
        return tl.get_poly()

    def custom_triangle():
        length: Real = uf.helper.length_float()
        tl.begin_poly()

        for _ in range(3):
            tl.fd(length)
            tl.lt(120)

        tl.end_poly()
        return tl.get_poly()

    def custom_poly():
        length: Real = uf.helper.length_float()
        sides: int = uf.helper.sides_num()

        radius = length / (2 * uf.sine(180 / sides))
        angle_to_right = (180 - (180 * (sides - 2)) / sides) / 2
        tl.begin_poly()

        tl.rt(angle_to_right)
        tl.circle(radius, 360, sides)
        tl.lt(angle_to_right)

        tl.end_poly()
        return tl.get_poly()

    def custom_SOD():
        side: Real = uf.helper.length_float()
        tl.begin_poly()

        for _ in range(6):
            tl.pu(); tl.fd(side); tl.pd(); tl.rt(60)
            for _ in range(3):
                tl.fd(side); tl.rt(120)
            tl.lt(60); tl.pu(); tl.bk(side); tl.pd(); tl.lt(60)

        tl.end_poly()
        return tl.get_poly()

    #* Creates and returns a dictionary mapping [[UserShape]]
    #* function names with their corresponding function
    @classmethod
    def list_shapes(cls):
        return uf.classes_to_dict(cls)

#* Creates a customized dictionary mapping [[UserShape]] functions by having the
#* prefix "custom_" switched with cm
def get_UserShape_dict():
    return {
        f"cm {name.removeprefix('custom_')}": func
        for name, func in UserShape.list_shapes().items()
        if not name.startswith("_")
    }

#* [[UserShape]] dictionary storage
CUSTOM_SHAPES = get_UserShape_dict()
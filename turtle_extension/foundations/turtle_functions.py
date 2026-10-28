# ⚓ Anchor for this module: [[turtle-functions-anchor|turtle_functions.py]] 

import uf

from .. import turtle_heart as tls_heart
from . import custom_turtle_shapes as cm_tl_shapes
from . import global_variables as glb_var


# ⚓ TurtleFct anchor: [[TurtleFct-anchor|class TurtleFct]] 
#* 📝 Class containing turtle shape changer functions
class TurtleFct:

    # ⚓ change_shape anchor: [[TurtleFct-change-shape-anchor|change_shape()]] 
     #* 📝 Main turtle shape changer function, potentially triggers [[#user-drawing-ft-anchor|user_tls_shape_ft()]] 
    @classmethod
    def change_shape(cls, tls_num = None):
        if tls_num is not None:
            uf.TypeValidate(tls_heart.ChainTurtle)(tls_num, name="tls_num")

        turtle_shapes_list: list[str] = tls_heart.tl.getshapes()

        user_shape: str = uf.get_str(f'''
            Here are the options for the turtle shape:
            {turtle_shapes_list}
            custom -> custom turtle shapes
            Enter choice: ''', turtle_shapes_list, "custom")

        if user_shape in turtle_shapes_list:
            if tls_num is not None:
                tls_num.shape(user_shape)
                return tls_num
            else:
                glb_var.UV["tls_shape"] = user_shape
                return user_shape
        else:
            if tls_num is not None:
                return cls.user_tls_shape_ft(tls_num)
            else:
                return cls.user_tls_shape_ft()

    # ⚓ user_tls_shape_ft anchor: [[TurtleFct-user-tls-shape-ft-anchor|user_tls_shape_ft()]] 
    #* 📝 Lets the user choose custom shapes from [[#CUSTOM-SHAPES-anchor|CUSTOM_SHAPES]] 
    @staticmethod
    def user_tls_shape_ft(tls_num = None):
        if tls_num is not None:
            uf.TypeValidate(tls_heart.ChainTurtle)(tls_num, name="tls_num")

        CUSTOM_SHAPES = cm_tl_shapes.CUSTOM_SHAPES

        user_shape: str = uf.get_str(f'''
            Here are some custom options:
            {CUSTOM_SHAPES.keys()}
            Enter choice: 
            ''', CUSTOM_SHAPES)

        tl = tls_heart.tl
        
        tl.home()
        shape_made = CUSTOM_SHAPES[user_shape]()
        tl.addshape(user_shape, shape_made)    # type: ignore[reportArgumentType]  
        tl.clear()
        tl.ht()

        if tls_num is not None:

            tls_num.shape(user_shape)
            return tls_num
        
        else:

            UV["tls_shape"] = user_shape
            return user_shape
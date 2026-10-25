# ⚓ Anchor for this module: [[custom-turtle-shapes-anchor|custom_turtle_shapes.py]] 

import numbers as num

import uf

from .. import turtle_heart as tls_heart


# ⚓ UserShape anchor: [[UserShape-anchor|class UserShape]] 
#* 📝 Class containing all premade turtle shape functions
@uf.cls_deco_superposition(staticmethod)
class UserShape:

	# ⚓ custom_circle anchor: [[UserShape-custom-circle-anchor|custom_circle()]] 
	#* 📝 Draws a custom circle for the turtle shape 
	#* 📝 with custom radius and returns it
	def custom_circle():		# type: ignore
        
		# 🔗 Link to [[#get-num-anchor|get_num() root]] 
		radius: num.Real = uf.get_num(float, "Enter the radius: ") # type: ignore
		tl = tls_heart.tl
		
		tl.begin_poly()
		tl.circle(radius)		# type: ignore
		tl.end_poly()
        
		return tl.get_poly()

	# ⚓ custom_square anchor: [[UserShape-custom-square-anchor|custom_square()]] 
	#* 📝 Draws a custom square for the turtle shape
	#* 📝 with custom length and returns it
	def custom_square():		# type: ignore

		# 🔗 Link to [[#HelperFunctions-length-float-anchor|length_float() root]] 
		length: num.Real = uf.helper.length_float()
		tl = tls_heart.tl
		
		tl.begin_poly()

		for _ in range(4):
			tl.fd(length)		# type: ignore
			tl.lt(90)

		tl.end_poly()
      
		return tl.get_poly()

	# ⚓ custom_triangle anchor: [[UserShape-custom-triangle-anchor|custom_triangle()]] 
	#* 📝 Draws a custom triangle for the turtle shape
	#* 📝 with custom length and returns it
	def custom_triangle():		# type: ignore

		# 🔗 Link to [[#HelperFunctions-length-float-anchor|length_float() root]] 
		length: num.Real = uf.helper.length_float() 
		tl = tls_heart.tl
      
		tl.begin_poly()

		for _ in range(3):
			tl.fd(length)		# type: ignore
			tl.lt(120)

		tl.end_poly()
      
		return tl.get_poly()

	# ⚓ custom_poly anchor: [[UserShape-custom-poly-anchor|custom_poly()]] 
	#* 📝 Draws a custom regular polygon for the turtle shape
	#* 📝 with custom length and sides and returns it
	def custom_poly():		# type: ignore

		# 🔗 Link to [[#HelperFunctions-length-float-anchor|length_float() root]] 
		length: num.Real = uf.helper.length_float()

		# 🔗 Link to [[#HelperFunctions-sides-num-anchor|sides_num() root]] 
		sides: int = uf.helper.sides_num()

		tl = tls_heart.tl

		angle = 180 / sides
		radius = length / (2 * uf.sine(angle))		# type: ignore
		angle_to_right = (180 - (180 * (sides - 2)) / sides) / 2
      
		tl.begin_poly()

		tl.rt(angle_to_right)
		tl.circle(radius, 360, sides)		# type: ignore
		tl.lt(angle_to_right)

		tl.end_poly()
      
		return tl.get_poly()

	# ⚓ custom_SOD anchor: [[UserShape-custom-SOD-anchor|custom_SOD()]] 
	#* 📝 Draws a regular star of David for the turtle shape
	#* 📝 with custom length and returns it
	def custom_SOD():		# type: ignore

		# 🔗 Link to [[#HelperFunctions-length-float-anchor|length_float() root]] 
		side: num.Real = uf.helper.length_float()
		tl = tls_heart.tl

		tl.begin_poly()

		for _ in range(6):
			tl.pu()
			tl.fd(side)		# type: ignore
			tl.pd()
			tl.rt(60)

			for _ in range(3):
				tl.fd(side)		# type: ignore
				tl.rt(120)

			tl.lt(60)
			tl.pu()
			tl.bk(side)		# type: ignore
			tl.pd()
			tl.lt(60)

		tl.end_poly()

		return tl.get_poly()

	# ⚓ list_shapes anchor: [[UserShape-list-shapes-anchor|list_shapes()]] 
	#* 📝 Creates and returns a dictionary mapping [[#UserShape-anchor|UserShape]] 
	#* 📝 function names with their corresponding function
	@classmethod
	def list_shapes(cls):

		# 🔗 Link to [[#classes-to-dict-anchor|classes_to_dict() root]] 
		return uf.classes_to_dict(cls)


# ⚓ get_UserShape_dict(): [[get-UserShape-dict-anchor|get_UserShape_dict()]] 
#* 📝 Creates a customized dictionary mapping [[#UserShape-anchor|UserShape]] functions 
#* 📝 by having the prefix "custom_" switched with cm
def get_UserShape_dict():

	# 🔗 Link to [[#UserShape-list-shapes-anchor|list_shapes() root]] 
   return {
      f"cm {name.removeprefix('custom_')}": func
      for name, func in UserShape.list_shapes().items()
   }


# ⚓ CUSTOM_SHAPES anchor: [[CUSTOM-SHAPES-anchor|dictionary CUSTOM_SHAPES]] 
#* 📝 [[#UserShape-anchor|UserShape]] dictionary storage made with [[#get-UserShape-dict-anchor|get_UserShape_dict()]] 
CUSTOM_SHAPES = get_UserShape_dict()
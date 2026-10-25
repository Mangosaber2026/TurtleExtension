# ⚓ Anchor for this module: [[global-variables-anchor|global_variables.py]] 


# ⚓ UV anchor: [[UV-anchor|dictionary UV]] 
#* 📝 UV = UNIVERSAL VARIABLES
UV = {
    "delay": None,               #* 📝 Delay for [[#user-drawing-ft-anchor|user_drawing_ft()]] 
      "t": 0,                    #* 📝 [[#user-drawing-ft-anchor|user_drawing_ft's]] current turtle
      "tls": [],                 #* 📝 [[#user-drawing-ft-anchor|user_drawing_ft's]] turtle list
      "tls_shape": "arrow",      #* 📝 turtle's current shape
}


# ⚓ t_now anchor: [[t-now-anchor|t_now()]] 
#* 📝 Retrieves the current turtle from UV
def t_now():
    return UV["tls"][UV["t"]]


# ⚓ t_shape anchor: [[t-shape-anchor|t_shape()]] 
#* 📝 Retrieves the current turtle shape
def t_shape():
    return UV["tls_shape"]
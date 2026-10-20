#* UV = UNIVERSAL VARIABLES
UV = {
    "delay": None,              #* Delay for [[turtle_runner.py#user_drawing_ft]]
      "t": 0,                   #* user_drawing_ft's current turtle
      "tls": [],                #* user_drawing_ft's turtle list
      "tls_shape": "arrow",     #* turtle's current shape
}

#* Retrieves the current turtle from UV
def t_now():
    return UV["tls"][UV["t"]]

#* Retrieves the current turtle shape
def t_shape():
    return UV["tls_shape"]
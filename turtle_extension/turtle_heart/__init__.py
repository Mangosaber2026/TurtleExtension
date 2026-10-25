# ⚓ Anchor for this module: [[turtle-heart-anchor|turtle_heart.__init__.py]] 

#* 📝 Imports the [[#ChainTurtle-anchor|ChainTurtle class]] and turtle.py from [[#turtle-skeleton-anchor|turtle_skeleton.py]] 
from .turtle_skeleton import (
   ChainTurtle,
   # 🔗 Link to source code: [[#ChainTurtle-anchor|class ChainTurtle]] 
   tl,
)

#* 📝 Specifies the classes found in [[turtle_skeleton.py]]
__all__ = [
   "ChainTurtle",
   "tl",
]
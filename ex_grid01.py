# -*- coding: utf-8 -*-

"""
    Examples for the NURBS-Python Package - Grid Generator
    Released under MIT License
    Developed by Onur Rauf Bingol (c) 2017
"""

from nurbs import Grid as gridgen

# Generate a 50x100 rectangle
mygrid = gridgen.Grid(50.0, 100.0)

# Split the width into 5 equal pieces and the height into 10 equal pieces
mygrid.generate(5, 10)

# Save the file, by default as grid.txt
mygrid.save()

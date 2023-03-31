# Colour Map Analysis

This repository contains some basic colourbar QC tools for Petrel format colourbars (.alut files).

You can upload your own .alut file and see the QC plots: https://colourmapanalysis.pythonanywhere.com/

- Colour map analysis.ipynb 
  - Jupyter notebook containing code to load .alut files, analyse them and create figure
  
- flask_app.py
  - This the flask app, with similar code to the notebook, running at pythonanywhere.com
  
- export cmap to alut.py
  - Python script to export matplotlib colourmaps to .alut files (to load into Petrel)
  - Work in progress, need to handle colour maps with more than 256 samples

Required packages:
- Numpy
- Matplotlib
 - Colorspacious

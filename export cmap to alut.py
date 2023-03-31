import numpy as np
import matplotlib.pyplot as plt

def export_cmap(cmap):
    """
    Function to export matplotlib colourmap object to a .alut file which can be read by Petrel.
    RGBA values need to be rounded to the nearest integer so some precision is lost.
    Input: matplotlib.colors.ListedColormap or matplotlib.colors.LinearSegmentedColormap
    Output: .alut file (a csv text file with 256 lines of R,G,B,A integer values)
    """
    if cmap.N == 256:
        arr = (np.array([(cmap(i)) for i in range(256)]) * 255).round().astype(int)
        np.savetxt(f"{cmap.name}.alut", arr, delimiter=",", fmt='%.f')
        print(f"{cmap.name}.alut saved")
    else:
        # to do: map cmap.N to 256 and export, for now just print message
        print(f"{cmap.name} has {cmap.N} values, not 256, so not exported")
    
    return None

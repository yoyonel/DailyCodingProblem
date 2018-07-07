"""

"""
import numpy as np
from scipy import ndimage


def main():
    # Input
    a = 1 - np.zeros((5, 4), dtype=np.int)
    a[2, 0] = a[4, 0] = a[0, 1] = a[4, 1] = a[4, 2] = a[0, 3] = 0

    print(a)

    # Morpho Math: Structure
    struct = ndimage.generate_binary_structure(2, 1)
    struct[0, :] = struct[:, 0] = False
    struct[2, 2] = True

    print(struct)

    # Algo
    nb_erosion = 1
    for nb_erosion in range(1, min(a.shape)+1):
        a = ndimage.binary_erosion(a, structure=struct).astype(a.dtype)
        nb_bits = np.count_nonzero(a)
        print(f"nb_erosion: {nb_erosion} - nb_bits: {nb_bits}")
        if nb_bits < 4:
            break
    print(f"nb_erosion={nb_erosion} -> final result erosion:\n{a}")


if __name__ == '__main__':
    main()

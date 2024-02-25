from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    #(480, 640)
    for i in range(0, 9):
        res[300:, 32*i:32*(i+1)] = -0.0625 * (i-10)
    for i in range(10, 20):
        res[300:, 32*i:32*(i+1)] = -0.0625 * (i-10)
            
    
    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    for i in range(0, 9):
        res[300:, 32*i:32*(i+1)] = 0.0625 * (i-10)
    for i in range(10, 20):
        res[300:, 32*i:32*(i+1)] = 0.0625 * (i-10)
    # ---
    return res

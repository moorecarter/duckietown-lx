from typing import Tuple

import numpy as np


def get_motor_left_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    #(480, 640)
    
    for i in range(0, 80):
        res[140+(2*i):480, 0:320] = 0.0125 * i
    for i in range(0, 80):
        res[200-i:, i*4:4*(i+4)] += -0.0015*(i-80)

    for i in range(0, 80):
        res[140+(2*i):480, 320:] = -0.0125 * i
    for i in range(0, 80):
        res[120+i:, i*4+320:4*(i+4)+320] += 0.0015*(-i)

    for i in range(0, 80):
        res[0:200-i, i*4:4*(i+1)] = -0.35
    for i in range(0, 80):
        res[0:120+i, i*4+320:4*(i+1)+320] = 0.35
        

    # ---
    return res


def get_motor_right_matrix(shape: Tuple[int, int]) -> np.ndarray:
    # TODO: write your function instead of this one
    res = np.zeros(shape=shape, dtype="float32")
    # these are random values
    for i in range(0, 80):
        res[140+(2*i):480, 0:320] = -0.0125 * i
    for i in range(0, 80):
        res[200-i:, i*4:4*(i+4)] += 0.0015*(i-80)

    for i in range(0, 80):
        res[140+(2*i):480, 320:] = 0.0125 * i
    for i in range(0, 80):
        res[120+i:, i*4+320:4*(i+4)+320] += -0.0015*(-i)

    for i in range(0, 80):
        res[0:200-i, i*4:4*(i+1)] = 0.35
    for i in range(0, 80):
        res[0:120+i, i*4+320:4*(i+1)+320] = -0.35
        
    # ---
    return res

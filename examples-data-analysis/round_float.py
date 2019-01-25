import numpy as np

def binary_to_float_np(val): return np.array([val],dtype=np.int32).view(np.float32)[0] 

#def float_to_binary_np(val): return np.array([val],dtype=np.float32).view(np.int32)[0] 
def float_to_binary_np(val): return np.array([val],dtype=np.float32).view(np.uint32)[0] 

def double_to_float_np(val): return np.array([val],dtype=np.float32)[0] 

def precision_float_from_bit(val, add_bit):
    uval = float_to_binary_np(val)
    uval_p = uval + add_bit
    precision = binary_to_float_np(uval_p) - binary_to_float_np(uval)
    return precision

def round_float(val, nbits=23):
    mask = 0xFFFF_FFFF << (23 - nbits)
    uval = float_to_binary_np(val)
    uval &= mask
    result = binary_to_float_np(uval)
    return result

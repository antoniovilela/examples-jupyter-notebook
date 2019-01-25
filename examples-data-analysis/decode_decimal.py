import struct
import numpy as np

def binary_to_float(val): return struct.unpack('!i', struct.pack('!f', val))[0]

def float_to_binary(val): return struct.unpack('!f', struct.pack('!i', val))[0]

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

def decode(val, debug=False): 
    # From https://en.wikipedia.org/wiki/Single-precision_floating-point_format
    sign = (val & 0x8000_0000) >> 31 
    exp  = (val & 0x7F80_0000) >> 23 
    mant = (val & 0x007F_FFFF) 
    if debug: print ( hex(sign), hex(exp), hex(mant) )   
    sum_mant = 1. 
    for i in range(23): 
        mask = ( 0x1 << i ) 
        if debug: print ( hex(mask), hex(mant & mask), ( (mant & mask) >> i ) )   
        sum_mant += ( (mant & mask) >> i ) * 2**( -(23 - i) ) 
         
    result = (-1)**(sign) * 2**( exp - 127 ) * sum_mant       
    return result 

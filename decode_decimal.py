import struct

def binary_float(val): return struct.unpack('!i', struct.pack('!f', val))[0]

def float_binary(val): return struct.unpack('!f', struct.pack('!i', val))[0]

def decode(val, debug=False): 
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

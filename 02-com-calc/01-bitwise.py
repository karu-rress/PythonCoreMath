# 2's complement
def complement2(number):
    return -number & 0xFF

print(bin(complement2(5)))


# MASK
argb = 0b11010111101011010011010111001111
def get_pixel_color(argb_value):
    A = 0xFF000000
    R = 0x00FF0000
    G = 0x0000FF00
    B = 0x000000FF
    
    a = (argb_value & A) >> 24
    r = (argb_value & R) >> 16
    g = (argb_value & G) >> 8
    b = argb_value & B

    return a, r, g, b

print(get_pixel_color(argb))


# FLAG
# flag = item1, item2, item3, item4
item = 0b0000
item |= 0b0010 # add item3
item |= 0b1000 # add item1

item1 = item & 0b1000 # check if having item1

item &= (~0b0010) # remove item3
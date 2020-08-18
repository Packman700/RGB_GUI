def print_hex(dec):
    if dec >= 16:
        if dec > 255:
            return 'ff'
        else:
            return hex(dec)[2:]
    else:
        if dec < 0:
            return '00'
        else:
            return '0{}'.format(hex(dec)[2:])

def combine_hex(R,G,B):
    return '#{}{}{}'.format(print_hex(R),print_hex(G),print_hex(B))

def hex_validation(input):
    try:
        if input[0] == '#' and 0 <= int(input[1:3],16) <= 255  and 0 <= int(input[3:5],16) <= 255  and 0 <= int(input[5:7],16) <= 255:
            return True
    except:
        return False
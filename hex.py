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
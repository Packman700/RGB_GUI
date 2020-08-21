import colorsys
import math
import hex

Colors_preset = {'Triad': {1: [120, 30, 0], 2: [120, 0, 0], 4: [240, 0, 0], 5: [240, 30, 0]},
                 'Complementary': {1: [360, 30, 0], 2: [360, 60, 0], 4: [180, 0, 0], 5: [180, 30, 0]},
                 'Split-complementary': {1: [150, 30, 0], 2: [150, 0, 0], 4: [210, 0, 0], 5: [210, 30, 0]},
                 'Monochromatic': {1: [360, -20, 30], 2: [360, -10, 0], 4: [360, 10, 0], 5: [360, 20, 50]},
                 'Quadrangle': {1: [90, 30, 0], 2: [360, 30, 0], 4: [180, 0, 0], 5: [270, 0, 0]},
                 'Tetradic': {1: [90, 0, 0], 2: [0, -30, 0], 4: [180, 0, 0], 5: [270, 0, 0]},
                 'Analog': {1: [30, 0, 0], 2: [60, 0, 0], 4: [330, 0, 0], 5: [300, 0, 0]}}

def hue_change(r,g,b,number, type, preset=Colors_preset):
    hls_tuple_color = colorsys.rgb_to_hls(r, g, b)

    hls_color = list(hls_tuple_color)
    # H
    hls_color[0] = abs((hls_color[0]*360 + preset[type][number][0]+360)/360)

    # L
    if hls_color[1]/255*100-preset[type][number][1] >= 20: # Dać na 30?
        hls_color[1] = hls_color[1] - preset[type][number][1]*2.55
    elif hls_color[1] + preset[type][number][1]*2.55 > 255:
        hls_color[1] = 255
    else:
        hls_color[1] = hls_color[1] + preset[type][number][1]*2.55

    # #S
    hls_color[2] = hls_color[2] + preset[type][number][2]/10000

    rgb_color = colorsys.hls_to_rgb(hls_color[0],hls_color[1],hls_color[2])

    return hex.combine_hex(int(rgb_color[0]),int(rgb_color[1]),int(rgb_color[2]))


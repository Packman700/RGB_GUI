import colorsys
import math
import hex
# ,number=None, type=None
def hue_change(r,g,b,hue_spin):

    hls_tuple_color = colorsys.rgb_to_hls(r, g, b)

    hls_color = list(hls_tuple_color)
    hls_color[0] = abs(hls_color[0] + hue_spin/360 - 1) #Poprawić bo coś nie działa :<
    rgb_color = colorsys.hls_to_rgb(hls_color[0],hls_color[1],hls_color[2])

    return hex.combine_hex(int(rgb_color[0]),int(rgb_color[1]),int(rgb_color[2]))


print(hue_change(234,95,250,180))
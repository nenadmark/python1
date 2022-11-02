print(":::::::::::::::::::::::::::::::::")
print("OVO NE VALJA !")
blue_hex = "4285F4"
blue_rgb = 66-133-244

red_hex = "DB4437"
red_rgb = 219-68-55

yellow_hex = "F4B400"
yellow_rgb = 244-180-0

green_hex = "0F9D58"
green_rgb = 15-157-88

print("Converting HEX to RGB and vice versa: ")
print("#BLUE", "#", int(blue_hex, base=16), hex(blue_rgb))
print("#BLUE", "#", int(red_hex, base=16), hex(red_rgb))
print("#BLUE", "#", int(yellow_hex, base=16), hex(yellow_rgb))
print("#BLUE", "#", int(green_hex, base=16), hex(green_rgb))

print(":::::::::::::::::::::::::::::::::")
print("GOOGLE:")
def hex_to_rgb(hex):
  rgb = []
  for i in (0, 2, 4):
    decimal = int(hex[i:i+2], 16)
    rgb.append(decimal)
  
  return tuple(rgb)

print(hex_to_rgb('FFA501'))
print(":::::::::::::::::::::::::::::::::")


blue_rgb_a = 66
blue_rgb_b = 133
blue_rgb_c = 244
blue_hex_a = "42"
blue_hex_b = "85"
blue_hex_c = "F4"

red_rgb_a = 219
red_rgb_b = 68
red_rgb_c = 55
red_hex_a = "DB"
red_hex_b = "44"
red_hex_c = "37"

yellow_rgb_a = 244
yellow_rgb_b = 180
yellow_rgb_c = 0
yellow_hex_a = "F4"
yellow_hex_b = "B4"
yellow_hex_c = "00"

green_rgb_a = 15
green_rgb_b = 157
green_rgb_c = 88
green_hex_a = "0F"
green_hex_b = "9D"
green_hex_c = "58"

print(":::::::::::::::::::::::::::::::::")
print("BLUE - RGB TO HEX: ",hex(blue_rgb_a),".", hex(blue_rgb_b),".", hex(blue_rgb_c), sep = "")
print("RED - RGB TO HEX: ",hex(red_rgb_a),".", hex(red_rgb_b),".", hex(red_rgb_c), sep = "")
print("YELLOW - RGB TO HEX: ",hex(yellow_rgb_a),".", hex(yellow_rgb_b),".", hex(yellow_rgb_c), sep = "")
print("GREEN - RGB TO HEX: ",hex(green_rgb_a),".", hex(green_rgb_b),".", hex(green_rgb_c), sep = "")
print("::::::")
print("BLUE - HEX TO RGB: ",int(blue_hex_a, base=16),".", int(blue_hex_b, base=16),".", int(blue_hex_c, base=16), sep = "")
print("RED - HEX TO RGB: ",int(red_hex_a, base=16),".", int(red_hex_b, base=16),".", int(red_hex_c, base=16), sep = "")
print("YELLOW - HEX TO RGB: ",int(yellow_hex_a, base=16),".", int(yellow_hex_b, base=16),".", int(yellow_hex_c, base=16), sep = "")
print("GREEN - HEX TO RGB: ",int(green_hex_a, base=16),".", int(green_hex_b, base=16),".", int(green_hex_c, base=16), sep = "")
print(":::::::::::::::::::::::::::::::::")
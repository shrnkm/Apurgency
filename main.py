import numpy as np
import matplotlib.pyplot as plt

name = input('What\'s your name?\n')
print('\nHi ,' + name + '!')

print('=============================================================')

color_dic = {0: ['boring green','#63b365'],
             1: ['cyan','#00ffff'],
             2: ['yellow','#ffff14'],
             3: ['lime green','#89fe05'],
             4: ['hot pink','#ff028d'],
             5: ['cornflower','#6a79f7'],
             6: ['white','#ffffff'],
             7: ['neon blue','#04d9ff'],
             8: ['bright teal','#01f9c6'],
             9: ['purpley blue','#5f34e7'],
             10:['balck','#000000'],
             11:['darker purple','#5f1b6b'],
             12:['very light purple','#f6cefc'],
             13:['light yellow green','#ccfd7f'],
             14:['cool grey','#95a3a6'],
             15:['fluro green','#0aff02'],
             16:['lipstick red','#c0022f'],
             17:['lawn green','#4da409'],
             18:['darkblue','#030764'],
             19:['sand yellow','#fce166'],
             20:['golden rod','#f9bc08'],
             21:['neon red','#ff073a'],
             22:['vivid purple','#9900fa'],
             23:['orange pink','#ff6f52'],
             24:['desert','#ccad60']}

colors = [None] * 25
for key,value in color_dic.items():
  x = (key % 5) * 3.5
  y = (key // 5) * 3.5
  colors[key] = plt.Rectangle((x, y), 3, 3, fc=value[1])
  plt.gca().add_patch(colors[key])
  rx, ry = colors[key].get_xy()
  cx = rx + 1.5
  cy = ry + 1.5
  plt.annotate(key, (cx, cy), color='darkgrey', weight='bold',
                fontsize=12, ha='center', va='center')

plt.axis('scaled')
plt.axis('off')
plt.show()

color = input('Please pick up your color by entering its number: ')

color = color_dic[int(color)][1]

print('=============================================================')

print('Okay, let\'s start with the primary colors (red, gree, blue); which one is closer to your color, ' + name +'?\n')

red = plt.Rectangle((0, 0), 5, 5, fc='#e50000')
plt.gca().add_patch(red)
green = plt.Rectangle((5.5, 0), 5, 5, fc='g')
plt.gca().add_patch(green)
blue = plt.Rectangle((11, 0), 5, 5, fc='b')
plt.gca().add_patch(blue)
the_color = plt.Rectangle((19, 0), 5, 5, fc=color)
plt.gca().add_patch(the_color)
plt.annotate('Your color', (21.5, 2.5), color='w', weight='bold',
                fontsize=9, ha='center', va='center')
plt.axis('scaled')
plt.axis('off')
plt.show()

cur_clr = input('Please type the color name, ' + name + ': ')

print('=============================================================')

state = plt.Rectangle((0, 0), 5, 5, fc=cur_clr)
plt.gca().add_patch(state)
the_color = plt.Rectangle((5.5, 0), 5, 5, fc=color)
plt.gca().add_patch(the_color)

plt.annotate('Your color', (8, 2.5), color='w', weight='bold',
                fontsize=9, ha='center', va='center')

plt.axis('scaled')
plt.axis('off')
plt.show()

print('Now, comparing with the left hand side color,')
statement = input('how do you describe your color? ')

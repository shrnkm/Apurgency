import numpy as np
import matplotlib.pyplot as plt

act_dict = {'r':['warm'],
            'g':['yellow'],
            'b':['cold']}

msr_dict = {0:['bit', 'little'],
            1:['lot', 'very']}

name = input('What\'s your name?\n')
print('\nHi ,' + name + '!')

print('\n\n=============================================================\n\n')

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
color_rgb = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

print('\n\n=============================================================\n\n')

print('Okay, let\'s start with the primary colors (red, gree, blue); which one is closer to your color, ' + name +'?\n')

red = plt.Rectangle((0, 0), 5, 5, fc='#ff0000')
plt.gca().add_patch(red)
green = plt.Rectangle((5.5, 0), 5, 5, fc='#00ff00')
plt.gca().add_patch(green)
blue = plt.Rectangle((11, 0), 5, 5, fc='#0000ff')
plt.gca().add_patch(blue)
the_color = plt.Rectangle((19, 0), 5, 5, fc=color)
plt.gca().add_patch(the_color)
plt.annotate('Your color', (21.5, 2.5), color='w', weight='bold',
                fontsize=9, ha='center', va='center')
plt.axis('scaled')
plt.axis('off')
plt.show()

cur_clr = input('Please type the color name, ' + name + ': ')
if cur_clr.lower == 'red':
  cur_clr = '#ff0000'
elif cur_clr.lower == 'blue':
  cur_clr = '#00ff00'
elif cur_clr.lower == 'green':
  cur_clr = '#0000ff'

cur_clr_rgb = tuple(int(color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4))

print('\n\n=============================================================\n\n')

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

statement = statement.lower()
cur_clr_rgb_list = list(cur_clr_rgb)

action = ''
measure = 1

for key,value in act_dict.items():
  for adj in value:
    if adj in statement:
      action = key
      break

for key,value in msr_dict.items():
  for adv in value:
    if adv in statement:
      measure = key
      break

if ((action == 'r') and (measure == 0)):
  cur_clr_rgb_list[0] += 50
elif ((action == 'r') and (measure == 1)):
  cur_clr_rgb_list[0] += 100
elif ((action == 'b') and (measure == 0)):
  cur_clr_rgb_list[1] += 50
elif ((action == 'b') and (measure == 1)):
  cur_clr_rgb_list[1] += 100
elif ((action == 'g') and (measure == 0)):
  cur_clr_rgb_list[2] += 50
elif ((action == 'g') and (measure == 1)):
  cur_clr_rgb_list[2] += 100

cur_clr_rgb = tuple(cur_clr_rgb_list)

cur_clr = '#%02x%02x%02x' % cur_clr_rgb


print('\n\n=============================================================\n\n')

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

statement = statement.lower()
cur_clr_rgb_list = list(cur_clr_rgb)

action = ''
measure = 1

for key,value in act_dict.items():
  for adj in value:
    if adj in statement:
      action = key
      break

for key,value in msr_dict.items():
  for adv in value:
    if adv in statement:
      measure = key
      break

if ((action == 'r') and (measure == 0)):
  cur_clr_rgb_list[0] += 50
elif ((action == 'r') and (measure == 1)):
  cur_clr_rgb_list[0] += 100
elif ((action == 'b') and (measure == 0)):
  cur_clr_rgb_list[1] += 50
elif ((action == 'b') and (measure == 1)):
  cur_clr_rgb_list[1] += 100
elif ((action == 'g') and (measure == 0)):
  cur_clr_rgb_list[2] += 50
elif ((action == 'g') and (measure == 1)):
  cur_clr_rgb_list[2] += 100

cur_clr_rgb = tuple(cur_clr_rgb_list)

cur_clr = '#%02x%02x%02x' % cur_clr_rgb


print('\n\n=============================================================\n\n')

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

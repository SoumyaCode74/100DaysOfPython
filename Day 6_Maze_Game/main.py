'''

Create a game of maze. Steps to create:
1. Create a function to make the maze
2. Create functions to move left, right, up, and down
3. Prompt the player to check the bot's current position and ask for next position
4. Keep doing the same until the target position is reached

'''



import time

import matplotlib.pyplot as plt

x1, y1 = [5, 5], [10, 5]
x2, y2 = [0, 2], [2, 2]
# plt.xlim(0, 10)
# plt.ylim(0, 10)

plt.plot(x1, y1, color = 'red')
plt.plot(x2, y2, color = 'red')

for i in range(5):
    x3 = [i]
    y3 = [6]
    plt.clf()
    ax = plt.axes()
    ax.set_facecolor('black')
    plt.plot(x1, y1, color='red')
    plt.plot(x2, y2, color='red')
    plt.plot(x3, y3, marker='o', markersize=6, color='yellow')
    plt.show(block = False)
    plt.pause(3)
    input()
    plt.close()


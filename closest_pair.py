import matplotlib.pyplot as plt
import numpy as np
MIN_SEPARATION_DISTANCE = 3  # miles

def closest_pair(points):
    # base case: if there are less than 3 points, just compute the distance between them
    if len(points) < 3:
        return float("inf")
        
    # sort points by x-coordinate
    points.sort(key=lambda p: p[0])
    
    # divide points into two halves
    mid = len(points) // 2
    left_half = points[:mid]
    right_half = points[mid:]
    
    # find the minimum distance in the left and right halves
    d_left = closest_pair(left_half)
    d_right = closest_pair(right_half)
    
    # compute the minimum distance between the two halves
    d = min(d_left, d_right)
    
    # find the points within d distance of the midpoint
    midpoint = points[mid][0]
    strip = [p for p in points if abs(p[0] - midpoint) < d]
    
    # sort strip by y-coordinate
    strip.sort(key=lambda p: p[1])
    
    # find the minimum distance in the strip
    for i in range(len(strip)):
        for j in range(i+1, min(i+7, len(strip))):  #The basic operators that are the most time consuming in this inner loop are the 'range' and the 'min'. 
            d = min(d, np.linalg.norm(np.array(strip[i]) - np.array(strip[j])))    
    return d

# Points
points = [(0, 15), (2, 2), (9, 0),(0, -7), (-5, -9), (10, 20),(-8, -19), (7, -12), (-17, -11), (18, -9), (3, 5)]
n = len(points)
# compute minimum distance
d = closest_pair(points)
min_distance = closest_pair(points)
if min_distance < MIN_SEPARATION_DISTANCE:
  # Generate an alert to the pilots and air traffic control system
  b = "COLLISION ALERT: Other aircraft in close proximity. Take evasive action immediately, remaining distance {} miles".format(MIN_SEPARATION_DISTANCE)
  c = 'red'
else:
  b = "No collision detected"
  c = 'black'
# draw points and rulers
fig, ax = plt.subplots()
ax.scatter([p[0] for p in points], [p[1] for p in points])
ax.hlines(0, -25, 25)
ax.vlines(0, -25, 25)
ax.grid(True)
plt.subplots_adjust(left=0.25)
plt.figtext(0.50,0.90, "Distance = "+ str(round(d,2)), fontsize=14)
plt.figtext(0.25,0.02, b , fontsize=12, color = c)

# draw line connecting closest pair of points
if min_distance < MIN_SEPARATION_DISTANCE: 
    for i in range(n):
        for j in range(i+1, n):
            if np.linalg.norm(np.array(points[i]) - np.array(points[j])) == d:
                ax.plot([points[i][0], points[j][0]], [points[i][1], points[j][1]], 'r-')

plt.show()
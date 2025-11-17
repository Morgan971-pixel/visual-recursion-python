import matplotlib.pyplot as plt
import math

def draw_branch(x, y, length, angle, ax):
    # Base case — stop when branches get too small
    if length < 2:
        return

    # Compute the end of this branch
    rad = math.radians(angle)
    x2 = x + length * math.cos(rad)
    y2 = y + length * math.sin(rad)

    # Draw the branch
    ax.plot([x, x2], [y, y2], color="brown", linewidth=1)

    # Recursive calls for left and right branches
    new_length = length * 0.7
    draw_branch(x2, y2, new_length, angle + 30, ax)  # left branch
    draw_branch(x2, y2, new_length, angle - 30, ax)  # right branch

def draw_tree():
    fig, ax = plt.subplots(figsize=(6, 8))
    ax.set_aspect('equal')
    ax.axis("off")
    
    # Set background to white
    fig.patch.set_facecolor('white')

    # Start at (0, 0) and go upward at 90 degrees
    draw_branch(0, 0, 100, 90, ax)

    # Save the image first
    plt.savefig('fractal_tree.png', dpi=300, bbox_inches='tight', facecolor='white')
    print("Tree image saved as 'fractal_tree.png'")
    
    plt.show()

draw_tree()

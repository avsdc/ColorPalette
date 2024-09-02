
from flask import Flask, render_template
import random
import numpy as np
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt


app = Flask(__name__)
app.config['SECRET_KEY'] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
colors_num = 6

#Part 1
# Use a named color palette
palette = sns.color_palette("Blues", 5)
sns.palplot(palette)
plt.show()

# Use a sequential palette
palette = sns.color_palette("rocket", 6)
sns.palplot(palette)
plt.show()

# Use a diverging palette
palette = sns.color_palette("coolwarm", 8)
sns.palplot(palette)
plt.show()


# Part 2
# Generate 6x6 grid of random colors
grid = np.random.randint(0, 256, (6, 6, 3), dtype=np.uint8)

# Make into PIL Image and scale up using Nearest Neighbour
im = Image.fromarray(grid).resize((1600, 1600), resample=Image.NEAREST)

im.save('colors.png')


# Part 3
@app.route("/")
def generate_color_palette():

    global colors_num
    palette = []

    for _ in range(colors_num):
        color = "#{:2x}{:02x}{:02x}".format(
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )
        palette.append(color)

    return render_template("index.html", list=palette)


if __name__ == '__main__':
    app.run(debug=True)

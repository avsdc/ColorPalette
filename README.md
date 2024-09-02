**Description:**


Part1 
This part uses seaborn. Seaborn's color_palette is used to generate 3 palettes with 3 different hues i.e. 'Blues', 'rocket', and 'coolwarm'.


Part2
Numpy is used to create a grid of 6X6 random colors. The grid is resized, and scaled up using NEAREST NEIGHBOR to create a PIL image, and then saved
to a png image.

Part3
When the program is run, it navigates to the "/" endpoint, and generate_color_palette function. In the function, ussing random.randint 3 random integers, 
each in the range of 0-255 are produced. These are formatted into a string called color with 3 hexadecimal numbers.
The string is concatenated to a list called palette. The list palette is sent to index.html file using render_template. In index.html, inside the div class
container, 6 colors are displayed in 6 boxes, to create a color palette.


**Requirements:**

The following are required:
flask, numpy, PIL, random, seaborn, matplotlib

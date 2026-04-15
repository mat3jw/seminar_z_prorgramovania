from tkinter import *

def load_and_process(filename):
    try:
        with open(filename, 'r') as f:
            header = f.readline().split()
            if not header: return None
            
            width = int(header[0])
            height = int(header[1])
            total_pixels = width * height
            
            print(f"Resolution: {width}x{height}")
            print(f"Total pixels: {total_pixels}")

            f.seek(0)
            print("\nFirst 5 lines of the file:")
            for i in range(5):
                line = f.readline().strip()
                if not line: break
                print(line)
            
            f.seek(0)
            f.readline()
            raw_data = f.read().replace('\n', '').replace(' ', '')
            
            pixels = []
            for r in range(height):
                row = list(raw_data[r * width : (r + 1) * width])
                pixels.append(row)
                
            return width, height, pixels
    except FileNotFoundError:
        print(f"Error: File {filename} not found.")
        return None

def draw_image():
    canvas.delete("all")
    scale = 10 
    
    for r in range(len(pixel_grid)):
        for c in range(len(pixel_grid[r])):
            color = "black" if pixel_grid[r][c] == '0' else "white"
            x1, y1 = c * scale, r * scale
            x2, y2 = x1 + scale, y1 + scale
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=color)

def invert_colors(event):
    for r in range(len(pixel_grid)):
        for c in range(len(pixel_grid[r])):
            pixel_grid[r][c] = '1' if pixel_grid[r][c] == '0' else '0'
    
    print("Image inverted!")
    draw_image()

filename = "subor1.txt" 
data = load_and_process(filename)

if data:
    img_width, img_height, pixel_grid = data
    
    root = Tk()
    root.title("Tkinter Image Viewer")

    canvas_w = img_width * 10
    canvas_h = img_height * 10
    canvas = Canvas(root, width=canvas_w, height=canvas_h, bg="grey")
    canvas.pack()

    draw_image()

    canvas.bind("<Button-1>", invert_colors)

    root.mainloop()
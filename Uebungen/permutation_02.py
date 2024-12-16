from tkinter import Tk, Frame, Canvas, Scrollbar, Button, Label, BOTH, RIGHT, Y

def perm(numbers, pos=0, results=None):
    if results is None:
        results = []

    if pos == len(numbers):
        results.append(numbers[:])  # Append a copy of the current permutation
    else:
        for element in range(pos, len(numbers)):
            numbers[pos], numbers[element] = numbers[element], numbers[pos]  # Swap
            perm(numbers, pos + 1, results)
            numbers[pos], numbers[element] = numbers[element], numbers[pos]  # Swap back
    
    return results

def display_permutations(canvas, permutations):
    # Define the color map
    color_map = {
        1: "red",
        2: "yellow",
        3: "blue",
        4: "green"
    }

    canvas.delete("all")  # Clear the canvas

    y_offset = 10  # Start position for text
    for perm in permutations:
        x_offset = 10
        for number in perm:
            canvas.create_rectangle(x_offset, y_offset, x_offset + 20, y_offset + 20, fill=color_map[number])
            x_offset += 30  # Move to the right for the next number
        y_offset += 30  # Move down for the next permutation

def generate_and_display(canvas):
    numbers = [1, 2, 3, 4]
    permutations = perm(numbers)
    display_permutations(canvas, permutations)

def main():
    root = Tk()
    root.title("Permutations Display")

    # Create the main frame
    frame = Frame(root)
    frame.pack(fill=BOTH, expand=True)

    # Create a canvas with a scrollbar
    canvas = Canvas(frame, width=400, height=400, bg="white")
    scrollbar = Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scrollbar.set)

    scrollbar.pack(side=RIGHT, fill=Y)
    canvas.pack(fill=BOTH, expand=True)

    # Add a button to generate permutations
    generate_and_display(canvas)

    root.mainloop()

if __name__ == "__main__":
    main()

from pynput.mouse import Listener, Button
import time


def add_to_file(file_path, message):
    with open(file_path, "a") as file:
        file.write(message)


interval= 0.5
last_time= time.time()
def on_move(x, y):
    global last_time
    current_time= time.time()
    if current_time - last_time >= interval:
        add_to_file("moves.txt", f"{x, y}\n")
        print(x, y)
        last_time= current_time


def on_click(x, y, button, pressed):
    if pressed:
        if button == Button.left:
            print(f"Left click: {x, y}")
            add_to_file("moves.txt", f"Left click: {x, y}\n")
        elif button == Button.right:
            print(f"Right click: {x, y}")
            add_to_file("moves.txt", f"Right click: {x, y}\n")
        elif button == Button.middle:
            return False


def on_scroll(x, y, dx, dy):
    if dy > 0:
        print(f"Scrolled up at {x, y}")
        add_to_file("moves.txt", f"Scrolled up at {x, y}\n")
    else:
        print(f"Scrolled down at {x, y}")
        add_to_file("moves.txt", f"Scrolled down at {x, y}\n")


with Listener(
    on_move= on_move,
    on_click= on_click,
    on_scroll= on_scroll
) as listener:
    listener.join()





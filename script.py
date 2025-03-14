from pynput.mouse import Listener, Button
import time
import threading

interval= 0.5
last_time= time.time()


def on_move(x, y):
    global last_time
    current_time= time.time()
    if current_time - last_time >= interval:
        print(x, y)
        last_time= current_time


def on_click(x, y, button, pressed):
    if pressed:
        if button == Button.left:
            print(f"Left click: {x, y}")
        elif button == Button.right:
            print(f"Right click: {x, y}")
        elif button == Button.middle:
            return False

def mouse_listener():
    with Listener(
        on_move= on_move,
        on_click= on_click
    ) as listener:
        listener.join()

        return listener


def add_to_file(file_path, message):
    with open(file_path, "a") as file:
        file.write(message)


# thread= threading.Thread(target= add_to_file, args=("follow moves/moves.txt", mouse_listener()))
# thread.start()


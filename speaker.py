import os
import time

my_pipe = "da_pipe"

try:
    os.mkfifo(my_pipe)
except FileExistsError:
    print("pipe already exists, continuing")

with open(my_pipe, "w") as pipe:
    print("about to write to pipe")
    pipe.write("Hellllooooo\n")
    print("Wrote to pipe")

with open(my_pipe, "w") as pipe:
    for i in range(10):
        pipe.write(f"Guess what. It's a me. Number {i}\n")
        pipe.flush()
        time.sleep(2)
        
time.sleep(2)

with open(my_pipe, "w") as pipe:
    pipe.write("goodbye\n")

print("My work here is done")

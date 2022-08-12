import os 

my_pipe = "da_pipe"

try:
    os.mkfifo(my_pipe)
except FileExistsError:
    print("pipe already exists, continuing")

def start_server():
    while True:
        with open(my_pipe, "r") as pipe:
            for line in pipe:
                if line == "goodbye\n":
                    return
                print(line)
start_server()
print("exiting. Goodbye")


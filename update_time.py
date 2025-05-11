from datetime import datetime

with open("timestamp.txt", "a") as f:
    f.write(f"{datetime.now()}\n")


print("Hello, world!")


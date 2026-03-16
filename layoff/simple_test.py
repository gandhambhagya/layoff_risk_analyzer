import os
log_path = r"c:\Users\gandh\udbhav\career-risk\layoff\simple_test.txt"
with open(log_path, "w") as f:
    f.write("Python is working and can write to disk.\n")
    f.write(f"Current Dir: {os.getcwd()}\n")

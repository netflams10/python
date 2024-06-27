#! /home/segun/anaconda3/bin/python3
import os

file = os.open("foo", os.O_WRONLY | os.O_CREAT, 0o644)

os.write(file, bytes("Hello World", "utf-8"))
os.close(file)
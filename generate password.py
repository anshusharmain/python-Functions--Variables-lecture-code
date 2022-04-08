import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%&{}[]/?()"
all = lower + upper + numbers + symbols
length = 16
password = " " .join(random.Sample(all,length))
print(password)
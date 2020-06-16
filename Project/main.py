import os
import sys

print(f"PYTHONPATH value: {os.getenv('PYTHONPATH')}")
sys.path.append("../Data")
# sys.path.append("../Programing/Pyth-env-test-1/Data")
print(sys.path)
print(f"PYTHONPATH value: {os.getenv('PYTHONPATH')}")

from veiksmas import *


print(exchange_dollar(25))
print(exchange_pound(55))

print("Success!")

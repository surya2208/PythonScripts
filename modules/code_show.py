import inspect
import random

source_code = inspect.getsource(random)
print(source_code)
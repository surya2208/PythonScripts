#inspect the pre-defined modules code in Python

import inspect
import random

source_code = inspect.getsource(random)
print(source_code)
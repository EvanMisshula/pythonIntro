import re
my_regex = re.compile("[0-9]+", re.I)

import re as regex
my_regex = regex.compile("[0-9]+", re.I)

import matplotlib.pyplot as plt 
from collections import defaultdict, Counter
lookup = defaultdict(int)
my_counter = Counter()

# Don;t just import everythin you may overwrite your own variables

match = 10
from re import *
print match

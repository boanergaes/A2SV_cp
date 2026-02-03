#!/bin/python3

#hackerrank

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
    if n % 2 == 0 and ( (n >= 2 and n <= 5) or (n > 20) ):
        print('Not Weird')
    else:
        print('Weird')

#!/usr/bin/env python3
import string
import random

def generate(size = 16, chars = string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))
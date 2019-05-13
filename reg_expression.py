#! /usr/bin/env python3

import re

message = 'Call me 415-555-1011 tomorrow, or at 415-555-9999 fpr my office line'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search(message)
print(mo.group())
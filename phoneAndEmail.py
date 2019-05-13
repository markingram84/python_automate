#! /usr/bin/env python3

import re, pyperclip

# Create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-000, 555-0000, (415) 555-0000, 555-0000 ext 12345, ext. 12345, x12345

(
 ((\d\d\d)|(\(\d\d\d)))?            # area code (optional)
 (\s|-)                             # first separator
 \d\d\d                             # first 3 digits
 -                                  # separator
 \d\d\d\d                           # last 4 digits
 (((ext(\.)?\s) |x)                 # extension word (optional)
 (\d{2,5}))?                        # extension (optional)
)

''', re.VERBOSE)

#regex for email addresses
emailRegex = re.compile(r'''
# some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+                     # name part
@                                   # @ symbol
[a-zA-Z0-9_.+]+                     # domain name part

''', re.VERBOSE)

#get the text from clipboard
text = pyperclip.paste()

#extract the email/phone from ytext
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#copy the extracted email to clipbaord
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)

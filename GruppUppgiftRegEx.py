import re
from gruppupgift_regex import support_message
from gruppupgift_regex import pattern

regex_email = pattern
result = re.findall(pattern, support_message)

print('Emails Found:' and result)



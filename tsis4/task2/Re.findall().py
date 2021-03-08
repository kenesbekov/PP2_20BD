import re
a = re.findall("[^aeiou]([aeiou]{2,})(?=[^aeiou])", input(), re.IGNORECASE)
if len(a):
    print(*a, sep='\n')
else:
    print(-1)

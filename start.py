
import sys

from structure.environment import XPathEnvironment

text = []
for line in sys.stdin:
    text.append(line)


env = XPathEnvironment.build().environment_from_string("\n".join(text))

for i in env:
    print(i)
    for j in i:
        print("-", j)

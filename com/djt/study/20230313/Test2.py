import sys

from MyModule import *

c = CLanguage("a", "b")
c.say()

print("=" * 20)
for p in sys.path:
    print(p)

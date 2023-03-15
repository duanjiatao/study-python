import MyModule as mm

print("=" * 20)
print(mm.__doc__)
print("=" * 20)

mm.say()
c = mm.CLanguage("谷歌", "www.google.com")
c.say()

print("=" * 20)
print(__name__)
print(mm.__name__)

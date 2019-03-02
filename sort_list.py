name=["a","b","c","d"]
name.append("e")
name.insert(3,"dc")
print(name)
name.sort()
print(name)
print(sorted(name))
name.sort(reverse=True)
print(name)
name.reverse()
print(len(name))
for p in name:
	print(p)


i = 1
count = 0
for ch in open("input.txt","r").read():
	count = count + (1 if ch == "(" else -1)
	if(count == -1): print(i)
	i += 1
print(count)

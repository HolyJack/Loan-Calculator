args = sys.argv
summary = 0

for i in range(4):
    summary += int(args[i + 1])
print(summary)

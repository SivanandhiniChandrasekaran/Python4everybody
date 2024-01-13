fname = input("Enter file name:")
fh = open(fname)

end = list()
for lines in fh:
    print(lines)
    words= lines.split()
    print(words)
    for word in words:
        print(word)
        end.append(word)
        print(end)
end.sort()
print(end)
cnt = end.count("and")
print(cnt)
end.reverse()
print(end)

dupes = dict.fromkeys(end)
print(dupes)
result=list(dupes)
print(result)


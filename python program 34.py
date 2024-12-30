items=input("Input comma seperated sequence of words")
words=[word for word in items.split("","")]
print(",".join(sorted(list(set(words)))))

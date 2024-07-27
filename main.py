with open("input.txt", "r", encoding="utf-8") as infile:
    content = infile.read()


reversed_content = content[::-1]

with open("output.txt", "w", encoding="utf-8") as outfile:

    outfile.write(reversed_content)

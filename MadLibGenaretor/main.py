with open("MadLibGenaretor/story.txt", "r") as f:
    story = f.read()

words = set()
start_char = '<'
end_char = '>'
start_point = -1;
for i,char in enumerate(story):
    if char ==start_char:
        start_point = i
    if char == end_char and start_point !=-1:
        word = story[start_point : i+1]
        words.add(word)
        start_point = -1



answers = dict()
for word in words:
    answers[word] = input(f"Enter your favourite word for {word}: ")

for word in words:
    story = story.replace(word, answers[word])


print("\n\n")
print(story)

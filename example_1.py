from pathlib import Path

file_path = "files/example.txt"
text_temp = 'hello'
text = (
    "Lorem Ipsum is simply dummy text of the printing and typesetting industry. "
    "Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
    "when an unknown printer took a galley of type and scrambled it to make a type specimen book. "
    "It has survived not only five centuries, but also the leap into electronic typesetting, "
    "remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset "
    "sheets containing Lorem Ipsum passages, and more recently with desktop publishing software "
    "like Aldus PageMaker including versions of Lorem Ipsum."
)

f = open(file_path, "w", encoding="utf-8")
f.write(text + text_temp)

f.close()

f = open(file_path, "r", encoding="utf-8")
content = f.read()
print(content)
f.close()

assert content == text, "Текст не совпадает"


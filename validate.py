import json
import re

with open("patch.json", mode="r", encoding="UTF-8") as f:
    patch = json.load(f)


def count_characters(text):
    count = 0
    text = re.sub(r"{.*}", "", text)
    for char in text:
        if char == "\n":
            continue
        count += 2 if ord(char) > 255 else 1
    return count


for item in patch:
    for k, v in item.items():
        for line in v.splitlines():
            count = count_characters(line)
            if count >= 25 and not line.isascii():
                if 25 <= count <= 30:
                    print(
                        f"[WARN] {count} chars: ",
                        item.get("code"),
                        item.get("name"),
                        k,
                        line,
                        count,
                    )
                else:
                    print(
                        f"[ERROR] {count} chars: ",
                        item.get("code"),
                        item.get("name"),
                        k,
                        line,
                        count,
                    )

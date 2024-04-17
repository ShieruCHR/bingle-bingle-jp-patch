def normalize(filename: str):
    with open(filename, mode="r", encoding="UTF-8") as f:
        data = f.read()
    data = data.replace('file="', 'file="graphic/font/')
    with open(filename, mode="w", encoding="UTF-8") as f:
        f.write(data)


if __name__ == "__main__":
    for file in [
        "English_Huge.fnt",
        "English_Large.fnt",
        "English_Medium.fnt",
        "English_Small.fnt",
    ]:
        normalize(file)

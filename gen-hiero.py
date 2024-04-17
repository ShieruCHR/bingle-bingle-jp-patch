SIZES = {"Huge": 65, "Large": 28, "Medium": 18, "Small": 15}


def uniqunize():
    with open("patch.json", mode="r", encoding="UTF-8") as f:
        patch = (
            r"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890\"!`?'.,;:()[]{}<>|/@\^$-%+=#_&~*\n"
            + f.read()
        )
    return set(patch)


def generate_hiero(size: int, text: str):
    with open("template.hiero", mode="r", encoding="UTF-8") as f:
        config = f.read()
    with open(f"{size}.hiero", mode="w", encoding="UTF-8") as f:
        f.write(config.replace("%SIZE%", str(size)).replace("%TEXT%", text))


if __name__ == "__main__":
    unique = "".join(uniqunize()).replace("\n", "")
    for size in SIZES.values():
        generate_hiero(size, unique)

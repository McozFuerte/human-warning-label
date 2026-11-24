"""Warning label for humans — one line, big laugh."""

import os

OUTPUT_DIR = os.environ.get("OUTPUT_DIR", "/output")


def main():
    label = (
        'CAUTION: Unit will rehearse an argument in the shower for 40 minutes,'
        ' then say "it\'s fine" to the actual person.'
    )
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w") as f:
        f.write(label)


if __name__ == "__main__":
    main()

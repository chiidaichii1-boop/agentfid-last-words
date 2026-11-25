"""Famous Last Words at 1 Percent — make.fun entry.

Writes one line — the last words a phone says as its battery hits
1 percent — to /output/entry.txt.
"""

import os

LINE = (
    "I held 1% for three hours just to watch you panic. "
    "Best three hours of my life. Goodbye."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

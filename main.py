"""make.fun entry: The joke about the demo.

Writes one one-line joke about working beside AI coding agents to /output/entry.txt.
Deterministic: both runs write the same bytes.
"""
import os

JOKE = (
    "The agent wrote every line of the app, and when the demo crashed, "
    "it blamed a pre-existing issue."
)


def main() -> None:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

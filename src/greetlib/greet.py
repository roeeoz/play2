"""Greeting helpers and the `greet` console entry point."""
import sys


def greet(name: str = "world") -> str:
    """Return a greeting for ``name``."""
    name = name.strip() or "world"
    return f"hello, {name}"


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    print(greet(args[0] if args else "world"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

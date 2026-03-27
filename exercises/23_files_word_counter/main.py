from pathlib import Path

def count_words(text: str) -> int:
    """Return number of whitespace-separated words in text."""
    raise NotImplementedError

def count_words_in_file(path: str | Path) -> int:
    """Read the file at path and return its word count."""
    raise NotImplementedError

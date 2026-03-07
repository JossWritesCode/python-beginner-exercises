# Python Beginner Exercises (with pytest)

This is a set of **very beginner-friendly** programming exercises in Python.
Each exercise lives in its own folder under `exercises/` and includes:

- `README.md` – the prompt
- one or more `.py` files – **student starter code** (mostly empty stubs)
- `test_*.py` – tests that run with **pytest**

## Setup

```bash
python -m venv .venv
source .venv/bin/activate  # (Windows: .venv\Scripts\activate)
pip install -r requirements.txt
```

## Run all tests

```bash
pytest
```

## Run one exercise's tests

Example:

```bash
pytest exercises/05_even_or_odd
```

## Notes for students

Most starter functions raise `NotImplementedError`.
That is normal: it means **you haven't written the solution yet**.
As you implement each function, the tests should start passing.

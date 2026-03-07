## 07 — While Loops (Guessing Attempts)

Write a function `attempts_until_guess(secret, guesses)`.

- `secret` is an integer.
- `guesses` is a list of integers representing guesses in order.

Return how many guesses it takes to guess the secret.
If the secret never appears in the list, return `-1`.

### Examples
- `attempts_until_guess(5, [1, 2, 5, 9])` -> `3`
- `attempts_until_guess(3, [1, 2, 4])` -> `-1`

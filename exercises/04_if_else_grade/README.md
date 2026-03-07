## 04 — If / Else (Letter Grade)

Write a function `letter_grade(score)` that returns:

- `"A"` for scores 90–100
- `"B"` for scores 80–89
- `"C"` for scores 70–79
- `"D"` for scores 60–69
- `"F"` for scores 0–59

Assume `score` is an integer from 0 to 100.

### Hint

<details>
<summary>Show hint</summary>

You can compare numbers using operators like `>=` and `<`.

<details>
<summary>Extra hint</summary>

Python checks `if/elif` conditions from top to bottom and stops at the first match.

So put the highest grade first, otherwise a high score might match a lower grade too early.

</details>

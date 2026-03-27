## 14 — Lists (Skip First N)

Write a function `skip_first_n(items, n)` that returns a new list without the first `n` items.

### Examples

- `skip_first_n([1, 2, 3, 4], 2)` -> `[3, 4]`
- `skip_first_n([1, 2], 5)` -> `[]`

Assume `n` is a non-negative integer.

<details>
<summary>Hint</summary>

Think about how slicing works when you provide a starting index but no ending index.  
What happens if the starting index is larger than the length of the list?

You can read more about slicing here:  
https://docs.python.org/3/tutorial/datastructures.html

</details>

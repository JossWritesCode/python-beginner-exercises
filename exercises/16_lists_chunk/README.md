## 16 — Lists (Chunk)

Write a function `chunk_list(items, size)` that splits a list into chunks of length `size`.

### Examples

- `chunk_list([1,2,3,4,5], 2)` -> `[[1,2], [3,4], [5]]`

Assume `size` is a positive integer.

<details>
<summary>Hint</summary>

This problem is very similar to the previous one (making pairs), but now the chunk size can change.

Try looping through the list using a step of `size`, and at each step take a slice of length `size`.

What would `items[i:i+size]` give you?

</details>

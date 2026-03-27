## 15 — Lists (Make Pairs)

Write a function `make_pairs(items)` that splits a list into groups of 2.

### Examples

- `make_pairs([1, 2, 3, 4])` -> `[[1, 2], [3, 4]]`
- `make_pairs([1, 2, 3, 4, 5])` -> `[[1, 2], [3, 4], [5]]`

This is like chunking, but the chunk size is always 2.

<details>
<summary>Hint</summary>

Think about iterating through the list using an index that increases by 2 each time.  
At each step, you can take a slice of size 2 starting from that index.

For example, what does `items[i:i+2]` give you?

</details>

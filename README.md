# Data Structures & Systems Design

- **Name:** Ankit Kumar
- **Email:** [nasaankit01@gmail.com](mailto:nasaankit01@gmail.com)
- **Portfolio:** [anky209e.netlify.app](https://anky209e.netlify.app)
- **GitHub:** [anky209e](https://github.com/anky209e)
- **Repository:** [interval-and-order](https://github.com/Anky209e/interval-and-order)

- I implemented an LRU cache and an event scheduler in Python.
- Both files include examples that run when executed directly.
- Requires Python 3. No external packages are needed.

## Problem 1: LRU Cache

- Code: [lru.py](lru.py)
- I used a dictionary to find a key's node in average O(1) time.
- A doubly linked list keeps the nodes in usage order. The least recently used node is next to the head, and the most recently used node is next to the tail.
- `get(key)` returns the value and moves the node to the most recently used position. A missing key returns `-1`.
- `put(key, value)` adds or updates a key and marks it as recently used. If the cache is full, it removes the least recently used key first.
- A capacity of zero stores nothing. Negative or non-integer capacities raise `ValueError`.

This example shows how accessing key `1` keeps it in the cache when key `3` is added:

```python
from lru import LRUCache

cache = LRUCache(2)
cache.put(1, 100)
cache.put(2, 200)
print(cache.get(1))  # 100
cache.put(3, 300)
print(cache.get(2))  # -1: key 2 was least recently used
```

## Problem 2: Event Scheduler

- Code: [even_scheduler.py](even_scheduler.py)
- I sort the events by start time before checking them.
- `can_attend_all(events)` returns `False` if an event starts before the previous event ends. Otherwise, it returns `True`.
- `min_rooms(events)` implements the assignment's `min_rooms_required` operation.
- For room counting, I use a min-heap of end times for active meetings. Before adding a meeting, I remove every meeting that has already ended.
- The largest heap size is the minimum number of rooms needed, because all meetings in the heap overlap at that point.
- An end time equal to the next start time allows the room to be reused.
- Empty input returns `True` for attendance and `0` rooms. Zero-duration events are ignored; events that end before they start raise `ValueError`.

These examples show that adjacent meetings share a room, while overlapping meetings need separate rooms:

```python
from even_scheduler import can_attend_all, min_rooms

adjacent = [(9, 10), (10, 11), (11, 12)]
print(can_attend_all(adjacent))  # True
print(min_rooms(adjacent))      # 1

overlapping = [(9, 11), (10, 12)]
print(can_attend_all(overlapping))  # False
print(min_rooms(overlapping))      # 2
```

## Time and Space Complexity

Here, `n` is the number of input events and `c` is the cache capacity. Space means extra memory used by the operation unless stated otherwise.

| Function | Time | Space |
| --- | --- | --- |
| `_Node.__init__` | O(1) | O(1) |
| `LRUCache.__init__` | O(1) | O(1) initially; O(c) when filled |
| `_append` / `_remove` | O(1) | O(1) |
| `get` | O(1) average | O(1) |
| `put` | O(1) average | O(1) per call; O(c) total cache storage |
| `_ordered_events` | O(n log n) | O(n) |
| `can_attend_all` | O(n log n), including sorting | O(n) |
| `min_rooms` | O(n log n), including sorting and heap operations | O(n) |

- Dictionary operations are O(1) on average; unusually bad hash collisions can make them O(c).
- Each meeting enters and leaves the heap at most once, so the room-counting loop takes O(n log n) overall.

## Discussion

### Why a dictionary and a doubly linked list?

- The dictionary finds a node quickly, and the linked list removes or moves that node without searching.
- A dictionary alone does not directly track the least recently used item. A linked list alone needs O(c) time to find a key.
- The trade-off is extra memory for dictionary entries and node pointers, plus more code to keep both structures consistent.

### How would I assign room numbers?

- Keep `(end_time, room_id)` pairs in the active-meeting heap.
- Move room IDs into a free-room pool when their meetings end.
- Reuse a free room, or create a new room if none is available.
- Save each event's assigned room, such as `Room A` or `Room B`, using its original input index so results stay in the original order.

### How would I make the cache thread-safe?

- Add a `threading.Lock` to the cache.
- Hold the lock for the entire `get` or `put` operation, covering both dictionary and linked-list changes.
- `get` also needs locking because it changes the usage order.
- This prevents concurrent operations from corrupting the cache, but threads must wait while another operation holds the lock.

## Run the Examples

Run each file to see its built-in examples:

```bash
python lru.py
python even_scheduler.py
```

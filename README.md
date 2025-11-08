# Thread Synchronization Techniques in Python
(Using Lock, RLock, Semaphore and Condition)

This project demonstrates how different synchronization tools from Python’s `threading` module manage concurrent access to a shared list through a common computation function (`do_something.py`).

The goal is to show how threads can work together without breaking data integrity, even when running simultaneously.

---

## 🔒 Synchronization Methods Demonstrated

### 1. **Lock**
**Purpose:** Allows only one thread to modify the shared list at a time.

**Observed Output (Simplified):**
```
Thread 0 started.
Thread 0 finished.
Thread 1 started.
Thread 1 finished.
Thread 2 started.
Thread 2 finished.
Length of list (Lock): 21
```

**Conclusion:**  
Threads ran one after another, preventing overlap. The final list length was correct.

---

### 2. **RLock (Reentrant Lock)**
**Purpose:** Lets the same thread acquire the lock multiple times safely.

**Behavior:**  
Works almost the same as Lock, but is useful in recursive functions or nested locking.

**Conclusion:**  
Data remained consistent and thread-safe.

---

### 3. **Semaphore**
**Purpose:** Controls how many threads can operate at the same time.

**Example Output:**
```
Thread 0 waiting for permit...
Thread 0 started.
Thread 1 waiting for permit...
Thread 2 waiting for permit...
Thread 1 started.
Thread 0 finished.
Thread 1 finished.
Thread 2 started.
Thread 2 finished.
Length of list (Semaphore): 21
```

**Conclusion:**  
Multiple threads could run together, but within controlled limits.

---

### 4. **Condition**
**Purpose:** Lets threads wait for a specific signal before continuing.

**Observed Output:**
```
Thread 0 notifying condition.
Thread 1 notifying condition.
Thread 2 notifying condition.
Monitor: Current length = 7
Monitor: Current length = 14
Monitor: Current length = 21
```

**Conclusion:**  
Useful when one thread must monitor or react to the progress of others.

---

## 📊 Comparison Table

| Sync Type | Core Function | Behavior | Data Safety | Ideal Use Case |
|----------|----------------|----------|-------------|----------------|
| **Lock** | Prevents simultaneous access | Threads run one-by-one | ✅ Safe | Simple mutual exclusion |
| **RLock** | Allows repeated locking by same thread | Same as Lock | ✅ Safe | Nested or recursive locking |
| **Semaphore** | Limits concurrent threads | Controlled parallelism | ✅ Safe | Limited shared resources |
| **Condition** | Enables wait/notify | Event-driven coordination | ✅ Safe | Producer-consumer patterns |

---

## 🧠 Summary

All four synchronization methods preserved data integrity, producing the expected **21 items** in the shared list.

- **Lock/RLock:** Simple mutual exclusion  
- **Semaphore:** Controls parallelism  
- **Condition:** Thread-to-thread signaling  

Choose the technique based on how much coordination or restriction your threads need.

---

## ▶️ Running the Examples

Run each file individually to observe the behavior:

```
python Chapter_02/Lock.py
python Chapter_02/RLock.py
python Chapter_02/Semaphore.py
python Chapter_02/Condition.py
```

---

## ✅ Project Structure

```
Chapter_02/
│── Lock.py
│── RLock.py
│── Semaphore.py
│── Condition.py
│── do_something.py
└── README.md
```

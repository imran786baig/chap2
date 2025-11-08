#!/usr/bin/env python3
import threading
import time
from do_something_v2 import do_something


def thread_job(thread_id, task_size, shared_list, rlock):
    """Perform work using a re-entrant lock for safe nested locking."""
    print(f"[Thread-{thread_id}] Initiated.")

    # Re-entrant locking demonstration
    with rlock:
        with rlock:
            do_something(task_size, shared_list)

    print(f"[Thread-{thread_id}] Completed.")


def main():
    shared_list = []
    rlock = threading.RLock()

    thread_count = 3
    task_size = 7

    workers = [
        threading.Thread(
            target=thread_job,
            args=(thread_id, task_size, shared_list, rlock)
        )
        for thread_id in range(thread_count)
    ]

    # Start workers with slight delay for readable output
    for worker in workers:
        worker.start()
        time.sleep(0.4)

    # Ensure all threads finish
    for worker in workers:
        worker.join()

    print("\n✅ Final Data List:", shared_list)
    print("📊 Total Items (RLock):", len(shared_list))


if __name__ == "__main__":
    main()

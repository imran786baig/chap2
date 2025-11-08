#!/usr/bin/env python3
import threading
import time
from do_something_v2 import do_something


def execute_job(thread_id, task_size, results, lock):
    """Run a CPU-bound task inside a thread while holding a lock."""
    print(f"[Worker-{thread_id}] Execution started.")

    # Ensure safe access to shared list
    with lock:
        do_something(task_size, results)

    print(f"[Worker-{thread_id}] Execution completed.")


def main():
    results = []
    lock = threading.Lock()

    thread_count = 3
    task_size = 7

    workers = [
        threading.Thread(
            target=execute_job,
            args=(thread_id, task_size, results, lock),
        )
        for thread_id in range(thread_count)
    ]

    # Start workers with a small delay for clean output
    for worker in workers:
        worker.start()
        time.sleep(0.4)

    # Wait for all threads to finish
    for worker in workers:
        worker.join()

    print("\n✅ Final Result List:", results)
    print("📊 Total Processed (Lock):", len(results))


if __name__ == "__main__":
    main()

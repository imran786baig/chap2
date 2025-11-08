#!/usr/bin/env python3
import threading
import time
from do_something_v2 import do_something


def thread_task(thread_id, chunk_size, shared_data, semaphore):
    """Acquire a semaphore permit before executing the assigned task."""
    print(f"[Worker-{thread_id}] Requesting access...")

    with semaphore:
        print(f"[Worker-{thread_id}] Access granted. Processing...")
        do_something(chunk_size, shared_data)
        print(f"[Worker-{thread_id}] Task complete.")


def main():
    shared_data = []
    semaphore = threading.Semaphore(2)  # allow up to 2 concurrent threads

    thread_count = 3
    chunk_size = 7

    threads = [
        threading.Thread(
            target=thread_task,
            args=(thread_id, chunk_size, shared_data, semaphore)
        )
        for thread_id in range(thread_count)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("\n✅ Final Shared Data:", shared_data)
    print("📊 Total Elements (Semaphore):", len(shared_data))


if __name__ == "__main__":
    main()

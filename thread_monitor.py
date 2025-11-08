#!/usr/bin/env python3
import threading
import time
from do_something_v2 import do_something


def task_runner(tid, count, results, sync_lock):
    """Run CPU-bound work in a worker thread and notify monitor."""
    print(f"[Worker-{tid}] Running task...")
    do_something(count, results)

    with sync_lock:
        print(f"[Worker-{tid}] Task complete. Sending signal.")
        sync_lock.notify()

    print(f"[Worker-{tid}] Exiting thread.")


def watch_progress(results, sync_lock, expected_total):
    """Monitor progress until all items are processed."""
    with sync_lock:
        while len(results) < expected_total:
            sync_lock.wait()
            print(f"[Monitor] Current processed items: {len(results)}")


def main():
    results = []
    sync_lock = threading.Condition()

    threads_count = 3
    chunk_size = 7
    expected_total = threads_count * chunk_size

    workers = [
        threading.Thread(
            target=task_runner,
            args=(tid, chunk_size, results, sync_lock)
        )
        for tid in range(threads_count)
    ]

    observer = threading.Thread(
        target=watch_progress,
        args=(results, sync_lock, expected_total)
    )

    observer.start()

    for worker in workers:
        worker.start()
        time.sleep(0.4)

    for worker in workers:
        worker.join()

    observer.join()

    print("\n✅ Final Results:", results)
    print("📊 Total Items Processed:", len(results))


if __name__ == "__main__":
    main()

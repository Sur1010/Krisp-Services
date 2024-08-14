from typing import Dict, Any, Tuple
import time


class Cache:
    def __init__(self, max_keys: int = 3, ttl: int = 10):
        self.cache: Dict[int, Tuple[Any, float]] = {}
        self.max_keys = max_keys
        self.ttl = ttl

    def get(self, key: int) -> Any:
        if key in self.cache:
            value, timestamp = self.cache[key]
            if time.time() - timestamp < self.ttl:
                return value
            else:
                self.delete(key)
        return None

    def set(self, key: int, value: Any):
        if len(self.cache) >= self.max_keys:
            self.evict()
        self.cache[key] = (value, time.time())

    def delete(self, key: int):
        if key in self.cache:
            del self.cache[key]

    def evict(self):
        # Evict the oldest item in the cache
        oldest_key = None
        oldest_time = float('inf')
        for key, (value, timestamp) in self.cache.items():
            if timestamp < oldest_time:
                oldest_time = timestamp
                oldest_key = key
        if oldest_key is not None:
            self.delete(oldest_key)


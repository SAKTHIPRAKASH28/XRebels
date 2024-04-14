from cachetools import TTLCache

cache = TTLCache(maxsize=100, ttl=600)


def get_from_cache(uid: str) -> list[str]:
    if uid in cache:
        return cache[uid]
    else:
        return []


def set_to_cache(uid: str, data: list[str]) -> None:
    if uid not in cache:
        cache[uid] = data
    else:
        cache[uid].extend(data)

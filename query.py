def find_first(items, predicate):
    return next(item for item in items if predicate(item))

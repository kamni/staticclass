def not_static(func):
    func.__notstatic__ = True
    return func

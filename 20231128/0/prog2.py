
class ctype(type):
    _first = None
    _second = None
    _fl = True

    def __call__(cls, *args, **kwargs):
        if first is None:
            first = super().__call__()(*args, **kwargs)
        elif second is None:
            second = super().__call__()(*args, **kwargs)
        _fl = not _fl

        return cls._first if cls._fl else cls._second

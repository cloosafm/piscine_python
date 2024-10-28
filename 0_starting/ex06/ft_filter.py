def ft_filter(function, iterable) -> iter:
    """ft_filter(function or None, iterable) --> filter object

    \rReturn an iterator yielding those items of iterable for \
    \b\b\b\bwhich function(item)
    \ris true. If function is None, return the items that are true."""
    if function is None:
        for item in iterable:
            if item:
                yield item
    else:
        for item in iterable:
            if function(item):
                yield item

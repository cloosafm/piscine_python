def ft_tqdm(lst: range) -> None:
    """Decorate an iterable object, returning an iterator which acts exactly
    like the original iterable, but prints a dynamically updating
    progressbar every time a value is requested.
    Args:
        lst (range): The iterable object to decorate.
    """

    total = len(lst)
    bar_length = 100
    for i, item in enumerate(lst):
        percent_complete = (i + 1) / total * 100
        num_bars = int(percent_complete * (bar_length / 100))
        bar = '|' + '█' * num_bars + ' ' * (bar_length - num_bars) + '| '
        print(f"\r{percent_complete:3.0f}%{bar}{i + 1}/{total}", end='')
        yield item
    print()

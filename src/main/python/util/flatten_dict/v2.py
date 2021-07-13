from typing import Iterator, Optional, Tuple, Union

Node = Optional[Union[bool, int, str]]
Path = Tuple[Node, ...]


iterators = {
    dict: dict.items,
    list: enumerate
}


def iter_paths(data) -> Iterator[Path]:
    if iterate := iterators.get(type(data)):
        for key, val in iterate(data):
            for path in iter_paths(val):
                yield (key,) + path
    else:
        yield data,


def flatten_dict(data: dict, separator: str = '/') -> dict:
    return {separator.join(map(str, path[0:-1])): path[-1] for path in iter_paths(data)}

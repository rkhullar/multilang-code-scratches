from typing import Iterator, Optional, Union

Node = Optional[Union[bool, int, str]]
Path = tuple[Node, ...]


iterators = {
    dict: dict.items,
    list: enumerate
}


def iter_paths(data) -> Iterator[Path]:
    queue: list[Path] = [(data,)]
    while queue:
        path: Path = queue.pop(0)
        node: Node = path[-1]
        if iterate := iterators.get(type(node)):
            for key, val in iterate(node):
                next_path = path[:-1] + (key, val)
                queue.append(next_path)
        else:
            yield path


def flatten_dict(data: dict, separator: str = '/') -> dict:
    return {separator.join(map(str, path[0:-1])): path[-1] for path in iter_paths(data)}

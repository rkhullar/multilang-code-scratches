from contextlib import contextmanager
from typing import List, Dict, Union, TypeVar

T = TypeVar('T')


def _list_get(data: List[T], idx: int) -> T:
    if 0 <= idx < len(data):
        return data[idx]


def _dict_get(data: Dict[str, T], key: str) -> T:
    if key in data:
        return data[key]


class GetItemView:
    def function(self, item):
        pass

    def __getitem__(self, item):
        return self.function(item)


@contextmanager
def silent(collection: Union[List, Dict]):
    view = GetItemView()
    if isinstance(collection, List):
        view.function = lambda idx: _list_get(collection, idx)
    elif isinstance(collection, Dict):
        view.function = lambda key: _dict_get(collection, key)
    yield view


if __name__ == '__main__':
    arr = [1, 2, 4]
    with silent(arr) as view:
        for i in range(-5, 5):
            print('arr', i, view[i])
    data = {'a': 1, 'c': 3}
    with silent(data) as view:
        print('map', 'a', view['a'])
        print('map', 'b', view['b'])

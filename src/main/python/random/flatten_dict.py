import json
from typing import Dict, Iterator, Tuple


def iter_dict_flatten(data, separator: str = '/') -> Iterator[Tuple[str, str]]:
    if isinstance(data, (str, int, bool)) or data is None:
        yield None, data
    elif isinstance(data, dict):
        for key, val in data.items():
            for sub_key, sub_val in iter_dict_flatten(val, separator):
                key_parts = filter(None, [key, sub_key])
                yield separator.join(key_parts), sub_val
    elif isinstance(data, list):
        for idx, item in enumerate(data):
            for sub_key, sub_val in iter_dict_flatten(item, separator):
                key_parts = filter(None, [str(idx), sub_key])
                yield separator.join(key_parts), sub_val


def flatten_dict(data, separator: str = '/') -> Dict[str, str]:
    return {key: val for key, val in iter_dict_flatten(data, separator)}


if __name__ == '__main__':
    data = {
        'a': {'b': {'c': 'd'}},
        'w': ['x', {'y': 'z'}]
    }
    data = flatten_dict(data)
    print(json.dumps(data, indent=4, sort_keys=True))

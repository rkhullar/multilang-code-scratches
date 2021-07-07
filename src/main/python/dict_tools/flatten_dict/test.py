from v1 import flatten_dict
import json

test_input = {
    'a': {
        'b': {
            'c': 'd'
        }
    },
    'w': [
        'x',
        {
            'y': 'z'
        }
    ]
}

test_output = {
    'a/b/c': 'd',
    'w/0': 'x',
    'w/1/y': 'z'
}


def to_json(data: dict):
    return json.dumps(data, indent=4, sort_keys=True)


print(to_json(test_input))
result = flatten_dict(test_input, separator='/')
assert to_json(test_output) == to_json(result)

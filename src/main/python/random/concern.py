from typing import List, Optional, Union


class Concern:
    # https://stackoverflow.com/questions/8601268/class-that-acts-as-mapping-for-unpacking

    def keys(self) -> List[str]:
        return ['message', 'count']

    def __getitem__(self, key: str) -> Optional[Union[str, int]]:
        if key == 'message':
            return 'hello world'
        elif key == 'count':
            return 4

    def __call__(self) -> 'Concern':
        return self


def doit(message: str, count: int = 1):
    for _ in range(count):
        print(message)


if __name__ == '__main__':
    concern = Concern()
    doit(**concern)

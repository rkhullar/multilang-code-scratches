import functools
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import Callable, Dict, List, Type


@dataclass
class RetryFactory(ABC):

    attempts: int
    errors: List[Type[Exception]] = field(default_factory=list)

    def __post_init__(self):
        assert self.attempts > 0

    @abstractmethod
    def main(self, *args, **kwargs):
        pass

    def handle_expected(self, attempt: int):
        pass

    def handle_uncaught(self, attempt: int):
        pass

    def handle_exhaust(self):
        pass

    def __call__(self, *args, **kwargs):
        for i in range(self.attempts):
            # NOTE: although to_raise isn't defined before the loop; it's defined at least once
            to_raise = None  # noqa
            try:
                return self.main(*args, **kwargs)
            except tuple(self.errors) as err:
                to_raise = err
                self.handle_expected(i)
            except Exception as err:
                self.handle_uncaught(i)
                raise err
        else:
            self.handle_exhaust()
            raise to_raise  # noqa


def retry(attempts: int, errors: List[Type[Exception]], hooks: Dict[str, Callable]):
    def decorator(fn):
        class ChildRetry(RetryFactory):
            def main(self, *args, **kwargs):
                return fn(*args, **kwargs)
        retry_object = ChildRetry(attempts=attempts, errors=errors)
        for key in 'expected', 'uncaught', 'exhaust':
            if key in hooks:
                setattr(retry_object, f'handle_{key}', hooks[key])
        retry_object = functools.wraps(fn)(retry_object)
        return retry_object
    return decorator

from unittest import TestCase
from nose.tools import assert_equal, assert_raises
from util.retry import retry


class RetryTest(TestCase):

    def test_decorator_with_hook(self):
        error_messages = list()

        def example_hook(attempt: int):
            error_messages.append(f'inside hook {attempt}')

        @retry(attempts=2, errors=[ZeroDivisionError], hooks=dict(expected=example_hook))
        def compute(a: int, b: int, fail: bool = False):
            """hello world"""
            if fail:
                raise ValueError
            return a / b

        # metadata
        assert_equal(compute.__name__, 'compute')
        assert_equal(compute.__doc__, 'hello world')

        # non error flow
        assert_equal(compute(6, 3), 2)

        # exp error flow
        with assert_raises(ZeroDivisionError):
            compute(6, 0)

        assert_equal(len(error_messages), 2)
        assert_equal(error_messages[0], 'inside hook 0')
        assert_equal(error_messages[1], 'inside hook 1')

        # bad error flow
        with assert_raises(ValueError):
            compute(1, 1, fail=True)

'''
A test example using the Hypothesis library and property-based testing.

pip install hypothesis

Read more here: https://hypothesis.readthedocs.io/en/latest/

Contact Richard if you have questions.
'''


# hypothesis functions
from hypothesis import given, strategies as st

# simple function
def sum(x, y):
    return x + y


# unit test 01
# test multiple float values
@given(st.floats, st.floats)
def test_sum(x, y):
    assert sum(x, y) == x + y


# unit test 02
# test multiple integers
@given(st.integers, st.integers)
def test_sum(x, y):
    assert sum(x, y) == x + y
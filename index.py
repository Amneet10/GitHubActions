# app.py
# This is a test commit
# this is for testing GithubActions
def add(a, b):
    return a + b

def test_add():
    assert add(1, 2) == 3
    assert add(1, -1) == 0
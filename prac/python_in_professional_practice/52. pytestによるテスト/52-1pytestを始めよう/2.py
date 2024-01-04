# pytest test_myapp.pyで実行

from myapp import hello

def test_hello_1():
    s = hello("Alice")
    assert s == "Hello Alice!"

def test_hello_2():
    s = hello("Bob")
    assert s == "Hello Bob!"
import os

from pysu.cli import main


def test_unknown_user():
    assert main(["foo:bar", "echo"]) == 1


def test_unknown_group():
    assert main([f"{os.getuid()}:foobar", "echo"]) == 2


def test_no_perm_user():
    assert main([f"0:{os.getgid()}", "echo"]) == 3


def test_no_perm_group():
    assert main([f"{os.getuid()}:0", "echo"]) == 3

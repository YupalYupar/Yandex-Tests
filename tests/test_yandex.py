import pytest
from main_ya import create_folder, check_folder


def test_create_folder():
    assert create_folder('boogy').status_code == 201 or create_folder('boogy').status_code == 409


def test_check_folder():
    assert check_folder('boogy').status_code == 200




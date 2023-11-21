import pytest


@pytest.mark.chek
def test_name(user):
    assert user.name == 'Olga'

@pytest.mark.chek
def test_second_name(user):
    assert user.second_name == 'Savrol'
import pytest


@pytest.mark.api
def test_user_exists_login(github_api):
    user = github_api.get_user(username = 'defunkt')
    assert user["login"] == "defunkt"

@pytest.mark.api
def test_user_exists_bio(github_api):
    user = github_api.get_user(username = 'OlgaSavr')
    assert user["bio"] == "my bio ❤"

@pytest.mark.api
def test_user_exists_name(github_api):
    user = github_api.get_user(username = 'OlgaSavr')
    assert user["name"] == "Olga"

@pytest.mark.api
def test_not_user_exists(github_api):
    user2 = github_api.get_user(username = 'butenkosergii')
    assert user2["message"] == "Not Found"
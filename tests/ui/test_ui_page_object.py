from modules.ui.page_objects.sign_in_page import SignInPage
from modules.ui.page_objects.contact_page import Write_and_send
from modules.ui.page_objects.search_page import Search
import pytest
import time

@pytest.mark.ui
def test_check_incorect_username_page_odject():
    sign_in_page = SignInPage()

    sign_in_page.go_to()

    sign_in_page.try_login("page@object.com", "wrongpassword")

    assert sign_in_page.check_title("Sign in to GitHub · GitHub")

    sign_in_page.close()

@pytest.mark.ui
def test_send_contact():
    sending = Write_and_send()

    sending.go_to()

    sending.write('savrol18@gmail.com', 'Ds2023')

    sending.send()

    sending.check_title("Мої курси")

    sending.close()

@pytest.mark.ui
def test_search():    
    searcing = Search()

    searcing.go_to()

    searcing.search()
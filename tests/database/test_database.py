import pytest
from modules.common.database import Database


@pytest.mark.database
def test_database_connection():
    db = Database()
    db.test_conection()
    print(db)

@pytest.mark.database
def test_database_users():
    db = Database()
    users = db.get_all_users()
    print(users)

@pytest.mark.database
def test_product_qnt_update():
    db = Database()
    a = db.update_product_qnt_by_id(1, 15)
    b = db.get_product_qnt_by_id(1)
    chek = int(b[0][0])
    assert a + 15 == chek

@pytest.mark.database
def test_product_insert():
    db = Database()
    db.create_product(4, 'cokie', 'chokolate', 30)
    chek = db.get_product_qnt_by_id(4)
    assert chek [0][0] == 30

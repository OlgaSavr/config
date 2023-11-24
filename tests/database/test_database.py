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

@pytest.mark.database
def test_product_delete():
    db = Database()
    db.create_product(99, 'test', 'information', 99)
    db.delete_product_by_id(99)
    chek = db.get_product_qnt_by_id(99)
    assert len(chek) == 0

@pytest.mark.database
def test_detailed_orders():
    db = Database()
    order = db.get_detailed_orders()
    print(f'Замовлення {order}')
    assert len(order) == 1

    assert order[0][0] == 1
    assert order[0][1] == 'Sergii'
    assert order[0][2] == 'солодка вода'
    assert order[0][3] == 'з цукром'

def test_product_create():
    db = Database()
    db.create_product(5, 'Вода не газована', 'морщинська природна', 10)
    chek = db.get_product_qnt_by_id(5)
    assert chek [0][0] == 10

def test_product_create2():
    db = Database()
    db.create_product(6, 'данні', 'які потрібно видалити', 0)
    chek = db.get_product_qnt_by_id(6)
    assert chek [0][0] == 0

def test_product_create3():
    db = Database()
    db.create_product(7, 'желейні ведмедики', 'haribo', 15)
    chek = db.get_product_qnt_by_id(7)
    assert chek [0][0] == 15

@pytest.mark.database
def test_product_qnt_update2():
    db = Database()
    a = db.update_product_qnt_by_id(2, 20)
    b = db.get_product_qnt_by_id(2)
    chek = int(b[0][0])
    assert a + 20 == chek

@pytest.mark.database
def test_product_qnt_update3():
    db = Database()
    a = db.update_product_qnt_by_id(3, 5)
    b = db.get_product_qnt_by_id(3)
    chek = int(b[0][0])
    assert a + 5 == chek

@pytest.mark.database
def test_product_delete2():
    db = Database()
    db.delete_product_by_id(6)
    chek = db.get_product_qnt_by_id(6)
    assert len(chek) == 0

@pytest.mark.database
def test_product_delete3():
    db = Database()
    db.create_product(8, 'кінь', 'не крадений', 1)
    db.delete_product_by_id(8)
    chek = db.get_product_qnt_by_id(8)
    assert len(chek) == 0

@pytest.mark.database
def test_getting_Stepan():
    db = Database()
    print(db.get_user_address_by_name('Stepan'))
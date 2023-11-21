import sqlite3

class Database():
    
    def __init__(self):
        self.connection = sqlite3.connect('C://Users//HP 650 G1//Desktop//repositi1' + '//become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_conection(self):
        sqlite_select_Query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_Query)
        record = self.cursor.fetchall()
        print(f"Conected sucsessfully. SQLite databese version is: {record}")
    
    def get_all_users(self):
        qerry = 'SELECT name, address, city FROM customers'
        self.cursor.execute(qerry)
        record = self.cursor.fetchall()
        return record
    
    def get_user_address_by_name(self, name):
        qerry = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(qerry)
        record = self.cursor.fetchall()
        return record
    
    def update_product_qnt_by_id(self, product_id, qnt):
        qerry = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(qerry)
        record = self.cursor.fetchall()
        a = int(record[0][0])
        query = f"UPDATE products SET quantity = {qnt + a} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()
        return a
 
    def get_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
    
    def create_product(self, product_id, name, description, quantity):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) VALUES ({product_id}, '{name}', '{description}', {quantity})"
        self.cursor.execute(query)
        self.connection.commit

    def get_craeted_product(self, product_id):
        query = f"SELECT id, name, decription, quantity WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

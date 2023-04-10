import os
import sqlite3

from typing import List, Set


def execute_query(query_sql: str) -> List:
    '''
    Функция для выполнения запроса
    :param query_sql: запрос
    :return: результат выполнения запроса
    '''
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    connection = sqlite3.connect(db_path)
    cur = connection.cursor()
    result = cur.execute(query_sql).fetchall()
    connection.close()
    return result


def unwrapper(records: List) -> None:
    '''
    Функция для вывода результата выполнения запроса
    :param records: список ответа БД
    '''
    for record in records:
        print(*record)


# Функция формирования списка:
def get_unique_customers():
    query_sql = '''
        SELECT FirstName
          FROM customers;
    '''
    names = execute_query(query_sql)
    unique_names = list()
    for name in names:
        unique_names.append(name[0])
    return unique_names


result = get_unique_customers()
#print(result)


# Функция сортировки и печати повторений имени:
def sort():
    for el in result:
        if rez.get(el, None):
            rez[el] += 1
            print(el, rez[el])
        else:
            rez[el] = 1


rez = {}
sort()


# Функция подсчета прибыли по таблице invoice_items:
def get_orders_amount() -> int:
    '''
    сумма заказов по таблице invoice_items
    '''
    query_sql = f'''
        SELECT UnitPrice
              ,Quantity
          FROM invoice_items;
    '''
    orders = execute_query(query_sql)
    total_amount = 0
    for order in orders:
        total_amount += order[0] * order[1]

    return round(total_amount, 2)


print('Сумма по заказу: ', get_orders_amount())

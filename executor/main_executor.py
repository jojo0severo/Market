import sqlite3

_db = sqlite3.connect("database_data/mercearia.db")


def init():
    try:
        _db.executescript(open('database_data/db.sql', 'r', encoding='utf-8').read())
        _db.commit()
        return 1
    except sqlite3.OperationalError:
        return 2
    except:
        return 3


def insert(info):
    if info['table'].lower() in ['ano', 'mes']:
        query = 'insert into ' + info['table'] + ' values(' + ','.join(info['values']) + ');'
    else:
        query = 'insert into ' + info['table'] + ' values(null,' + ','.join(info['values']) + ');'

    try:
        _db.executescript(query)
        _db.commit()
        return 1
    except sqlite3.IntegrityError:
        return 2
    except:
        return 3


def drop_all():
    query = 'drop table if exists compra; ' \
            'drop table if exists venda; ' \
            'drop table if exists mes; ' \
            'drop table if exists ano;'

    try:
        _db.executescript(query)
        _db.commit()
        return True
    except:
        return False


def select_list(info):
    query = 'select valor from ' + info['table'] + ' \ninner join mes \n\ton mes.nome_mes = ' + \
            info['table'] + '.nome_mes and mes.nome_ano = ' + info['table'] + '.nome_ano' \
                                                                              ' \n\tinner join ano \n\t\ton ano.nome_ano = mes.nome_ano' \
                                                                              '\nwhere mes.nome_mes = ' + info[
                'mes'] + ' and ano.nome_ano = ' + info['ano'] + ';'

    c = _db.cursor()
    return c.execute(query).fetchall()


def select_total(info):
    query = 'select sum(valor) from ' + info['table'] + ' \ninner join mes \n\ton mes.nome_mes = ' + \
            info['table'] + '.nome_mes and mes.nome_ano = ' + info['table'] + '.nome_ano' \
                                                                              ' \n\tinner join ano \n\t\ton ano.nome_ano = mes.nome_ano' \
                                                                              '\nwhere mes.nome_mes = ' + info[
                'mes'] + ' and ano.nome_ano = ' + info['ano'] + ';'

    c = _db.cursor()
    return c.execute(query).fetchall()[0][0]


def select_profit(info):
    from decimal import Decimal
    from decimal import getcontext

    getcontext().prec = 50

    query_compras = 'select sum(valor) from compra inner join mes ' \
                    ' on mes.nome_mes = compra.nome_mes and mes.nome_ano = compra.nome_ano' \
                    ' inner join ano on ano.nome_ano = mes.nome_ano' \
                    ' where mes.nome_mes = ' + info['month'] + ' and ano.nome_ano = ' + info['year'] + ';'

    query_vendas = 'select sum(valor) from venda inner join mes ' \
                   ' on mes.nome_mes = venda.nome_mes and mes.nome_ano = venda.nome_ano' \
                   ' inner join ano on ano.nome_ano = mes.nome_ano' \
                   ' where mes.nome_mes = ' + info['month'] + ' and ano.nome_ano = ' + info['year'] + ';'

    c = _db.cursor()
    try:
        return Decimal(c.execute(query_vendas).fetchall()[0][0]) - Decimal(c.execute(query_compras).fetchall()[0][0])
    except TypeError:
        return 0
    except:
        return 'Erro'


def direct_query(query):
    try:
        return _db.cursor().execute(query).fetchall()[0]
    except:
        return 0


def delete_last_insert():
    delete_purchase = 'DELETE FROM compra WHERE id = (SELECT MAX(id) FROM compra);'
    delete_sale = 'DELETE FROM venda WHERE id = (SELECT MAX(id) FROM venda);'

    try:
        _db.executescript(delete_purchase)
        _db.executescript(delete_sale)
        return 1
    except:
        return 2


def close():
    _db.close()

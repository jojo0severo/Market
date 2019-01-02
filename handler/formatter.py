from datetime import datetime
import json


# ================================ Patterns ====================================
# insert       = {'table': table_name, 'values'  : [field1, field2, etc]}
# select list  = {'table': table_name, 'month'   : month_name, 'year': year_name}
# select total = {'table': table_name, 'month'   : month_name, 'year': year_name}
# select lucro = {'month': month_name, 'year'    : year_name}

labels = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']


def format_insert(sales, purchases, month=None, year=None):
    if not month:
        month = str(datetime.now().month)
    if not year:
        year = str(datetime.now().year)

    info = {
        'insert_1': {
            'table': 'Ano',
            'values': [str(year)]
        },
        'insert_2': {
            'table': 'Mes',
            'values': [str(month), str(year)]
        },
        'insert_3': {
            'table': 'Compra',
            'values': [str(purchases), str(month), str(year)]
        },
        'insert_4': {
            'table': 'Venda',
            'values': [str(sales), str(month), str(year)]
        }
    }

    return info


def format_cache(sales, purchases):
    info = {
        'insert_1': {
            'table': 'Compra',
            'values': [purchases[0], purchases[1], purchases[2]]
        },
        'insert_2': {
            'table': 'Venda',
            'values': [sales[0], sales[1], sales[2]]
        }
    }

    return info


def format_consult(profit, table=None):
    if profit:
        info = {
            'month': str(datetime.now().month),
            'year': str(datetime.now().year)
        }

    else:
        info = {
            'table': table,
            'month': str(datetime.now().month),
            'year': str(datetime.now().year)
        }

    return info


def format_x_labels():
    current_month = datetime.now().month-2
    current_year = datetime.now().year

    months = []

    for i in range(12):
        label = labels[current_month-1] + '\n' + str(current_year)
        months.append(label)

        if current_month - 1 == 0:
            current_month = 12
            current_year -= 1
        else:
            current_month -= 1

    return months


def format_y_consult(x_labels):
    months = [labels.index(x.split('\n')[0])+1 for x in x_labels]
    years = list(sorted(set([x.split('\n')[1] for x in x_labels])))

    query = "{"

    for i in range(12):
        if months[i] == 12:
            years.pop()

        query += "\"consult_" + str(i+1) + "\":"
        query += "{\"month\":\"" + str(months[i]) + "\","
        query += "\"year\":\"" + str(years[len(years)-1]) + "\"},"

    query = query[:-1]
    query += "}"

    return json.loads(query)


def format_number(n):
    coins = str(0)
    n = str(n)
    try:
        response = list(n.split('.')[0])
        coins = n.split('.')[1]
    except:
        response = list(str(n))

    aux = []
    if len(response) > 3:
        response.reverse()
        for i in range(len(response)):
            if i % 3 == 0 and i != 0:
                aux.append('.')
            aux.append(response[i])
        aux.reverse()
    else:
        aux.extend(response)

    if coins:
        if len(coins) == 1:
            coins += str(0)
        aux.append(',')
        aux.append(coins)
    else:
        aux.append(',00')

    return ''.join(aux)

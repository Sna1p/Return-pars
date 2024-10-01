def district(x):
    dist = {
        'district': 'district'
        'district2': 'district'
    }
    arr = list(range(0, len(x)))    # задаем длинну массива 
    for i in range(0, len(x)):
        arr[i] = dist.get(str(x[i]))  # меняем Rvk на dist
    return arr

def StafType(x):
    Staf = {
        '1': 'Невролог',
        '2': 'Хирург',
        '3': 'Стоматолог',
        '4': 'ЛОР',
        '5': 'Окулист',
        '6': 'Психиатр',
        '7': 'Дермотолог',
        '8': 'Терапевт',
        '9': 'Секретариат',
        '10': 'Мед. сестра',
        }
    arr = list(range(0, len(x)))
    for i in range(0, len(x)):
        arr[i] = Staf.get(str(x[i]))
    return arr

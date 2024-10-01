
import multiprocessing
import datetime


def read_info(name):
    all_data = []
    file = open(name, 'r', encoding='utf8')
    stroka = None
    while stroka != '':
        stroka = file.readline()
        if stroka != '':
            all_data.append(stroka)
    file.close()


filenames = [f'./file {number}.txt' for number in range(1, 5)]

if __name__ == '__main__':
    # Линейный вызов
    start = datetime.datetime.now()
    for filename in filenames:
        read_info(filename)
    end = datetime.datetime.now()
    print(f'{end - start} (линейный)')

    # Многопроцессный вызов
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=6) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(f'{end - start} (многопроцессный)')

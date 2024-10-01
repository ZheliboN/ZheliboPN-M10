from threading import Thread
import queue
from time import sleep
from random import randint


class Table:
    def __init__(self, number):
        self.number = number
        self.guest = None


class Guest(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.table = None

    def run(self):
        second = randint(3, 10)
        sleep(second)


class Cafe:

    def __init__(self, *ltables):
        self.tables = list(ltables)
        self.queue = queue.Queue()
        '''
        #self.list_thread = []
        '''

    def buzy_table(self):
        table_is_byzy = False
        for table in self.tables:
            if not table.guest is None:
                table_is_byzy = True
        return table_is_byzy

    def guest_arrival(self, *lguests):
        """
        #self.list_thread = []
        """
        for guest in lguests:
            for table in self.tables:
                if table.guest is None and guest.table is None:
                    table.guest = guest
                    guest.table = table
                    guest.start()
                    '''
                    #self.list_thread.append(guest)
                    '''
                    print(f'{table.guest.name} сел(-а) за стол номер {table.number}')
            if guest.table is None:
                self.queue.put(guest)
                print(f'{guest.name} в очереди')

    def discuss_guests(self):
        table_buzy = True
        while not self.queue.empty() or table_buzy:
            table_buzy = Cafe.buzy_table(self)
            for table in self.tables:
                if not (table.guest is None) and not (table.guest.is_alive()):
                    print(f'{table.guest.name} покушал(-а) и ушел(ушла)')
                    print(f'Cтол номер {table.number} свободен')
                    table.guest.table = None
                    table.guest = None
                if not (self.queue.empty()) and table.guest is None:
                    table.guest = self.queue.get()
                    print(f'{table.guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}')
                    table.guest.start()
                    '''
                    #self.list_thread.append(table.guest)
                    '''
        '''
        #проверка на обслуживание всех гостей
        for table in self.tables:
            print(f'Стол {table.number} гость {table.guest}')
        print(f'Очередь гостей пустая {self.queue.empty()}')
        '''


tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = ['Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman', 'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya',
                'Alexandra']

# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()
'''
#for thr in cafe.list_thread:
#   thr.join()
'''
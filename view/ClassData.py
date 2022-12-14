import pprint


class Data:
    time_list = [
        '8:00', '10:00',
        '12:00', '14:00',
        '16:00', '18:00'
    ]

    def __init__(self, data, number_lesson, weekday):
        """
        :param data: Входной json file
        :param number_lesson: порядковый номер пары
        :param weekday: день недели начиная с понедельника
        т.е 8:00 - 9:40 - 0 Пара
        10:00 - 11:49 1 пара и т.д.
        """
        self.data = data
        self.number_lesson = number_lesson
        self.weekday = weekday
        self.date = ''
        self.time_start = ''
        self.time_end = ''
        self.typeObj = ''
        self.nameObj = ''
        self.nameTeach = ''
        self.auditories = ''
        self.get_all()

    def get_all(self):
        print('Connection')
        # get  date in json
        for date in self.data['days']:
            if date['weekday'] == self.weekday:
                self.date = date['date']
                print(date['lessons'][self.number_lesson]['time_start'])
                # if date['lessons']['time_start'] in Data.time_list[self.number_lesson]:
                self.time_start = date['lessons'][self.number_lesson]['time_start']
                self.time_end = date['lessons'][self.number_lesson]['time_end']
                self.typeObj = date['lessons'][self.number_lesson]["typeObj"]["name"]
                self.nameObj = date['lessons'][self.number_lesson]["subject"]
                self.nameTeach = date['lessons'][self.number_lesson]["teachers"][0]["full_name"]
                self.auditories = f'i{date["lessons"][self.number_lesson]["auditories"][0]["building"]["name"]} аудитория {date["lessons"][self.number_lesson]["auditories"][0]["name"]}'
                print(self.nameObj)
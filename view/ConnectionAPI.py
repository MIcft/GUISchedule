import http.client
import json
from pprint import pprint


class ConnectionApi:
    def __init__(self, group_name):
        self.group_id = None
        self.group_name = group_name
        self.ans_dict = None

    def get_group_id_by_name(self):
        server_address = "ruz.spbstu.ru"
        request = f'/api/v1/ruz/search/groups?&q={self.group_name}'
        connection = http.client.HTTPSConnection(server_address)
        connection.request('GET', request)
        response = connection.getresponse()
        ans = response.read()
        connection.close()
        self.group_id = json.loads(ans)['groups'][1]['id']


    def get_schedule_by_id(self):
        server_address = "ruz.spbstu.ru"
        request = f'https://ruz.spbstu.ru/api/v1/ruz/scheduler/{self.group_id}'
        connection = http.client.HTTPSConnection(server_address)
        connection.request('GET', request)
        response = connection.getresponse()
        ans = response.read()
        connection.close()
        self.ans_dict = json.loads(ans)



if __name__ == '__main__':
    group_name = input('Введите ваш номер группы:')
    group_id = get_group_id_by_name(group_name)
    schedule = get_schedule_by_id(group_id)
    pprint(schedule)
    # with open(f'{group_id}.txt', 'w', encoding='UTF-8') as file:
    #     file.write(str(schedule))

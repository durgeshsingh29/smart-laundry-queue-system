from database import get_queue

AVERAGE_WASH_TIME = 30


def calculate_waiting_time(machine_name):
    queue = get_queue(machine_name)

    people_waiting = len(queue)

    estimated_time = people_waiting * AVERAGE_WASH_TIME

    return people_waiting, estimated_time


def get_position(student_id, machine_name):
    queue = get_queue(machine_name)

    for position, item in enumerate(queue, start=1):
        if item[1] == student_id:
            return position

    return None
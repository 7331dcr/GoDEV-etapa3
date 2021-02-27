from .models import Event_room, Coffee_space, Attendee

def count_max_attendees():
    query_smallest_room = Event_room.objects.all().order_by('capacity').first()
    smallest_room_capacity = int(query_smallest_room.capacity)
    number_of_rooms = Event_room.objects.all().count()
    max_attendees = smallest_room_capacity * number_of_rooms + (number_of_rooms - 1)
    
    return max_attendees


def find_emptier_room():
    rooms = Event_room.objects.all()
    emptier_room = None
    index = 0
    for i in range(len(rooms)):
        if rooms[i].room1_assigneds.count() < rooms[index].room1_assigneds.count():
            index = i
        emptier_room = rooms[index]

    return emptier_room


def find_second_room(available_rooms):
    emptier_room = None
    index = 0
    for i in range(len(available_rooms)):
        if available_rooms[i].room2_assigneds.count() < available_rooms[index].room2_assigneds.count():
            index = i
        emptier_room = available_rooms[index]
    
    return emptier_room


def define_coffee_space(current_attendees):
    assigned_space = Coffee_space.objects.all()
    if current_attendees % 2 != 0:
        assigned_space = assigned_space.first()
    else:
        assigned_space = assigned_space.last()

    return assinged_space


def define_room_etapa2():
    current_attendees = Attendee.objects.all().count()
    if current_attendees % 2 != 0:
        emptier_room = find_emptier_room()
    else:
        emptier_room = find_emptier_room()
        available_rooms = Event_room.objects.exclude(name=emptier_room.name)
        emptier_room = find_second_room(available_rooms)

    return emptier_room
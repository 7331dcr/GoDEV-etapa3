from django.http import HttpResponseRedirect
from django.template import Context, Template
from django.shortcuts import render
from django.urls import reverse
from .models import Event_room, Coffee_space, Attendee



def index(request):
    return render(request, "manager/index.html")

def cadastro(request):
    if len(Event_room.objects.all()) < 1:
        return HttpResponseRedirect(reverse("pre_cadastro_sala"))
    
    if len(Coffee_space.objects.all()) < 2:
        return HttpResponseRedirect(reverse("cadastro_cafe"))


    if request.method == "POST":
        name = request.POST['name']
        last_name = request.POST['last_name']
        if not name or not last_name:
            return render(request, "manager/cadastro.html", {
                "message": f'Cadastro não efetuado. NOME ou SOBRENOME inválidos.'
            })
        
        # capacidade maxima de participantes:
        query_smallest_room = Event_room.objects.all().order_by('capacity').first()
        smallest_room_capacity = int(query_smallest_room.capacity)
        number_of_rooms = Event_room.objects.all().count()
        max_attendees = smallest_room_capacity * number_of_rooms + (number_of_rooms - 1)
        print(max_attendees)

        # quantidade de participantes já cadastrados
        attendees_qnt = Attendee.objects.all().count()
        print(attendees_qnt)

        if max_attendees > attendees_qnt:
            
            print('ok')
            # encontra a sala com menor quantidade de prticipantes
            rooms = Event_room.objects.all()
            emptier_room = None
            index = 0
            for i in range(len(rooms)):
                if rooms[i].room_assigneds.count() < rooms[index].room_assigneds.count():
                    index = i
                emptier_room = rooms[index]
            print(emptier_room)

            # designa espaço para café
            assigned_space = Coffee_space.objects.all()
            if attendees_qnt % 2 != 0:
                assigned_space = assigned_space.first()
            else:
                assigned_space = assigned_space.last()

            new_entry = Attendee(name=name, last_name=last_name, event_room=emptier_room, coffee_space=assigned_space)
            new_entry.save()
            print(new_entry)

        return render(request, "manager/cadastro.html", {
            "message": f'Participante "{name} {last_name}" foi cadastrado com sucesso.'
        })

    return render(request, "manager/cadastro.html")

def pre_cadastro_sala(request):
    if len(Event_room.objects.all()) > 0:
        return HttpResponseRedirect(reverse("cadastro_sala"))
        
    if request.method == "POST":

        pass
    return render(request, "manager/pre_cadastro_sala.html")

def cadastro_sala(request):
    # Show's only current event rooms if they were already created
    rooms = Event_room.objects.all()
    if len(rooms) > 0:
        rooms_list = []
        for room in range(len(rooms)):
            rooms_list.append(f'Sala "{rooms[room].name}". Capacidade: {rooms[room].capacity}')
        return render(request, "manager/cadastro_sala.html", {
            "rooms": rooms_list
        })
    
    # Handles number of event room forms
    forms_quantity = 0
    number_list = []
    if request.method == "GET":
        forms_quantity = int(request.GET.get('quantity', ''))
        for i in range(forms_quantity):
            number_list.append(i)

    if request.method == "POST":
        rooms_quantity = int(request.POST['quantity'])
        for i in range(rooms_quantity):
            name = request.POST[f'name{i}']
            capacity = request.POST[f'capacity{i}']
            if not name or not capacity:
                # Returns error message
                return render(request, "manager/pre_cadastro_sala.html", {
                    "message": f'Cadastro não efetuado. NOME ou LOTAÇÃO MÁXIMA inválidos.',
                })
            new_entry = Event_room(name=name, capacity=capacity)
            new_entry.save()
        return HttpResponseRedirect(reverse("cadastro"))

    return render(request, "manager/cadastro_sala.html", {
        "number_list": number_list,
        "quantity": forms_quantity
    })

def cadastro_cafe(request):
    spaces = Coffee_space.objects.all()
    if len(spaces) > 0:
        spaces_list = []
        for space in range(len(spaces)):
            spaces_list.append(f'Espaço "{spaces[space].name}". Capacidade: {spaces[space].capacity}')
        return render(request, "manager/cadastro_cafe.html", {
            "spaces": spaces_list
        })
    
    if request.method == "POST":
        name1 = request.POST['name1']
        capacity1 = request.POST['capacity1']
        name2 = request.POST['name2']
        capacity2 = request.POST['capacity2']
        
        if not name1 or not capacity1 or not name2 or not capacity2:
            return render(request, "manager/cadastro_cafe.html", {
                "message": f'Cadastro não efetuado. NOME ou LOTAÇÃO MÁXIMA inválidos.'
            })

        spaces.delete()
        new_entry1 = Coffee_space(name=name1, capacity=capacity1)
        new_entry2 = Coffee_space(name=name2, capacity=capacity2)
        new_entry1.save()
        new_entry2.save()
        
        return HttpResponseRedirect(reverse("cadastro"))

    return render(request, "manager/cadastro_cafe.html")


def consulta(request):
    attendees = Attendee.objects.all()
    
    # # temporario
    # attendees_list = []
    # for attendee in range(len(attendees)):
    #     attendees_list.append(f'"{attendees[attendee].name}{attendees[attendee].last_name}"')
    
    if request.method == "POST":
        name = request.POST['name']
        last_name = request.POST['last_name']
        
        if not name or not last_name:
            return render(request, "manager/cadastro.html", {
                "message": f'NOME ou SOBRENOME inválidos.'
            })

        query = Attendee.objects.filter(name=name, last_name=last_name)

        return render(request, "manager/consulta.html", {
            "attendees": query
        })
    
    return render(request, "manager/consulta.html", {
        # "attendees": attendees_list
    })

def consulta_sala(request):
    rooms = Event_room.objects.all()
    rooms_list = []
    for room in range(len(rooms)):
        rooms_list.append(rooms[room])

    if request.method == "POST":
        name = request.POST['name']
        
        if not name or not last_name:
            return render(request, "manager/cadastro.html", {
                "message": f'NOME ou SOBRENOME inválidos.'
            })
        
        query = Attendee.objects.filter(event_room=Event_room.objects.get(name=name))
        print(query)
        return render(request, "manager/consulta_sala.html", {
            "attendees": query,
            "room_name": name
        })
    
    return render(request, "manager/consulta_sala.html", {
        "rooms": rooms_list
    })

def consulta_cafe(request):
    spaces = Coffee_space.objects.all()
    spaces_list = []
    for space in range(len(spaces)):
        spaces_list.append(spaces[space])

    if request.method == "POST":
        name = request.POST['name']
        
    #     if not name or not last_name:
    #         return render(request, "manager/cadastro.html", {
    #             "message": f'NOME ou SOBRENOME inválidos.'
    #         })

        query = Attendee.objects.filter(coffee_space=Coffee_space.objects.get(name=name))
        print(query)
        return render(request, "manager/consulta_cafe.html", {
            "attendees": query,
            "room_name": name
        })
    
    return render(request, "manager/consulta_cafe.html", {
        "spaces": spaces_list
    })

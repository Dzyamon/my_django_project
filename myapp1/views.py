from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from myapp1.models import Worker


def index(request):
    # new_worker = Worker(name='Хр', second_name='Морж', salary=100)
    # new_worker.save()
    # #v2
    # Worker.objects.create(name='Хр', second_name='Морж', salary=101)

    # worker_to_change = Worker.objects.get(id=5)
    # worker_to_change.second_name = 'Дрищ'
    # worker_to_change.save()
    # #v2
    # Worker.objects.filter(id=5).update(name='Уася')

    # Worker.objects.get(id=6).delete()
    #
    # all_workers = Worker.objects.all()
    # workers_filter = Worker.objects.filter(salary=222)

    # for i in all_workers:
    #     print(i)
    return HttpResponse("<h2>Главная</h2>")

def index1(request):
    all_workers = Worker.objects.all()
    return render(request, 'index.html', {'data': all_workers})

def index2(request):
    host = request.META["HTTP_HOST"]  # получаем адрес сервера
    path = request.path  # получаем запрошенный путь
    user_agent = request.META["HTTP_USER_AGENT"]  # получаем данные бразера
    return HttpResponse(f"""
        <p>Host: {host}</p>
        <p>Path: {path}</p>
        <p>User-agent: {user_agent}</p>
    """)

def index3(request):
    return JsonResponse({"name": "Tom", "age": 38})

def about(request, name, age):
    return HttpResponse(f"""
            <h2>О пользователе</h2>
            <p>Имя: {name}</p>
            <p>Возраст: {age}</p>
    """)

def contact(request):
    return HttpResponse("Контакты")

def user(request, name="Undefined", age =0):
    return HttpResponse(f"Имя:{name}, Возраст:{age}")

def user2(request):
    age = request.GET.get("age", 0)
    name = request.GET.get("name", "Undefined")
    return HttpResponse(f"Имя:{name}, Возраст:{age}")

def products(request, id):
    return HttpResponse(f"Товар {id}")

def new(request):
    return HttpResponse("Новые товары")

def top(request):
    return HttpResponse("Наиболее популярные товары")

def comments(request, id):
    return HttpResponse(f"Комментарии о товаре {id}")

def questions(request, id):
    return HttpResponse(f"Вопросы о товаре {id}")

# установка куки
def set(request):
    # получаем из строки запроса имя пользователя
    username = request.GET.get("username", "Undefined")
    # создаем объект ответа
    response = HttpResponse(f"Hello {username}")
    # передаем его в куки
    response.set_cookie("username", username)
    return response

# получение куки
def get(request):
    # получаем куки с ключом username
    username = request.COOKIES["username"]
    return HttpResponse(f"Hello {username}")
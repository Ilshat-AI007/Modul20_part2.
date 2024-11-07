from django.http import HttpResponse

def home(request):
    return HttpResponse('Добро пожаловать на главную страницу нашего города!')

def history(request):
    content = """
    История нашего города:
    - Основание города.
    - Важные исторические события.
    """
    return HttpResponse(content)

def famous_people(request):
    people_content = """
    Известные люди нашего города:
    - Иван Иванович.
    - Анна Петровна.
    - Сергей Васильевич.
    """
    return HttpResponse(people_content)

def historical_photos(request):
    photos_content = """
    Исторические фото нашего города:
    - Вид на старую площадь.
    - Старый мост через реку.
    """
    return HttpResponse(photos_content)

def city_news(request):
    news_content = """
    Актуальные новости нашего города:
    - Открытие дворца Борьбы в Уфе.
    - Проведение субботника.
    """
    return HttpResponse(news_content)

def city_management(request):
    management_content = """
        Руководство нашего города:
        - Мэр: Елена Робертовна.
        - Заместитель мэра: Людмилла.
        - Глава администрации: Евгений Алексеевич.
        """
    return HttpResponse(management_content)

def multy_table(request, wrong):
    table = [[i * j for j in range(1, 11)] for i in range(1, 11)]
    result = f'Таблица умножения {table}.'
    return HttpResponse(result)

def city_facts(request):
    facts_content = """
        Интересные факты о нашем городе:
        - Основан башкирами по доброй воле.
        - Известен своими медом, гостеприимством и кумысом.
        """
    return HttpResponse(facts_content)

def contact_phone_services(request):
    contacts_content = """
        Контактные телефоны городских служб:
        - Пожарная служба: 01.
        - Полиция: 02.
        - Скорая помощь: 03.
        - Справочная служба: +7 (123) 456-78-90.
        """
    return HttpResponse(contacts_content)
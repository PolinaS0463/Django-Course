from django.shortcuts import render, HttpResponse
import logging

logger = logging.getLogger('main')

def index(request):
    logger.info('User visited \'index\' page')
    h2 = 'Добро пожаловать на мой сайт!'
    h3 = 'Сдаю первое ДЗ'
    b = 'какой-то текст'
    i = 'еще текст'
    context = {'h2' : h2, 
               'h3' : h3, 
               'b' : b,
               'i' : i}
    return render(request, 'myapp/index.html', context=context)


def about(request):
    logger.info('User visited \'about\' page')
    return HttpResponse('''<h2>Всем привет! Это страница "Обо мне"!</h2>
                           <h3>Я Python разработчик</h3>
                            <b>здесь должен быть текст</b><br>
                           <i>еще текст</i>
                        ''')

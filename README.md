# Программа исправления оценок

Программа исправляет оценки 2 и 3 на 5, удаляет все замечания и добавляет 
случайную похвалу на указанный предмет.

## Как установить

Python3 должен быть уже установлен. 

Файл `script.py` необходимо положить на сервер электронного дневника в папку 
рядом с файлом `manage.py`.

## Запуск

1. Запустить Django shell командой:
    ~~~ 
    python manage.py shell
    ~~~
2. Подключить скрипт командой:
    ~~~
    import script
    ~~~
3. Запустить скрипт командой:
    ~~~
    script.main()
    ~~~
4. Ввести ФИО ученика которому необходимо исправить оценки и нажать `Enter`, например:
   ~~~
   Фролов Иван Григорьевич
   ~~~
5. Ввести название предмета по которому необходимо добавить похвалу, например:
    ~~~
    Русский язык
    ~~~

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на 
сайте [Devman](https://dvmn.org).

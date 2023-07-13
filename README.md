# About

htmlbuilder-python-bridge is serverside and client tools for uploading static sites. 
It is addon for https://github.com/ArtNazarov/htmlbuilder

![Flask app with WSGI](http://apprr.rf.gd/flask.png)

# О расширении

htmlbuilder-python-bridge это утилита из 2 частей для сервера и клиента для загрузки статических сайтов. 
Это дополнение предназначено для https://github.com/ArtNazarov/htmlbuilder


# Using of bridge from serverside

1. Set API key in server.py
2. Upload to serverside file server.py
3. You can test receiving and unpacking with zip archive files.zip and script send-files.py
If all right, for domain example.com, will be create page http://example.com/test_dir/test2.html


# Использование моста со стороны сервера

1. Назначьте ключ API в файле server.py
2. Выгрузите на сервер файл server.py
3. Вы можете протестировать загрузку и распаковку архива files.zip, используя send-files.py
Если все в порядке, для домена example.com будет создана страница http://example.com/test_dir/test2.html


# Publication of zip archive from client

1. Change domain in send-files.py to own
2. Send API key corresponding to API key from the server.py
2. Call python3 script send-files.py in terminal

```
python3 send-files.py
```

# Публикация zip архива от клиента

1. Установите свой домен в send-files.py
2. Установите ключ API в соответствии со значением API из server.py
2. Запустите скрипт send-files.py в терминале

```
python3 send-files.py
```

During this action:

1. File files.zip will be uploaded to server
2. server.py unpack to document root content of zip archive
3. server.py remove from server archive files.zip

Во время этого действия:

1. Файл files.zip выгружается на сервер
2. Мост server.py распакует содержимое архива в корневую папку
3. Мост server.py удалит с сервера файл files.zip

Before launch / Перед запуском

Install libraries with pip using requirements.txt.
Установите библиотеки с помощью pip согласно requirements.txt.
```
pip install requirments.txt
```

Launch server / Запуск сервера
```
mod_wsgi-express start-server wsgi.py --processes 4 --port 8080
```

or

```
mod_wsgi-express start-server wsgi.py --processes 4 --port 8080 --user www-data --group www-data
```

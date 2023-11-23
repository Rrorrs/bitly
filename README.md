# Обрезка ссылок с помощью Битли

Данный код позволяет быстро сократить длинные ссылки в формат Битли и подсчитать сколько раз по ним перешли используя консоль. Тоесть, запуская данную программу, мы вводим в консоль ссылку, которую требуется сократить и получаем на выходе её, но преобразованную в Битли формате. Если же снова запустив программу мы введём уже краткий вариант исходной ссылки, то на выходе получим количество кликов по ней, то есть то, сколько раз люди переходили по ней.

### Как установить

Ключ для работы с bit.ly находится в файле `.env` как переменная окружения. Сама переменная называется "BITLY_TOKEN", ключ находящийся внутри можно взять с сайта [bit.ly](https://app.bitly.com/Bn2reWEAZob/dashboard/), в личном кабинете. Данный ключ нужен для того, чтобы программа могла использовать функцианал сайта и сокращать ссылки самостоятельно.

Python3 должен быть уже установлен. 
Затем используйте `pip`(или `pip3`, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).

# Django-shop

## Описание проекта

**Django-shop** — это веб-приложение, разработанное с использованием Django. Оно представляет собой интернет-магазин с возможностью просмотра продуктов, услуг, информации о компании и контактных данных. Приложение поддерживает поиск по продуктам и услугам, а также адаптивный дизайн для удобного использования на различных устройствах.

---

## Структура проекта

- **`req.txt`** — файл с зависимостями проекта. Используется для установки всех необходимых библиотек.
- **`shop/`** — корневая папка проекта Django.
  - **`shop/settings.py`** — настройки проекта.
  - **`shop/urls.py`** — маршруты проекта.
  - **`shop/wsgi.py`** — точка входа для WSGI-сервера.
- **`shop/main/`** — основное приложение проекта.
  - **`models.py`** — модели базы данных (продукты, услуги, контакты, информация о компании).
  - **`views.py`** — представления для обработки запросов.
  - **`urls.py`** — маршруты для приложения.
  - **`templates/`** — HTML-шаблоны для отображения страниц.
  - **`static/`** — статические файлы (CSS, изображения, JavaScript).
  - **`templatetags/`** — кастомные фильтры и теги для шаблонов.

---

## Установка и запуск проекта

### 1. Клонирование репозитория

Склонируйте репозиторий на локальную машину:

```bash
git clone https://github.com/rollouts21/django-shop
cd django-shop
```

### 2. Установка зависимостей
Убедитесь, что у вас установлен Python 3. Затем установите зависимости:
```bash
pip install -r req.txt
```

### 3. Настройка базы данных
Примените миграции для настройки базы данных:
```bash
python manage.py migrate
```
### 4. Запуск сервера разработки
Запустите сервер разработки:
```bash 
python manage.py runserver
```
Приложение будет доступно по адресу: http://127.0.0.1:8000.



## Основные функции
### 1. Продукты
Просмотр списка продуктов.
Детальная страница продукта с описанием, ценой и количеством.
Поиск по продуктам.
### 2. Услуги
Просмотр списка услуг.
Детальная страница услуги с описанием и ценой.
Поиск по услугам.
### 3. О нас
Просмотр информации о компании.
### 4. Контакты
Просмотр контактной информации (телефоны, email).


## Адаптивный дизайн
Проект поддерживает адаптивный дизайн, что делает его удобным для использования как на настольных компьютерах, так и на мобильных устройствах.

##Статические файлы
Для работы со статическими файлами выполните команду:
```bash
python manage.py collectstatic
```
Убедитесь, что в настройках указаны правильные пути:
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

## Дополнительные команды
Создание суперпользователя
Для доступа в админ-панель создайте суперпользователя:
```bash
python manage.py createsuperuser
```
Админ-панель будет доступна по адресу: http://127.0.0.1:8000/admin.

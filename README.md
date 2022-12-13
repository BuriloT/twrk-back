# twrk-back

## Test-task

> В проекте создана модель Продукт с полями: Название, Артикул, Статус, Цена, Изображение. Поле изображение принимает формат .jpg и .png и конвертирует его в .webp.

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/BuriloT/twrk-back.git
```

```
cd twrk-back
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```
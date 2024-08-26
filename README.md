# Osh Cargo


## __Установка на локальном компьютере__
1. Клонируйте репозиторий:
    ```
    git clone https://github.com/mhdnv1/cargo.git
    ```
2. Установите и активируйте виртуальное окружение:
    ```
    python -m venv venv
    source venv/Scripts/activate  - для Windows
    source venv/bin/activate - для Linux
    ```
3. Установите зависимости:
    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. Создайте файл .env в коневом коталоге где manage.py
5. Перейдите в папку product и выполните миграции:
    ```
    cd product
    python manage.py migrate
    ```
6. Создайте суперпользователя:
    ```
    python manage.py createsuperuser
    ```
7. Запустите проект:
    ```
    python manage.py runserver
    ```

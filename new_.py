# Не понял, в чем смысл задачи ниже. Создал по описанию.

def test_function():  # 1. Создайте новую функцию def test_function
    inner_function()  # 3. Вызовите функцию inner_function внутри функции test_function


def inner_function():
    def another_function():  # 2. Создайте другую функцию внутри функции inner_function
        print("Я в области видимости функции test_function")  # 2. функция должна печатать значение


inner_function()  # 4. Попробуйте вызывать inner_function вне функции test_function и посмотрите на результат выполнения программы





# Или должно быть так?

# def test_function():
#     inner_function()
# def inner_function():
#     print("Я в области видимости функции test_function")
# inner_function()


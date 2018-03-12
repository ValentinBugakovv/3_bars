# Ближайшие бары

Программа расчитывает самый большой, маленький, близкий бар в г.Москва. Список московских баров в формате JSON можно взять [здесь](https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json) или с сайта [data.mos.ru](https://data.mos.ru/). 

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
После названия исполняемого файла (bars.py) требуется указать путь к файлу со списком баров (bars.json)
```python
# для работы программы необходимо импортироватm следующие модули:

import json
import argparse
import os
from math import sqrt

# Функция def get_arguments принимает на вход путь до файла из командной строки
def get_arguments():
return args

# Функция def decorate является декоратором для красивого вывода json объектов

def decorate(func):
    def wrap(*args):
        return json.dumps(func(args[0]))
    return wrap
    
# Функция def load_data принимет на вход путь до файла и декодирует json в строку

def load_data(filepath):
return json.load(jsonfile)

# Функция def get_biggest_bar(bar_data) принмает список баров 
# и выводит информацию о самом большом баре в формате json
def get_biggest_bar(bar_data):
return attributes

# Функця  def get_smallest_bar(bar_data) аналогична, но выводит информацию о самом маленьком баре

# Функция def get_closest_bar(bar_data, longitude, latitude) примает на вход список баров, 
# координаты( долгота и широта), 
# возвращает самый близкий бар относительно введенных координатов в формате json
def get_closest_bar(bar_data, longitude=37.55, latitude=55.75):
  return attributes
```

Запуск на Linux:

```bash

$ python bars.py filepath.json # possibly requires call of python3 executive instead of just python

# Пример вывода

САМЫЙ БОЛЬШЙ БАР:
Спорт бар <<Красная машина>>

САМЫЙ МАЛЕНЬКИЙ БАР:
Бар Соки

САМЫЙ МАЛЕНЬКИЙ БАР:
Бар <<Разлив>>

```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)

# Ближайшие бары

Программа расчитывает самый большой, маленький, близкий бар в г.Москва. Список московских баров в формате JSON можно взять [здесь](https://devman.org/media/filer_public/95/74/957441dc-78df-4c99-83b2-e93dfd13c2fa/bars.json) или с сайта [data.mos.ru](https://data.mos.ru/). 

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5
```python
# для работы программы необходимо импортироватm следующие модули:

import json
import argparse
import os
from math import sqrt

```

Запуск на Linux:

```bash

$ python bars.py  # possibly requires call of python3 executive instead of just python

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

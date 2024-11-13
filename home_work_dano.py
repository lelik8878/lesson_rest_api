
message_from_artiom = '''  {
  "title": "физик",
  "service_set": [
    {
      "title": "petux",
      "image": "/media/service/logo.png",
      "description": "fdsagdfsgdsf",
      "best": true
    },
    {
      "title": "petux2",
      "image": "/media/service/logo.png",
      "description": "fdsagdfsgdsf",
      "best": true
    }
  ]
}'''

# Есть две модели: главная с полем 'title' и зависимая, с полями "title" "image" "description" "best"  и связью
# ForeighnKey с первой моделью. От Артёма приходят данные в виде message_from_artiom. Нужно проверить, есть ли запись
# с полем 'title' в главной таблице: если нет, то создать, и создать записи во вторичной модели и связать с первичной.
#  Если есть, новую не создавать, проверить, существуют ли в базе данных экземпляры вторичной модели, связанные с
# данной первичной моделью, если их нет, то создать.

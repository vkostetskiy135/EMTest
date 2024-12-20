# Library Management System

## Описание

Это консольное приложение для управления библиотекой книг. Оно позволяет добавлять, удалять, искать и отображать книги. Данные о книгах сохраняются в JSON-файле.

---

## Функционал

Приложение поддерживает следующие операции:

1. **Добавление книги**  
   Пользователь вводит название, автора и год издания книги. Книга добавляется в библиотеку с уникальным `id` и статусом `в наличии`.

2. **Удаление книги**  
   Пользователь вводит `id` книги, которую нужно удалить.

3. **Поиск книги**  
   Поиск возможен по названию (`title`), автору (`author`) или году издания (`year`).

4. **Отображение всех книг**  
   Вывод всех книг в библиотеке с их `id`, названием, автором, годом издания и статусом.

5. **Изменение статуса книги**  
   Пользователь может изменить статус книги на `в наличии` или `выдана`, указав `id` книги.




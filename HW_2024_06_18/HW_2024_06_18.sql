-- 1. Создайте таблицу "Students" с полями "ID", "name", "age", "major", "GPA". DONE
CREATE TABLE Students (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    major TEXT NOT NULL,
    GPA REAL NOT NULL
);

-- 2. Вставьте строки с данными о студентах в таблицу "Students".
INSERT INTO Students (name, age, major, GPA) VALUES ('Alice', 22, 'Computer Science', 4.8);
INSERT INTO Students (name, age, major, GPA) VALUES ('Bob', 19, 'Mathematics', 3.6);
INSERT INTO Students (name, age, major, GPA) VALUES ('Charlie', 20, 'Physics', 3.5);
INSERT INTO Students (name, age, major, GPA) VALUES ('David', 23, 'Biology', 3.7);
INSERT INTO Students (name, age, major, GPA) VALUES ('Eve', 21, 'Chemistry', 3.4);
INSERT INTO Students (name, age, major, GPA) VALUES ('Frank', 22, 'Engineering', 4.9);
INSERT INTO Students (name, age, major, GPA) VALUES ('Grace', 19, 'Economics', 3.3);
INSERT INTO Students (name, age, major, GPA) VALUES ('Heidi', 20, 'Computer Science', 3.6);
INSERT INTO Students (name, age, major, GPA) VALUES ('Ivan', 23, 'Mathematics', 3.8);
INSERT INTO Students (name, age, major, GPA) VALUES ('Judy', 21, 'Physics', 3.4);
INSERT INTO Students (name, age, major, GPA) VALUES ('Karl', 22, 'Biology', 3.9);
INSERT INTO Students (name, age, major, GPA) VALUES ('Linda', 19, 'Chemistry', 3.3);
INSERT INTO Students (name, age, major, GPA) VALUES ('Mike', 20, 'Engineering', 2.7);
INSERT INTO Students (name, age, major, GPA) VALUES ('Nancy', 23, 'Economics', 3.5);
INSERT INTO Students (name, age, major, GPA) VALUES ('Oliver', 21, 'Computer Science', 3.9);
INSERT INTO Students (name, age, major, GPA) VALUES ('Patricia', 22, 'Mathematics', 3.3);
INSERT INTO Students (name, age, major, GPA) VALUES ('Quentin', 19, 'Physics', 3.8);
INSERT INTO Students (name, age, major, GPA) VALUES ('Rebecca', 20, 'Biology', 2.4);
INSERT INTO Students (name, age, major, GPA) VALUES ('Steve', 23, 'Chemistry', 3.6);
INSERT INTO Students (name, age, major, GPA) VALUES ('Tina', 21, 'Engineering', 3.9);
INSERT INTO Students (name, age, major, GPA) VALUES ('Ursula', 22, 'Economics', 3.3);
INSERT INTO Students (name, age, major, GPA) VALUES ('Victor', 19, 'Computer Science', 3.7);
INSERT INTO Students (name, age, major, GPA) VALUES ('Wendy', 20, 'Mathematics', 3.5);
INSERT INTO Students (name, age, major, GPA) VALUES ('Xavier', 23, 'Physics', 3.9);
INSERT INTO Students (name, age, major, GPA) VALUES ('Yvonne', 21, 'Biology', 3.3);
INSERT INTO Students (name, age, major, GPA) VALUES ('Zachary', 22, 'Chemistry', 3.8);
INSERT INTO Students (name, age, major, GPA) VALUES ('Amelia', 19, 'Engineering', 4.4);
INSERT INTO Students (name, age, major, GPA) VALUES ('Benjamin', 20, 'Economics', 3.6);
INSERT INTO Students (name, age, major, GPA) VALUES ('Clara', 23, 'Computer Science', 3.9);
INSERT INTO Students (name, age, major, GPA) VALUES ('Daniel', 21, 'Mathematics', 3.3);
INSERT INTO Students (name, age, major, GPA) VALUES ('Emily', 22, 'Physics', 3.8);
INSERT INTO Students (name, age, major, GPA) VALUES ('Frederick', 19, 'Biology', 3.4);
INSERT INTO Students (name, age, major, GPA) VALUES ('Gabrielle', 20, 'Chemistry', 4.6);
INSERT INTO Students (name, age, major, GPA) VALUES ('Hannah', 23, 'Engineering', 4.9);
INSERT INTO Students (name, age, major, GPA) VALUES ('Isaac', 21, 'Economics', 3.3);
INSERT INTO Students (name, age, major, GPA) VALUES ('Jacqueline', 22, 'Computer Science', 3.8);
INSERT INTO Students (name, age, major, GPA) VALUES ('Kevin', 19, 'Mathematics', 3.6);
INSERT INTO Students (name, age, major, GPA) VALUES ('Laura', 20, 'Physics', 3.3);
INSERT INTO Students (name, age, major, GPA) VALUES ('Matthew', 23, 'Biology', 3.9);
INSERT INTO Students (name, age, major, GPA) VALUES ('Nicole', 21, 'Chemistry', 3.4);
INSERT INTO Students (name, age, major, GPA) VALUES ('Oscar', 22, 'Engineering', 3.6);
INSERT INTO Students (name, age, major, GPA) VALUES ('Pamela', 19, 'Economics', 3.9);
INSERT INTO Students (name, age, major, GPA) VALUES ('Quincy', 20, 'Computer Science', 2.3);
INSERT INTO Students (name, age, major, GPA) VALUES ('Rachel', 23, 'Mathematics', 3.8);
INSERT INTO Students (name, age, major, GPA) VALUES ('Samuel', 21, 'Physics', 3.4);
INSERT INTO Students (name, age, major, GPA) VALUES ('Theresa', 22, 'Biology', 2.6);
INSERT INTO Students (name, age, major, GPA) VALUES ('Ulysses', 19, 'Chemistry', 3.9);
INSERT INTO Students (name, age, major, GPA) VALUES ('Virginia', 20, 'Engineering', 3.3);
INSERT INTO Students (name, age, major, GPA) VALUES ('Walter', 23, 'Economics', 3.8);
INSERT INTO Students (name, age, major, GPA) VALUES ('Xenia', 21, 'Computer Science', 2.4);
INSERT INTO Students (name, age, major, GPA) VALUES ('York', 22, 'Mathematics', 3.6);
INSERT INTO Students (name, age, major, GPA) VALUES ('Zoe', 19, 'Physics', 2.9);

-- 3. Выведите все данные из таблицы "Students".

-- 4. Выведите только имена и средние баллы студентов из таблицы "Students".

-- 5. Выведите всех студентов, которые изучают "Computer Science".

-- 6. Выведите всех студентов, средний балл которых превышает 3.5.

-- 7. Обновите средний балл студента с ID 1 на 3.6.

-- 8. Обновите специальность всех студентов, средний балл которых ниже или равен 3.4, на "Undecided".

-- 9. Удалите студента с ID 5 из таблицы "Students".

-- 10. Удалите всех студентов, которые изучают "Economics".

-- 11. Выведите количество студентов в таблице "Students".

-- 12. Выведите средний возраст студентов в таблице "Students".

-- 13. Выведите имена и средние баллы всех студентов, отсортированных по среднему баллу в порядке убывания.

-- 14. Выведите всех студентов, средний балл которых выше среднего по таблице.

-- 15. Выведите имена и средние баллы всех студентов, специальность которых начинается на "C", отсортированных по имени в порядке возрастания.

-- 16. Обновите специальность всех студентов на "Advanced", средний балл которых выше или равен 3.8.

-- 17. Обновите специальность студента с ID 1 на "Mathematics".

-- 18. Обновите имена всех студентов, средний балл которых выше 3.5, добавив к их имени префикс "Top student".

-- 19. Удалите всех студентов, возраст которых ниже 18 лет.

-- 20. Удалите всех студентов, средний балл которых ниже 2.0.

-- 21. Измените таблицу "Students", добавив поле "Email" типа TEXT.

-- 22. Измените таблицу "Students", переименовав поле "major" в "Specialization".

-- 23. Измените таблицу "Students", удалив поле "Email".

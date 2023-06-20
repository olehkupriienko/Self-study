/*   #1.2.1   */
SELECT *
FROM book;

/*   #1.2.2   */
SELECT author, title, price
FROM book;

/*   #1.2.3   */
SELECT title AS Название, author AS Автор
FROM book;

/*   #1.2.4   */
SELECT title,
       amount,
       amount * 1.65 AS pack
FROM book;

/*   #1.2.5
     Выборка данных, вычисляемые столбцы, математические функции    */
SELECT title,
       author,
       amount,
       ROUND(price * 0.7, 2) AS new_price
FROM book;

/*   #1.2.6
     Логические функции    */
SELECT author,
       title,
       IF(author = 'Булгаков М.А.', ROUND(price * 1.1, 2),
          (IF(author = 'Есенин С.А.', ROUND(price * 1.05, 2), price))) AS new_price
FROM book;

/*   #1.2.7
     Выборка данных по условию    */
SELECT author,
       title,
       price
FROM book
WHERE amount < 10;

/*   #1.2.7
     Выборка данных, логические операции    */
SELECT title,
       author,
       price,
       amount
FROM book
WHERE price * amount >= 5000
  and (price < 500 or price > 600);

/*   #1.2.8
     Выборка данных, операторы BETWEEN, IN    */
SELECT title,
       author
FROM book
WHERE price BETWEEN 540.50 AND 800
  AND amount IN (2, 3, 5, 7);

/*   #1.2.9
     Выборка данных с сортировкой    */
SELECT author,
       title
FROM book
WHERE amount BETWEEN 2 AND 14
ORDER BY author DESC, title;

/*   #1.2.9
     Выборка данных, оператор LIKE    */
SELECT title,
       author
FROM book
WHERE title LIKE '%_ %' AND author LIKE '%С.%'
ORDER BY title;

/*   #1.2.10
     Повторение материала    */
SELECT 'Дарья Донцова' AS author,
       CONCAT('Евлампия романова и ', title) as title,
       ROUND(price * 1.42, 2) as price
FROM book
ORDER BY price DESC, title DESC
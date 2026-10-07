
--DAY 1 PROBLEMS


CREATE TABLE Books(book_id INT PRIMARY KEY,book_name VARCHAR(50),author VARCHAR(50),price INT)

CREATE TABLE Members(member_id INT PRIMARY KEY,member_name VARCHAR(50),city VARCHAR(50),phone INT)

CREATE TABLE Borrow(borrower_id INT PRIMARY KEY, book_id INT,member_id INT,borrow_date DATE)

ALTER TABLE Books
ADD category VARCHAR(50)

ALTER TABLE Books 
ADD quantity INT

ALTER TABLE Members
ADD Email VARCHAR(50)

ALTER TABLE Borrow
ADD return_date DATE

ALTER TABLE Books
ALTER COLUMN price TYPE DECIMAL(10,2)

ALTER TABLE Books
RENAME quantity to stock_quantity

SELECT*FROM Books
SELECT*FROM Members
SELECT*FROM Borrow

INSERT INTO Books(book_id,book_name,author,price,category,stock_quantity)VALUES
(101,'Atomic Habits','Author 1',530,'Psychology',12),
(102,'The life of pi','Author 2',540,'Stories',14),
(103,'To kill a mocking bird','Author 3',,600'Philosophy',18),
(104,'The tale of unsinkable ship','Author 4',550,'History',20),
(105,'The marvel spiderman comics','Author 5',600,'Kids',22)
(106,'The power of subconsious mind','Author 6',700,'Psychology',12)
(107,'The 48 laws of power','Author 7',750,'Psychology',15)
(108,'The art of war','Author 8',800,'Psychology',20)
(109,'The drama','Author 9',900,'Literature',22)
(110,'The tales of mario','Author 10',850,'Kids',25)


INSERT INTO members (member_id, member_name, city, phone, email)
VALUES
(1, 'Member 1', 'Chennai', '1234567890', 'xyz@gmail.com'),
(2, 'Member 2', 'Bangalore', '2233445566', 'yyy@gmail.com'),
(3, 'Member 3', 'Mumbai', '2343567855', 'abc@gmail.com'),
(4, 'Member 4', 'Chennai', '3425678456', 'hello@gmail.com'),
(5, 'Member 5', 'Tirunelveli', '1324567845', 'hi@gmail.com'),
(6, 'Member 6', 'Bangalore', '5643755822', 'abd@gmail.com'),
(7, 'Member 7', 'Assam', '5644732856', 'assam@gmail.com'),
(8, 'Member 8', 'Gujarat', '4563758901', 'amail@gmail.com')


INSERT INTO borrow (borrower_id, book_id, member_id, borrow_date, return_date)
VALUES
(121,110,2,'2026-08-12','2026-09-15'),
(122,103,5,'2026-02-11','2026-02-20'),
(123,104,4,'2026-04-23','2026-05-20'),
(124,103,8,'2026-05-12','2026-06-15'),
(125,108,9,'2026-02-25','2026-03-21'),
(126,103,3,'2026-10-01','2026-10-10'),
(127,104,1,'2026-11-11','2026-11-20'),
(128,110,7,'2026-12-12','2026-12-24'),
(129,105,8,'2026-05-18','2026-06-18'),
(130,110,6,'2026-06-12','2026-07-15')

INSERT INTO Books(book_id,book_name,author,price,category,stock_quantity)VALUES
(111,'The pursuit of happyness','Author 11',570,'Lfestyle',15

INSERT INTO members (member_id, member_name, city, phone, email)
VALUES
(009,'Member 9','Kochi','4536784561','zyx@gmail.com')

INSERT INTO borrow (borrower_id, book_id, member_id, borrow_date, return_date)
VALUES
(131,102,004,'2026-02-02','2026-03-11')

DELETE FROM Books 
WHERE book_id=106

UPDATE books
SET price=600
WHERE book_id=103

UPDATE books
SET price = price * 1.10
WHERE category = 'Psychology'

UPDATE books
SET stock_quantity=stock_quantity + 5

UPDATE members
SET city='Madurai'
WHERE member_id=1

UPDATE members
SET email ='123@gmail.com'
WHERE member_id=4

UPDATE books
SET category='Life philosophy'
WHERE book_id=103

UPDATE Borrow
SET return_date='2026-02-28'
WHERE borrower_id=122

DELETE FROM Borrow 
WHERE borrower_id=131

DELETE FROM Books
WHERE stock_quantity=0

SELECT*FROM Books
SELECT book_name,author FROM Books

SELECT*FROM Books
WHERE price>500

SELECT*FROM Books
WHERE price<500

SELECT*FROM Books
WHERE price BETWEEN 300 AND 800

SELECT*FROM Books
WHERE category='Psychology'

SELECT*FROM Books
WHERE author='Author 1'

SELECT*FROM Books 
WHERE book LIKE S%

SELECT*FROM Books
WHERE book ILIKE %SQL%

SELECT*FROM Books 
WHERE category IN ('Psychology','History')

SELECT*FROM Books
WHERE price <>500

SELECT*FROM Books
WHERE stock_quantity>10

SELECT*FROM Books 
WHERE stock_quantity between 5 AND 15

SELECT*FROM Books
ORDER BY PRICE ASC

SELECT*FROM Books
ORDER BY PRICE DESC

SELECT*FROM Books
ORDER BY books ASC

SELECT*FROM Books
ORDER BY category ASC , price ASC

SELECT*FROM Books
ORDER BY PRICE DESC
LIMIT 3

SELECT*FROM Books
ORDER BY PRICE ASC
LIMIT 3

SELECT*FROM Books
ORDER BY stock_quantity DESC
LIMIT 5

SELECT*FROM Members
ORDER BY member_name ASC
LIMIT 5

SELECT*FROM Borrow
ORDER BY borrow_date DESC
LIMIT 5

SELECT COUNT(*) AS total_books
FROM books

SELECT COUNT(*) AS total_members
FROM Members

SELECT COUNT(*) AS total_borrow
FROM Borrow

SELECT SUM(stock_quantity) AS total_stock
FROM Books

SELECT SUM(price) AS total_price
FROM Books

SELECT MAX(price) AS highest_price
FROM Books

SELECT MIN(price) AS lowest_price
FROM Books

SELECT MAX(price) - MIN(price) AS price_difference
FROM Books

SELECT AVG(stock_quantity) AS avg_quantity
FROM Books

SELECT category, COUNT(*) AS total_books
FROM books
GROUP BY category

SELECT category, AVG(price) AS average_price
FROM books
GROUP BY category

SELECT category, MAX(price) AS highest_price
FROM books
GROUP BY category

SELECT category , MIN(price) AS lowest_price
FROM Books
GROUP BY category

SELECT category , SUM(stock_quantity) AS total_stock_quantity
FROM Books
GROUP BY category

SELECT category,
SUM(price * stock_quantity) AS total_value
FROM books
GROUP BY category

SELECT category, COUNT(*) AS total_books
FROM books
GROUP BY category
HAVING COUNT(*) > 2

SELECT category, AVG(price) AS average_price
FROM books
GROUP BY category
HAVING AVG(price) > 500

SELECT author, COUNT(*) AS total_books
FROM books
GROUP BY author

SELECT author, AVG(price) AS average_price
FROM books
GROUP BY author

SELECT category, COUNT(*) AS total_books
FROM books
GROUP BY category
HAVING COUNT(*) > 2

SELECT category, AVG(price) AS average_price
FROM books
GROUP BY category
HAVING AVG(price) > 500

SELECT author, COUNT(*) AS total_books
FROM books
GROUP BY author
HAVING COUNT(*) > 1

SELECT category, SUM(stock_quantity) AS total_stock
FROM books
GROUP BY category
HAVING SUM(stock_quantity) > 20

SELECT author, AVG(price) AS average_price
FROM books
GROUP BY author
HAVING AVG(price) > 600
/*DAY 2 PROBLEMS AND SUMS*/
--USING INNER JOINS

SELECT b.book_name, m.member_name
FROM borrow br
INNER JOIN books b
ON br.book_id = b.book_id
INNER JOIN members m
ON br.member_id = m.member_id;


SELECT b.book_name, m.member_name, br.borrow_date
FROM borrow br
INNER JOIN books b
ON br.book_id = b.book_id
INNER JOIN members m
ON br.member_id = m.member_id;

SELECT b.book_name,
       b.author,
       m.member_name,
       m.city
FROM borrow br
INNER JOIN books b
ON br.book_id = b.book_id
INNER JOIN members m
ON br.member_id = m.member_id;

SELECT b.book_name, m.member_name, m.city
FROM borrow br
INNER JOIN books b
ON br.book_id = b.book_id
INNER JOIN members m
ON br.member_id = m.member_id
WHERE m.city = 'Chennai';

SELECT b.book_name, m.member_name
FROM borrow br
INNER JOIN books b
ON br.book_id= b.book_id
INNER JOIN members m
ON br.member_id=m.member_id
WHERE m.member_id=2;

SELECT b.book_name, m.member_name
FROM borrow br
INNER JOIN books b
ON br.book_id=b.book_id
INNER JOIN members m
ON br.member_id=m.member_id
WHERE b.category='Technology'

SELECT b.book_name, m.member_name
FROM borrow br
INNER JOIN books b
ON br.book_id = b.book_id
INNER JOIN members m
ON br.member_id = m.member_id;

SELECT br.borrower_id,
       b.book_name,
       m.member_name,
       br.borrow_date,
       br.return_date
FROM borrow br
INNER JOIN books b
ON br.book_id = b.book_id
INNER JOIN members m
ON br.member_id = m.member_id
ORDER BY br.borrow_date ASC;

--USING LEFT JOIN

SELECT b.book_name,
       m.member_name
FROM books b
LEFT JOIN borrow br
ON b.book_id = br.book_id
LEFT JOIN members m
ON br.member_id = m.member_id;


SELECT b.book_name,
       br.borrower_id,
       br.borrow_date
FROM books b
LEFT JOIN borrow br
ON b.book_id = br.book_id;



SELECT m.member_name,
       b.book_name
FROM members m
LEFT JOIN borrow br
ON m.member_id = br.member_id
LEFT JOIN books b
ON br.book_id = b.book_id;



SELECT m.member_id,
       m.member_name,
       m.city,
       b.book_name
FROM members m
LEFT JOIN borrow br
ON m.member_id = br.member_id
LEFT JOIN books b
ON br.book_id = b.book_id;


SELECT b.book_id, b.book_name
FROM books b
LEFT JOIN borrow br
ON b.book_id = br.book_id
WHERE br.book_id IS NULL;


SELECT m.member_id, m.member_name
FROM members m
LEFT JOIN borrow br
ON m.member_id = br.member_id
WHERE br.member_id IS NULL;

--USING RIGHT JOIN

SELECT br.borrower_id,
       br.book_id,
       b.book_name,
       br.member_id,
       br.borrow_date,
       br.return_date
FROM books b
RIGHT JOIN borrow br
ON b.book_id = br.book_id;


SELECT br.borrower_id,
       br.book_id,
       m.member_name,
       br.borrow_date,
       br.return_date
FROM members m
RIGHT JOIN borrow br
ON m.member_id = br.member_id;


SELECT m.member_id,
       m.member_name,
       m.city,
       br.borrower_id,
       br.book_id,
       br.borrow_date,
       br.return_date
FROM borrow br
RIGHT JOIN members m
ON br.member_id = m.member_id;

--USING CROSS JOIN

SELECT b.book_name,
       m.member_name
FROM books b
CROSS JOIN members m;


SELECT COUNT(*) AS total_combinations
FROM books
CROSS JOIN members;


SELECT m.member_name,
       b.book_name,
       b.category
FROM members m
CROSS JOIN books b
WHERE b.category = 'Technology';

--USING JOIN+GROUP BY

SELECT m.member_id,
       m.member_name,
       COUNT(br.book_id) AS total_books
FROM members m
INNER JOIN borrow br
ON m.member_id = br.member_id
GROUP BY m.member_id, m.member_name;


SELECT b.book_id,
       b.book_name,
       COUNT(br.member_id) AS total_members
FROM books b
INNER JOIN borrow br
ON b.book_id = br.book_id
GROUP BY b.book_id, b.book;


SELECT b.book_id,
       b.book_name,
       COUNT(br.borrower_id) AS borrow_count
FROM books b
INNER JOIN borrow br
ON b.book_id = br.book_id
GROUP BY b.book_id, b.book_name
ORDER BY borrow_count DESC
LIMIT 1;


SELECT m.member_id,
       m.member_name,
       COUNT(br.book_id) AS total_books
FROM members m
INNER JOIN borrow br
ON m.member_id = br.member_id
GROUP BY m.member_id, m.member_name
HAVING COUNT(br.book_id) > 2;


SELECT b.category,
       COUNT(br.borrow_id) AS total_borrowed
FROM books b
INNER JOIN borrow br
ON b.book_id = br.book_id
GROUP BY b.category;


SELECT b.category,
       COUNT(br.borrower_id) AS total_borrowed
FROM books b
INNER JOIN borrow br
ON b.book_id = br.book_id
GROUP BY b.category;

--USING SUBQUERIES
--SINGLE ROW SUBQUERIES

SELECT *
FROM books
WHERE price > (
SELECT AVG(price)
FROM books
);


SELECT *
FROM books
WHERE price < (
SELECT AVG(price)
FROM books
);


SELECT*
FROM books
WHERE price = (
SELECT MAX(price)
FROM books
);


SELECT*
FROM books
WHERE price =(
SELECT MIN(price)
FROM books
);


SELECT *
FROM books
WHERE price = (
SELECT price
FROM books
WHERE book_id = 2
);


SELECT*
FROM books
WHERE stock_quantity >(
SELECT AVG(stock_quantity)
FROM books
);


--SUBQUERY WITH IN 

SELECT *
FROM books
WHERE category IN (
SELECT category
FROM books
GROUP BY category
HAVING COUNT(*) > 1
);


SELECT*
FROM books
WHERE author IN (
SELECT author 
FROM books
GROUP BY author
HAVING COUNT(*) > 1
);


SELECT *
FROM books
WHERE category IN (
SELECT category
FROM books
GROUP BY category
HAVING AVG(price) > 500
);


SELECT *
FROM members
WHERE member_id IN (
SELECT member_id
FROM borrow
WHERE book_id IN (
SELECT book_id
FROM books
WHERE category = 'Technology'
    )
);


--SUBQUERY WITH NOT IN

SELECT *
FROM books
WHERE book_id NOT IN (
SELECT book_id
FROM borrow
);


SELECT *
FROM members
WHERE member_id NOT IN (
SELECT member_id
FROM borrow
);


SELECT DISTINCT author
FROM books
WHERE book_id NOT IN (
SELECT book_id
FROM borrow
);


--USING EXISTS keyword

SELECT *
FROM books b
WHERE EXISTS (
SELECT 1
FROM borrow br
WHERE br.book_id = b.book_id
);


SELECT *
FROM members m
WHERE EXISTS (
SELECT 1
FROM borrow br
WHERE br.member_id = m.member_id
);


SELECT *
FROM books b
WHERE EXISTS (
SELECT 1
FROM borrow br
WHERE br.book_id = b.book_id
GROUP BY br.book_id
HAVING COUNT(*) >= 2
);


--CTE

WITH avg_price AS (
SELECT AVG(price) AS average_price
FROM books
)
SELECT *
FROM books
WHERE price > (
SELECT average_price
FROM avg_price
);


WITH category_avg AS (
    SELECT category,
           AVG(price) AS average_price
    FROM books
    GROUP BY category
)
SELECT *
FROM category_avg;


WITH category_avg AS (
    SELECT category,
           AVG(price) AS average_price
    FROM books
    GROUP BY category
)
SELECT b.*
FROM books b
INNER JOIN category_avg ca
    ON b.category = ca.category
WHERE b.price > ca.average_price;


WITH category_stock AS (
    SELECT category,
           SUM(stock_quantity) AS total_stock
    FROM books
    GROUP BY category
)
SELECT *
FROM category_stock;


WITH category_stock AS (
    SELECT category,
           SUM(stock_quantity) AS total_stock
    FROM books
    GROUP BY category
)
SELECT *
FROM category_stock
WHERE total_stock > 20;


WITH category_max AS (
    SELECT category,
           MAX(price) AS highest_price
    FROM books
    GROUP BY category
)
SELECT b.*
FROM books b
INNER JOIN category_max cm
    ON b.category = cm.category
   AND b.price = cm.highest_price;


WITH author_books AS (
    SELECT author,
           COUNT(*) AS total_books
    FROM books
    GROUP BY author
)
SELECT *
FROM author_books;   


WITH author_books AS (
    SELECT author,
           COUNT(*) AS total_books
    FROM books
    GROUP BY author
)
SELECT *
FROM author_books
WHERE total_books > 1;


--WINDOW FUNCTIONS

SELECT book_id,
       book,
       price,
       RANK() OVER (ORDER BY price DESC) AS price_rank
FROM books;


SELECT book_id,
       book,
       price,
       RANK() OVER (ORDER BY price ASC) AS price_rank
FROM books;


SELECT book_id,
       book,
       price,
       ROW_NUMBER() OVER (ORDER BY price DESC) AS row_number
FROM books;


SELECT book_id,
       book,
       category,
       price,
       RANK() OVER (
           PARTITION BY category
           ORDER BY price DESC
       ) AS price_rank
FROM books;


SELECT book_id,
       book,
       category,
       price,
       DENSE_RANK() OVER (
           PARTITION BY category
           ORDER BY price DESC
       ) AS price_rank
FROM books;


SELECT book_id,
       book,
       category,
       price,
       AVG(price) OVER (
           PARTITION BY category
       ) AS category_avg_price
FROM books;


SELECT book_id,
       book,
       category,
       price,
       MAX(price) OVER (
           PARTITION BY category
       ) AS highest_category_price
FROM books;


SELECT book_id,
       book,
       category,
       price,
       MIN(price) OVER (
           PARTITION BY category
       ) AS lowest_category_price
FROM books;


SELECT book_id,
       book,
       category,
       price,
       price - AVG(price) OVER (
           PARTITION BY category
       ) AS price_difference
FROM books;


SELECT book_id,
       book,
       stock_quantity,
       SUM(stock_quantity) OVER (
           ORDER BY book_id
       ) AS cumulative_stock
FROM books;


SELECT book_id,
       book,
       category,
       stock_quantity,
       SUM(stock_quantity) OVER (
           PARTITION BY category
           ORDER BY book_id
       ) AS cumulative_stock
FROM books;


SELECT book_id,
       book,
       price,
       LAG(price) OVER (
           ORDER BY book_id
       ) AS previous_price
FROM books;


SELECT book_id,
       book,
       price,
       LEAD(price) OVER (
           ORDER BY book_id
       ) AS next_price
FROM books;


SELECT book_id,
       book,
       price,
       price - LAG(price) OVER (
           ORDER BY book_id
       ) AS price_difference
FROM books;


--CASE FUNCTIONS 

SELECT book_id,
       book,
       price,
       CASE
           WHEN price > 600 THEN 'Expensive'
           ELSE 'Affordable'
       END AS price_category
FROM books;


SELECT book_id,
       book,
       price,
       CASE
           WHEN price < 400 THEN 'Low'
           WHEN price BETWEEN 400 AND 700 THEN 'Medium'
           WHEN price > 700 THEN 'High'
       END AS price_category
FROM books;


SELECT book_id,
       book,
       stock_quantity,
       CASE
           WHEN stock_quantity = 0 THEN 'Out of Stock'
           WHEN stock_quantity BETWEEN 1 AND 5 THEN 'Low Stock'
           WHEN stock_quantity > 5 THEN 'Available'
       END AS stock_status
FROM books;


SELECT book,
       price,
       CASE
           WHEN price < 400 THEN 'Low'
           WHEN price BETWEEN 400 AND 700 THEN 'Medium'
           WHEN price > 700 THEN 'High'
       END AS price_category
FROM books;


SELECT book,
       stock_quantity,
       CASE
           WHEN stock_quantity = 0 THEN 'Out of Stock'
           WHEN stock_quantity BETWEEN 1 AND 5 THEN 'Low Stock'
           WHEN stock_quantity > 5 THEN 'Available'
       END AS stock_status
FROM books;


SELECT
    CASE
        WHEN price < 400 THEN 'Low'
        WHEN price BETWEEN 400 AND 700 THEN 'Medium'
        WHEN price > 700 THEN 'High'
    END AS price_category,
    COUNT(*) AS total_books
FROM books
GROUP BY
    CASE
        WHEN price < 400 THEN 'Low'
        WHEN price BETWEEN 400 AND 700 THEN 'Medium'
        WHEN price > 700 THEN 'High'
    END;


SELECT book,
       price,
       CASE
           WHEN price > 700 THEN price - 100
           ELSE price
       END AS discounted_price
FROM books;


--VIEWS FUNCTION

CREATE VIEW Technology_Books AS
SELECT *
FROM books
WHERE category = 'Technology';


SELECT *
FROM Technology_Books;


CREATE VIEW Expensive_Books AS
SELECT *
FROM books
WHERE price > 600;


CREATE VIEW Available_Books AS
SELECT *
FROM books
WHERE stock_quantity > 0;


CREATE VIEW Library_Borrow_Details AS
SELECT b.book_name,
       b.author,
       m.member_name,
       m.city,
       br.borrow_date
FROM borrow br
INNER JOIN books b
    ON br.book_id = b.book_id
INNER JOIN members m
    ON br.member_id = m.member_id;


SELECT *
FROM Library_Borrow_Details;


CREATE VIEW Category_Average_Price AS
SELECT category,
       AVG(price) AS average_price
FROM books
GROUP BY category;


CREATE VIEW Borrowing_Members AS
SELECT DISTINCT m.member_id,
       m.member_name,
       m.city
FROM members m
INNER JOIN borrow br
    ON m.member_id = br.member_id;


SELECT column_name,
       data_type
FROM information_schema.columns
WHERE table_name = 'technology_books';


CREATE OR REPLACE VIEW Technology_Books AS
SELECT book_id,
       book,
       author,
       category,
       price,
       stock_quantity,
       price * stock_quantity AS inventory_value
FROM books
WHERE category = 'Technology';


DROP VIEW Technology_Books;


--STORED PROCEDURES


CREATE OR REPLACE PROCEDURE GetAllBooks()
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT * FROM books;
END;
$$;


CREATE OR REPLACE PROCEDURE GetAllMembers()
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT * FROM members;
END;
$$;


CREATE OR REPLACE PROCEDURE GetBooksByCategory(
    IN p_category VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT *
    FROM books
    WHERE category = p_category;
END;
$$;


CREATE OR REPLACE PROCEDURE GetBooksByAuthor(
    IN p_author VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT *
    FROM books
    WHERE author = p_author;
END;
$$;


CREATE OR REPLACE PROCEDURE GetBooksAbovePrice(
    IN p_price NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT *
    FROM books
    WHERE price > p_price;
END;
$$;


CREATE OR REPLACE PROCEDURE GetMemberBorrowDetails(
    IN p_member_id INTEGER
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT m.member_name,
           b.book,
           br.borrow_date,
           br.return_date
    FROM borrow br
    INNER JOIN members m
        ON br.member_id = m.member_id
    INNER JOIN books b
        ON br.book_id = b.book_id
    WHERE m.member_id = p_member_id;
END;
$$;


CREATE OR REPLACE PROCEDURE GetCategoryBooks(
    IN p_category VARCHAR,
    IN p_price_limit NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT *
    FROM books
    WHERE category = p_category
      AND price <= p_price_limit;
END;
$$;


--INTEGRATED SQL PROBLEMS

SELECT DISTINCT m.member_name
FROM members m
INNER JOIN borrow br
    ON m.member_id = br.member_id
INNER JOIN books b
    ON br.book_id = b.book_id
WHERE b.price > (
    SELECT AVG(price)
    FROM books
);


SELECT b.book,
       b.author,
       b.category,
       b.price
FROM books b
WHERE b.price = (
    SELECT MAX(b2.price)
    FROM books b2
    WHERE b2.category = b.category
);


SELECT category,
       AVG(price) AS average_price
FROM books
GROUP BY category
HAVING AVG(price) > (
    SELECT AVG(price)
    FROM books
);


SELECT m.member_id,
       m.member_name,
       COUNT(br.book_id) AS total_books
FROM members m
INNER JOIN borrow br
    ON m.member_id = br.member_id
GROUP BY m.member_id, m.member_name
HAVING COUNT(br.book_id) > 1;


SELECT *
FROM books b
WHERE b.price > 500
  AND NOT EXISTS (
      SELECT 1
      FROM borrow br
      WHERE br.book_id = b.book_id
  );


SELECT book_id,
       book,
       price
FROM (
    SELECT book_id,
           book,
           price,
           ROW_NUMBER() OVER (ORDER BY price DESC) AS rn
    FROM books
) x
WHERE rn <= 3;


SELECT category,
       COUNT(*) AS total_books,
       AVG(price) AS average_price,
       SUM(stock_quantity) AS total_stock
FROM books
GROUP BY category;


SELECT book,
       category,
       price,
       AVG(price) OVER (
           PARTITION BY category
       ) AS category_average_price,
       price - AVG(price) OVER (
           PARTITION BY category
       ) AS difference_from_average
FROM books;


SELECT m.member_id,
       m.member_name,
       COUNT(br.book_id) AS borrowed_books
FROM members m
LEFT JOIN borrow br
    ON m.member_id = br.member_id
GROUP BY m.member_id, m.member_name;


WITH member_counts AS (
    SELECT m.member_id,
           m.member_name,
           COUNT(br.book_id) AS borrowed_books
    FROM members m
    LEFT JOIN borrow br
        ON m.member_id = br.member_id
    GROUP BY m.member_id, m.member_name
)
SELECT *
FROM member_counts
WHERE borrowed_books > (
    SELECT AVG(borrowed_books)
    FROM member_counts
);


SELECT member_name,
       book,
       price
FROM (
    SELECT m.member_name,
           b.book,
           b.price,
           RANK() OVER (
               PARTITION BY m.member_id
               ORDER BY b.price DESC
           ) AS rnk
    FROM members m
    INNER JOIN borrow br
        ON m.member_id = br.member_id
    INNER JOIN books b
        ON br.book_id = b.book_id
) x
WHERE rnk = 1;


SELECT category,
       COUNT(*) AS total_books,
       AVG(price) AS average_price
FROM books
GROUP BY category
HAVING COUNT(*) >= 2
   AND AVG(price) > 500;


SELECT book_id,
       book,
       category,
       price
FROM (
    SELECT book_id,
           book,
           category,
           price,
           ROW_NUMBER() OVER (
               PARTITION BY category
               ORDER BY price DESC
           ) AS rn
    FROM books
) x
WHERE rn <= 2;


SELECT *
FROM books b
WHERE price > (
    SELECT AVG(b2.price)
    FROM books b2
    WHERE b2.category = b.category
)
AND stock_quantity > 5;


CREATE VIEW Book_Borrow_Count AS
SELECT b.book,
       b.category,
       b.price,
       b.stock_quantity AS stock,
       COUNT(br.borrow_id) AS borrow_count
FROM books b
LEFT JOIN borrow br
    ON b.book_id = br.book_id
GROUP BY b.book_id,
         b.book,
         b.category,
         b.price,
         b.stock_quantity;


CREATE OR REPLACE PROCEDURE GetCategoryBooksSorted(
    IN p_category VARCHAR
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT *
    FROM books
    WHERE category = p_category
    ORDER BY price DESC;
END;
$$;


CREATE OR REPLACE PROCEDURE GetBooksByPriceRange(
    IN p_min_price NUMERIC,
    IN p_max_price NUMERIC
)
LANGUAGE plpgsql
AS $$
BEGIN
    SELECT *
    FROM books
    WHERE price BETWEEN p_min_price AND p_max_price;
END;
$$;


WITH category_borrow AS (
    SELECT b.category,
           COUNT(br.borrow_id) AS borrowed_books
    FROM books b
    INNER JOIN borrow br
        ON b.book_id = br.book_id
    GROUP BY b.category
)
SELECT *
FROM category_borrow
WHERE borrowed_books > 2;


SELECT
    CASE
        WHEN price < 400 THEN 'Low'
        WHEN price BETWEEN 400 AND 700 THEN 'Medium'
        ELSE 'High'
    END AS price_category,
    COUNT(*) AS total_books
FROM books
GROUP BY
    CASE
        WHEN price < 400 THEN 'Low'
        WHEN price BETWEEN 400 AND 700 THEN 'Medium'
        ELSE 'High'
    END;


SELECT book_id,
       book,
       category,
       price
FROM (
    SELECT book_id,
           book,
           category,
           price,
           RANK() OVER (
               PARTITION BY category
               ORDER BY price DESC
           ) AS price_rank
    FROM books
) x
WHERE price_rank = 1;


--CHALLENGE QUESTIONS 

SELECT *
FROM books
WHERE price = (
    SELECT MAX(price)
    FROM books
    WHERE price < (
        SELECT MAX(price)
        FROM books
    )
);


SELECT *
FROM books
WHERE price = (
    SELECT MAX(price)
    FROM books
    WHERE price < (
        SELECT MAX(price)
        FROM books
    )
);


SELECT book_id,
       book,
       price
FROM (
    SELECT book_id,
           book,
           price,
           DENSE_RANK() OVER (
               ORDER BY price DESC
           ) AS price_rank
    FROM books
) x
WHERE price_rank = 3;


SELECT category
FROM books
WHERE price = (
    SELECT MAX(price)
    FROM books
);


WITH author_count AS (
    SELECT author,
           COUNT(*) AS total_books
    FROM books
    GROUP BY author
)
SELECT author,
       total_books
FROM author_count
WHERE total_books = (
    SELECT MAX(total_books)
    FROM author_count
);


WITH member_count AS (
    SELECT m.member_id,
           m.member_name,
           COUNT(br.book_id) AS total_books
    FROM members m
    LEFT JOIN borrow br
        ON m.member_id = br.member_id
    GROUP BY m.member_id, m.member_name
)
SELECT *
FROM member_count
WHERE total_books = (
    SELECT MAX(total_books)
    FROM member_count
);


SELECT b.book_id,
       b.book,
       COUNT(br.borrow_id) AS borrow_count
FROM books b
INNER JOIN borrow br
    ON b.book_id = br.book_id
GROUP BY b.book_id, b.book
ORDER BY borrow_count DESC
LIMIT 1;


SELECT *
FROM books b
WHERE NOT EXISTS (
    SELECT 1
    FROM borrow br
    WHERE br.book_id = b.book_id
);


SELECT category
FROM books
GROUP BY category
HAVING MIN(price) > 300;


SELECT category
FROM books
GROUP BY category
HAVING MAX(price) > 800;


SELECT *
FROM books
WHERE price > (
    SELECT AVG(price)
    FROM books
)
AND price < (
    SELECT MAX(price)
    FROM books
);


SELECT book_id,
       book,
       category,
       price
FROM (
    SELECT book_id,
           book,
           category,
           price,
           ROW_NUMBER() OVER (
               PARTITION BY category
               ORDER BY price DESC
           ) AS rn
    FROM books
) x
WHERE rn <= 2;


SELECT m.member_id,
       m.member_name
FROM members m
INNER JOIN borrow br
    ON m.member_id = br.member_id
INNER JOIN books b
    ON br.book_id = b.book_id
GROUP BY m.member_id, m.member_name
HAVING COUNT(DISTINCT b.category) > 1;


SELECT category,
       SUM(price * stock_quantity) AS total_stock_value
FROM books
GROUP BY category
ORDER BY total_stock_value DESC
LIMIT 1;


SELECT SUM(price * stock_quantity) AS total_inventory_value
FROM books;


SELECT category,
       SUM(price * stock_quantity) AS inventory_value
FROM books
GROUP BY category;


SELECT category,
       SUM(price * stock_quantity) AS inventory_value,
       RANK() OVER (
           ORDER BY SUM(price * stock_quantity) DESC
       ) AS category_rank
FROM books
GROUP BY category;


SELECT DISTINCT m.member_name,
       b.book,
       b.price
FROM members m
INNER JOIN borrow br
    ON m.member_id = br.member_id
INNER JOIN books b
    ON br.book_id = b.book_id
WHERE b.price = (
    SELECT MAX(price)
    FROM books
);


SELECT m.member_id,
       m.member_name,
       COUNT(br.book_id) AS borrowed_books,
       RANK() OVER (
           ORDER BY COUNT(br.book_id) DESC
       ) AS member_rank
FROM members m
LEFT JOIN borrow br
    ON m.member_id = br.member_id
GROUP BY m.member_id, m.member_name;


SELECT b.book,
       b.author,
       b.category,
       b.price,
       b.stock_quantity AS stock,
       m.member_name,
       br.borrow_date,

       CASE
           WHEN br.borrow_id IS NULL THEN 'Not Borrowed'
           ELSE 'Borrowed'
       END AS borrow_status,

       CASE
           WHEN b.price < 400 THEN 'Low'
           WHEN b.price BETWEEN 400 AND 700 THEN 'Medium'
           ELSE 'High'
       END AS price_classification,

       RANK() OVER (
           PARTITION BY b.category
           ORDER BY b.price DESC
       ) AS category_price_rank

FROM books b
LEFT JOIN borrow br
    ON b.book_id = br.book_id
LEFT JOIN members m
    ON br.member_id = m.member_id;
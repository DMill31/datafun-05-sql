-- Count all books
SELECT COUNT(*) AS num_books
FROM books;

-- Count all authors
SELECT COUNT(*) AS num_authors
FROM authors;

-- Sum up the number of pages in all books
SELECT SUM(num_pages) AS total_pages
FROM books;

-- Find the average number of pages in all books
SELECT AVG(num_pages) AS avg_pages
FROM books;
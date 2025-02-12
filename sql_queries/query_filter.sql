-- Filter authors by year born
SELECT * FROM authors WHERE year_born < 1900;

-- Filter books by page count
SELECT * FROM books WHERE num_pages > 200 AND num_pages < 500;
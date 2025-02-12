-- Group books by range of number of pages
SELECT COUNT(*) AS num_books, 
       CASE
           WHEN num_pages < 200 THEN '0-199'
           WHEN num_pages < 400 THEN '200-399'
           ELSE '400+'
       END AS page_range
FROM books
GROUP BY page_range;
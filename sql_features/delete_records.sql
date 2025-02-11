-- Delete one of J.R.R. Tolkien's records from the authors table.
DELETE FROM authors
WHERE author_id = '16f3e0a1-24cb-4ed6-a50d-509f63e367f7';

-- Now delete the corresponding book from the books table.
DELETE FROM books
WHERE author_id = '16f3e0a1-24cb-4ed6-a50d-509f63e367f7';
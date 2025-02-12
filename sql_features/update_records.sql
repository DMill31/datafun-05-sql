-- Update a record in the specified table

-- Change title of Harry Potter to the American version
UPDATE books
SET title = "Harry Potter and the Sorcerer's Stone"
WHERE book_id = 'ca8e64c3-1e67-47f5-82cc-3e4e30f63b75';

-- Add a column to the authors table for the year the author was born
ALTER TABLE authors
ADD year_born INTEGER NULL;
-- Now insert the values
UPDATE authors SET year_born = 1926
WHERE author_id = '10f88232-1ae7-4d88-a6a2-dfcebb22a596';
UPDATE authors SET year_born = 1903
WHERE author_id = 'c3a47e85-2a6b-4196-a7a8-8b55d8fc1f70';
UPDATE authors SET year_born = 1896
WHERE author_id = 'e0b75863-866d-4db4-85c7-df9bb8ee6dab';
UPDATE authors SET year_born = 1894
WHERE author_id = '7b144e32-7ff4-4b58-8eb0-e63d3c9f9b8d';
UPDATE authors SET year_born = 1919
WHERE author_id = '8d8107b6-1f24-481c-8a21-7d72b13b59b5';
UPDATE authors SET year_born = 1920
WHERE author_id = '0cc3c8e4-e0c0-482f-b2f7-af87330de214';
UPDATE authors SET year_born = 1775
WHERE author_id = '4dca0632-2c53-490c-99d5-4f6d41e56c0e';
UPDATE authors SET year_born = 1892
WHERE author_id = '16f3e0a1-24cb-4ed6-a50d-509f63e367f7' OR author_id = '06cf58ab-90f1-448d-8e54-055e4393e75c';
UPDATE authors SET year_born = 1965
WHERE author_id = '6b693b96-394a-4a1d-a4e2-792a47d7a568';

-- Add a column to the books table for the number of pages in the book

ALTER TABLE books
ADD num_pages INTEGER NULL;
-- Now insert the values
UPDATE books SET num_pages = 281
WHERE book_id = 'd6f83870-ff21-4a5d-90ab-26a49ab6ed12';
UPDATE books SET num_pages = 328
WHERE book_id = '0f5f44f7-44d8-4f49-b8c4-c64d847587d3';
UPDATE books SET num_pages = 180
WHERE book_id = 'f9d9e7de-c44d-4d1d-b3ab-59343bf32bc2';
UPDATE books SET num_pages = 259
WHERE book_id = '38e530f1-228f-4d6e-a587-2ed4d6c44e9c';
UPDATE books SET num_pages = 214
WHERE book_id = 'c2a62a4b-cf5c-4246-9bf7-b2601d542e6d';
UPDATE books SET num_pages = 158
WHERE book_id = '3a1d835c-1e15-4a48-8e8c-b12239604e98';
UPDATE books SET num_pages = 279
WHERE book_id = 'c6e67918-e509-4a6b-bc3a-979f6ad802f0';
UPDATE books SET num_pages = 310
WHERE book_id = 'be951205-6cc2-4b3d-96f1-7257b8fc8c0f';
UPDATE books SET num_pages = 1178
WHERE book_id = 'dce0f8f2-d3ed-48a9-b8ff-960b6baf1f6f';
UPDATE books SET num_pages = 309
WHERE book_id = 'ca8e64c3-1e67-47f5-82cc-3e4e30f63b75';

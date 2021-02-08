-- ## CHALLENGE 1

USE publications;

SELECT au.au_id, au.au_lname, au.au_fname, tt.title, pb.pub_name
FROM authors AS au JOIN titleauthor AS ta
ON au.au_id = ta.au_id
JOIN titles AS tt
ON tt.title_id = ta.title_id
LEFT JOIN publishers AS pb
ON tt.pub_id = pb.pub_id;

-- ## CHALLENGE 2

CREATE TEMPORARY TABLE temp1

SELECT au.au_id, au.au_lname, au.au_fname, pb.pub_name, COUNT(title)
FROM authors AS au JOIN titleauthor AS ta
ON au.au_id = ta.au_id
JOIN titles AS tt
ON tt.title_id = ta.title_id
LEFT JOIN publishers AS pb
ON tt.pub_id = pb.pub_id
GROUP BY au_id, au_lname, au_fname, pub_name
ORDER BY au_id DESC;

-- ## CHALLENGE 3

SELECT au.au_id, au.au_lname, au.au_fname, COUNT(title)
FROM authors AS au JOIN titleauthor AS ta
ON au.au_id = ta.au_id
JOIN titles AS tt
ON tt.title_id = ta.title_id
LEFT JOIN publishers AS pb
ON tt.pub_id = pb.pub_id
GROUP BY au_id, au_lname, au_fname
ORDER BY COUNT(title) DESC LIMIT 3;

-- ## CHALLENGE 4

SELECT au.au_id, au.au_lname, au.au_fname, COUNT(title)
FROM authors AS au LEFT JOIN titleauthor AS ta
ON au.au_id = ta.au_id
LEFT JOIN titles AS tt
ON tt.title_id = ta.title_id
LEFT JOIN publishers AS pb
ON tt.pub_id = pb.pub_id
GROUP BY au_id, au_lname, au_fname
ORDER BY COUNT(title) DESC;

-- ## BONUS

SELECT au.au_id, au.au_lname, au.au_fname, SUM(tt.advance + tt.royalty)
FROM authors AS au LEFT JOIN titleauthor AS ta
ON au.au_id = ta.au_id
LEFT JOIN titles AS tt
ON tt.title_id = ta.title_id
LEFT JOIN publishers AS pb
ON tt.pub_id = pb.pub_id
GROUP BY au_id, au_lname, au_fname
ORDER BY SUM(tt.advance + tt.royalty) DESC LIMIT 3;
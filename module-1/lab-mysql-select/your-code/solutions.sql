-- CHALLENGE 1
SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', titles.title AS 'TITLE', publishers.pub_name AS 'Publisher' FROM authors
	LEFT JOIN titleauthor
	ON authors.au_id = titleauthor.au_id
	INNER JOIN titles
	ON titleauthor.title_id = titles.title_id
	RIGHT JOIN publishers
	ON titles.pub_id = publishers.pub_id
	WHERE titles.pub_id IS NOT NULL;

-- Ramon pointed out a LEFT JOIN would negate my need for the WHERE condition on my RIGHT JOIN with publishers table
/* SELECT authors.au_id, authors.au_lname, authors.au_fname, titles.title, publishers.pub_name FROM authors
	LEFT JOIN titleauthor
	ON authors.au_id = titleauthor.au_id
	INNER JOIN titles
	ON titleauthor.title_id = titles.title_id
	LEFT JOIN publishers
	ON titles.pub_id = publishers.pub_id; */

-- CHALLENGE 2
SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', publishers.pub_name AS 'Publisher', COUNT(titles.title) AS 'TITLE COUNT' FROM authors
	LEFT JOIN titleauthor
	ON authors.au_id = titleauthor.au_id
	INNER JOIN titles
	ON titleauthor.title_id = titles.title_id
	RIGHT JOIN publishers
	ON titles.pub_id = publishers.pub_id
	WHERE titles.pub_id IS NOT NULL
	GROUP BY authors.au_id, 'TITLE COUNT', publishers.pub_name
	ORDER BY authors.au_id DESC;

-- CHALLENGE 3
SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', SUM(sales.qty) AS 'TOTAL' FROM AUTHORS
	LEFT JOIN titleauthor
	ON authors.au_id = titleauthor.au_id
	JOIN sales
	ON titleauthor.title_id = sales.title_id
	GROUP BY authors.au_id
	ORDER BY SUM(sales.qty) DESC
	LIMIT 3
	;

-- CHALLENGE 4
SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', COALESCE(SUM(sales.qty), 0) AS 'TOTAL' FROM AUTHORS
	LEFT JOIN titleauthor
	ON authors.au_id = titleauthor.au_id
	LEFT JOIN sales
	ON titleauthor.title_id = sales.title_id
	GROUP BY authors.au_id
	ORDER BY SUM(sales.qty) DESC
	;


-- BONUS - STILL IN PROGRESS
/* SELECT authors.au_id, authors.au_lname, authors.au_fname, SUM(sales.qty)
	FROM authors
	JOIN titleauthor
	ON authors.au_id = titleauthor.au_id
	JOIN titles
	ON titleauthor.title_id = titles.title_id
	JOIN sales
	ON titles.title_id = sales.title_id
	GROUP BY authors.au_id
	ORDER BY SUM(sales.qty) DESC
	;
*/ 

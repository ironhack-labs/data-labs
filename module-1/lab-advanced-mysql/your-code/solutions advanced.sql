-- CHALLENGE 1
-- STEP 1
SELECT titleauthor.au_id, 
titles.title_id, 
titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100 as Sales_Royalty
FROM titleauthor
INNER JOIN titles ON titleauthor.title_id = titles.title_id
INNER JOIN sales ON sales.title_id = titles.title_id

-- STEP 2
SELECT titleauthor.au_id, 
titles.title_id, 
SUM(titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100) as Sales_Royalty
FROM titleauthor
INNER JOIN titles ON titleauthor.title_id = titles.title_id
INNER JOIN sales ON sales.title_id = titles.title_id
GROUP BY titleauthor.au_id, titles.title_id

-- STEP 3
SELECT p.AUTHOR_ID, SUM(Sales_Royalty) AS Profits FROM
	(SELECT ta.au_id AS AUTHOR_ID, 
	t.title_id AS TITLE, 
	SUM(t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100) as Sales_Royalty
	FROM titleauthor ta
	INNER JOIN titles t ON ta.title_id = t.title_id
	INNER JOIN sales s ON s.title_id = t.title_id
	GROUP BY ta.au_id, t.title_id) AS p
GROUP BY p.AUTHOR_ID

-- CHALLENGE 2
-- STEP 1
CREATE TEMPORARY TABLE sales_royalty
SELECT ta.au_id AS AUTHOR_ID, 
t.title_id AS TITLE, 
t.price * s.qty * t.royalty / 100 * ta.royaltyper / 100 AS Sales_Royalty
FROM titleauthor ta
INNER JOIN titles t ON ta.title_id = t.title_id
INNER JOIN sales s ON s.title_id = t.title_id

-- STEP 2
SELECT AUTHOR_ID, 
TITLE, 
SUM(Sales_Royalty) AS Sales_Royalty
FROM sales_royalty
GROUP BY AUTHOR_ID, TITLE

-- STEP 3
SELECT AUTHOR_ID, 
SUM(Sales_Royalty) AS Sales_Royalty
FROM sales_royalty
GROUP BY AUTHOR_ID

-- CHALLENGE 3
CREATE TABLE most_profiting_authors
	SELECT AUTHOR_ID AS au_id, 
	SUM(Sales_Royalty) AS profits
	FROM sales_royalty
	GROUP BY AUTHOR_ID
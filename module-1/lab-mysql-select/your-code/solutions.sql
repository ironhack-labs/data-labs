-- CHALLENGE 1
SELECT 
authors.au_id AS 'AUTHOR ID',
authors.au_lname AS 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
titles.title AS 'TITLE',
publishers.pub_name AS 'PUBLIHSER'

FROM authors
JOIN titleauthor
ON authors.au_id = titleauthor.au_id
JOIN titles
ON titleauthor.title_id = titles.title_id
JOIN publishers
ON titles.pub_id = publishers.pub_id;

-- CHALLENGE 2

SELECT `AUTHOR ID`, `LAST NAME`, `FIRST NAME`, PUBLISHER, COUNT(TITLE) as 'TITLE COUNT' 

FROM(
SELECT 
authors.au_id AS 'AUTHOR ID',
authors.au_lname AS 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
titles.title AS 'TITLE',
publishers.pub_name AS 'PUBLISHER'

FROM authors
JOIN titleauthor
ON authors.au_id = titleauthor.au_id
JOIN titles
ON titleauthor.title_id = titles.title_id
JOIN publishers
ON titles.pub_id = publishers.pub_id
)
 AS B GROUP BY `AUTHOR ID`, `LAST NAME`, `FIRST NAME`, PUBLISHER
ORDER BY `AUTHOR ID` DESC;

-- CHALLENGE 3

SELECT
`AUTHOR ID`, `LAST NAME`, `FIRST NAME`, TOTAL

FROM(
SELECT 
authors.au_id AS 'AUTHOR ID',
authors.au_lname AS 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
SUM(titles.price * sales.qty) OVER(PARTITION BY authors.au_id) AS 'Total'

FROM authors
JOIN titleauthor
ON authors.au_id = titleauthor.au_id
JOIN titles
ON titleauthor.title_id = titles.title_id
JOIN sales
ON titleauthor.title_id = sales.title_id
)
AS S GROUP BY `AUTHOR ID`, TOTAL
ORDER BY TOTAL DESC
LIMIT 3;



-- CHALLENGE 4

SELECT 
`AUTHOR ID`, `LAST NAME`, `FIRST NAME`, IFNULL(TOTAL, 0)

FROM(
SELECT 
authors.au_id AS 'AUTHOR ID',
authors.au_lname AS 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
SUM(titles.price * sales.qty) OVER(PARTITION BY authors.au_id) AS 'Total'

FROM authors
LEFT JOIN titleauthor
ON authors.au_id = titleauthor.au_id
LEFT JOIN titles
ON titleauthor.title_id = titles.title_id
LEFT JOIN sales
ON titleauthor.title_id = sales.title_id
)
AS S GROUP BY `AUTHOR ID`, TOTAL

ORDER BY TOTAL DESC
LIMIT 23;


-- BONUS CHALLENGE

SELECT
`AUTHOR ID`, `LAST NAME`, `FIRST NAME`, TOTAL

FROM(
SELECT 
authors.au_id AS 'AUTHOR ID',
authors.au_lname AS 'LAST NAME',
authors.au_fname AS 'FIRST NAME',
SUM(titles.price * sales.qty*titles.royalty/100*titleauthor.royaltyper/100+titles.advance) OVER(PARTITION BY authors.au_id) AS 'Total'

FROM authors
JOIN titleauthor
ON authors.au_id = titleauthor.au_id
JOIN titles
ON titleauthor.title_id = titles.title_id
JOIN sales
ON titleauthor.title_id = sales.title_id
)
AS S GROUP BY `AUTHOR ID`, TOTAL
ORDER BY TOTAL DESC
LIMIT 3;
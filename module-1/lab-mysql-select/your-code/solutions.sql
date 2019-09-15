SHOW DATABASES;
USE lab_mysql_select;

--### Challenge 1 - Who Have Published What At Where?
CREATE TABLE challenge_1
	SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', title AS 'TITLE', pub_name AS 'PUBLISHER'
	FROM authors JOIN titleauthor
	ON authors.au_id = titleauthor.au_id
	JOIN titles
	ON titleauthor.title_id = titles.title_id
	JOIN publishers
	ON titles.pub_id = publishers.pub_id
	;
SELECT * FROM challenge_1;

SELECT COUNT(authors.au_id) FROM authors;
SELECT COUNT(challenge_1.au_id) FROM challenge_1;

--### Challenge 2 - Who Have Published How Many At Where?

CREATE TABLE challenge_2
	SELECT au_id AS 'AUTHOR ID', au_lname AS 'LAST NAME', au_fname AS 'FIRST NAME', pub_name AS 'PUBLISHER', COUNT(title) AS 'TITLE COUNT'
	FROM challenge_1
	GROUP BY au_lname, au_fname, pub_name
	ORDER BY au_id DESC, COUNT(title) DESC
	;
	
SELECT * FROM challenge_2;

SELECT COUNT(titleauthor.title_id) FROM titleauthor;
SELECT COUNT(title) FROM challenge_1;

--### Challenge 3 - Best Selling Authors

CREATE TABLE challenge_3
	SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', titles.ytd_sales AS 'TOTAL'
	FROM authors JOIN titleauthor
	ON authors.au_id = titleauthor.au_id
	JOIN titles
	ON titleauthor.title_id = titles.title_id
	GROUP BY authors.au_id
	ORDER BY titles.ytd_sales DESC
	LIMIT 3;

SELECT * FROM challenge_3;

--### Challenge 4 - Best Selling Authors Ranking

CREATE TABLE challenge_4
	SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', titles.ytd_sales AS 'TOTAL'
	FROM authors JOIN titleauthor
	ON authors.au_id = titleauthor.au_id
	JOIN titles
	ON titleauthor.title_id = titles.title_id
	GROUP BY authors.au_id
	ORDER BY titles.ytd_sales DESC
	;

SELECT * FROM challenge_4;
	
--### Bonus Challenge - Most Profiting Authors

CREATE TABLE bonus_challenge
	SELECT authors.au_id AS 'AUTHOR ID', authors.au_lname AS 'LAST NAME', authors.au_fname AS 'FIRST NAME', SUM(titles.advance + (titles.royalty*titleauthor.royaltyper*titles.ytd_sales)) AS 'PROFIT'
	FROM authors JOIN titleauthor
	ON authors.au_id = titleauthor.au_id
	JOIN titles
	ON titleauthor.title_id = titles.title_id
	GROUP BY authors.au_id
	ORDER BY SUM(titles.advance + (titles.royalty*titleauthor.royaltyper*titles.ytd_sales)) DESC
	LIMIT 3;

SELECT * FROM bonus_challenge;
-- Lab | Advanced MySQL

-- Challenge 1 - Most Profiting Authors
-- Step 1: Calculate the royalties of each sales for each author
SELECT 
`Title ID`, `Author ID`, `Royalty`

FROM(
SELECT 
titleauthor.title_id AS 'Title ID',
titleauthor.au_id AS 'Author ID',
titles.price * sales.qty * titles.royalty/100 *titleauthor.royaltyper/100 AS 'Royalty'

FROM titleauthor
JOIN titles
ON titleauthor.title_id = titles.title_id
JOIN sales
ON titleauthor.title_id = sales.title_id
)
AS A GROUP BY `Author ID`, `Title ID`, Royalty
;

-- Step 2: Aggregate the total royalties for each title for each author
SELECT 
`Title ID`, `Author ID`, `Royalty`

FROM(
SELECT 
titleauthor.title_id AS 'Title ID',
titleauthor.au_id AS 'Author ID',
SUM(titles.price * sales.qty * titles.royalty/100 *titleauthor.royaltyper/100) OVER(PARTITION BY titleauthor.au_id) AS 'Royalty'

FROM titleauthor
JOIN titles
ON titleauthor.title_id = titles.title_id
JOIN sales
ON titleauthor.title_id = sales.title_id
)
AS A GROUP BY `Author ID`, `Title ID`, Royalty
;

-- Step 3: Calculate the total profits of each author
SELECT 
`Author ID`, `Profit`

FROM(
SELECT 
titleauthor.title_id AS 'Title ID',
titleauthor.au_id AS 'Author ID',
SUM(titles.price * sales.qty * titles.royalty/100 *titleauthor.royaltyper/100 + titles.advance) OVER(PARTITION BY titleauthor.au_id) AS 'Profit'

FROM titleauthor
JOIN titles
ON titleauthor.title_id = titles.title_id
JOIN sales
ON titleauthor.title_id = sales.title_id
)
AS A GROUP BY `Author ID`, Profit
ORDER BY Profit DESC
LIMIT 3;

-- Challenge 2 - Alternative Solution

CREATE TEMPORARY TABLE temp1

SELECT 
titleauthor.title_id AS 'Title ID',
titleauthor.au_id AS 'Author ID',
SUM(titles.price * sales.qty * titles.royalty/100 *titleauthor.royaltyper/100 + titles.advance) OVER(PARTITION BY titleauthor.au_id) AS 'Profit'

FROM titleauthor
JOIN titles
ON titleauthor.title_id = titles.title_id
JOIN sales
ON titleauthor.title_id = sales.title_id
;

SELECT 
`Author ID`, `Profit`
FROM 
temp1
GROUP BY `Author ID`, Profit
ORDER BY Profit DESC
LIMIT 3;

-- Challenge 3

CREATE TABLE most_profiting_authors AS

SELECT
distinct titleauthor.au_id AS 'Author ID',
SUM(titles.price * sales.qty * titles.royalty/100 *titleauthor.royaltyper/100 + titles.advance) OVER(PARTITION BY titleauthor.au_id) AS 'Profit'

FROM titleauthor
JOIN titles
ON titleauthor.title_id = titles.title_id
JOIN sales
ON titleauthor.title_id = sales.title_id
;

SELECT * FROM most_profiting_authors;
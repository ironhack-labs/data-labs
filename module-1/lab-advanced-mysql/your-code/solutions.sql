-- Initial solution completed using temporary tables
-- Step 1: calculate the royalties of each sale for each author (include the advances here, you'll need it later)
SELECT titleauthor.title_id AS TitleID, titleauthor.au_id AS AuthorID, (titles.price * sales.qty * (titles.royalty / 100) * (titleauthor.royaltyper / 100) ) AS SalesRoyalty, (titles.advance * (titleauthor.royaltyper / 100)) AS SalesAdvance
FROM titleauthor
JOIN titles ON titleauthor.title_id = titles.title_id
JOIN sales ON titles.title_id = sales.title_id
;

-- Step 2: aggregate the total royalties per title for each author
CREATE TEMPORARY TABLE temptable1 (SELECT titleauthor.title_id AS TitleID, titleauthor.au_id AS AuthorID, (titles.price * sales.qty * (titles.royalty / 100) * (titleauthor.royaltyper / 100) ) AS SalesRoyalty, (titles.advance * (titleauthor.royaltyper / 100)) AS SalesAdvance
FROM titleauthor
JOIN titles ON titleauthor.title_id = titles.title_id
JOIN sales ON titles.title_id = sales.title_id);

SELECT TitleID, AuthorID, SUM(SalesRoyalty) AS TotalRoyalties, SUM(SalesAdvance) AS TotalAdvance
FROM temptable1
GROUP BY TitleID, AuthorID;

-- Step 3: aggregate the total royalties and total advances by author, and retrieve the 3 with the top profits, in descending order
CREATE TEMPORARY TABLE temptable2 (SELECT TitleID, AuthorID, SUM(SalesRoyalty) AS TotalRoyalties, SUM(SalesAdvance) AS TotalAdvance
FROM temptable1
GROUP BY TitleID, AuthorID);

SELECT AuthorId, (TotalRoyalties + TotalAdvance) AS TotalProfit
FROM temptable2
ORDER BY TotalProfit DESC
LIMIT 3;

-- Alternate solution using derived tables
-- Step 1: calculate the royalties of each sale for each author (include the advances here, you'll need it later)
SELECT titleauthor.title_id AS TitleID, titleauthor.au_id AS AuthorID, (titles.price * sales.qty * (titles.royalty / 100) * (titleauthor.royaltyper / 100) ) AS SalesRoyalty, (titles.advance * (titleauthor.royaltyper / 100)) AS SalesAdvance
FROM titleauthor
JOIN titles ON titleauthor.title_id = titles.title_id
JOIN sales ON titles.title_id = sales.title_id
;

-- Step 2: aggregate the total royalties per title for each author
SELECT TitleID, AuthorID, SUM(SalesRoyalty) AS TotalRoyalties, SUM(SalesAdvance) AS TotalAdvance
    FROM (SELECT titleauthor.title_id AS TitleID, titleauthor.au_id AS AuthorID, (titles.price * sales.qty * (titles.royalty / 100) * (titleauthor.royaltyper / 100) ) AS SalesRoyalty, (titles.advance * (titleauthor.royaltyper / 100)) AS SalesAdvance
FROM titleauthor
JOIN titles ON titleauthor.title_id = titles.title_id
JOIN sales ON titles.title_id = sales.title_id)
    AS royalties_table
    GROUP BY royalties_table.TitleID, royalties_table.AuthorID;


-- Step 3: aggregate the total royalties and total advances by author, and retrieve the 3 with the top profits, in descending order
SELECT AuthorId, (TotalRoyalties + TotalAdvance) AS TotalProfit
FROM (SELECT TitleID, AuthorID, SUM(SalesRoyalty) AS TotalRoyalties, SUM(SalesAdvance) AS TotalAdvance
    FROM (SELECT titleauthor.title_id AS TitleID, titleauthor.au_id AS AuthorID, (titles.price * sales.qty * (titles.royalty / 100) * (titleauthor.royaltyper / 100) ) AS SalesRoyalty, (titles.advance * (titleauthor.royaltyper / 100)) AS SalesAdvance
FROM titleauthor
JOIN titles ON titleauthor.title_id = titles.title_id
JOIN sales ON titles.title_id = sales.title_id)
    AS royalties_table
    GROUP BY royalties_table.TitleID, royalties_table.AuthorID)
    AS agg_royalties_table
ORDER BY TotalProfit DESC
LIMIT 3;

-- Alternate Solution that creates a permanent table from previous solution
CREATE TABLE most_profiting_authors 
SELECT AuthorId AS au_id, TotalProfit AS profits
FROM(SELECT AuthorId, (TotalRoyalties + TotalAdvance) AS TotalProfit
FROM (SELECT TitleID, AuthorID, SUM(SalesRoyalty) AS TotalRoyalties, SUM(SalesAdvance) AS TotalAdvance
    FROM (SELECT titleauthor.title_id AS TitleID, titleauthor.au_id AS AuthorID, (titles.price * sales.qty * (titles.royalty / 100) * (titleauthor.royaltyper / 100) ) AS SalesRoyalty, (titles.advance * (titleauthor.royaltyper / 100)) AS SalesAdvance
FROM titleauthor
JOIN titles ON titleauthor.title_id = titles.title_id
JOIN sales ON titles.title_id = sales.title_id)
    AS royalties_table
    GROUP BY royalties_table.TitleID, royalties_table.AuthorID
) AS agg_royalties_table
ORDER BY TotalProfit DESC
LIMIT 3) AS total_profit_author;

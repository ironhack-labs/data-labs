select database() publications ;
create temporary table Authors_Profits_helper
select titles.title_id as Title_ID, authors.au_id as AUTHOR_ID , 
sum(ROUND(titles.price * sales.qty *titles.royalty/100 *titleauthor.royaltyper/100,3)) as Total_Royalty,
titles.advance as Advance
FROM authors
Join titleauthor on titleauthor.au_id = authors.au_id
Join titles on titles.title_id = titleauthor.title_id
Join sales on sales.title_id = titles.title_id
group by authors.au_id;
select AUTHOR_ID, (Total_Royalty+Advance) as Profits from Authors_Profits_helper
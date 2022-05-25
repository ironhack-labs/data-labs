select database() publications ;
select titles.title_id as Title_ID, authors.au_id as AUTHOR_ID , 
sum(ROUND(titles.price * sales.qty *titles.royalty/100 *titleauthor.royaltyper/100,3)) as Total_Royalty,
titles.advance as Advance,
sum(ROUND(titles.price * sales.qty *titles.royalty/100 *titleauthor.royaltyper/100,3)) + titles.advance as Profits
FROM authors
Join titleauthor on titleauthor.au_id = authors.au_id
Join titles on titles.title_id = titleauthor.title_id
Join sales on sales.title_id = titles.title_id
group by authors.au_id
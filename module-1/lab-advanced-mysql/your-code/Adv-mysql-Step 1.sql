select database() publications ;
select titles.title_id as  'Title ID', authors.au_id as 'AUTHOR ID' , 
sum(ROUND(titles.price * sales.qty * titles.royalty / 100 * titleauthor.royaltyper / 100,3)) as 'Royalty for each author'
FROM authors
Join titleauthor on titleauthor.au_id = authors.au_id
Join titles on titles.title_id = titleauthor.title_id
Join sales on sales.title_id = titles.title_id
group by authors.au_id
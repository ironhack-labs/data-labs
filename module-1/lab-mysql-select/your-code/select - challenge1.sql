select database() publications ;
select authors.au_id as 'AUTHOR ID' , authors.au_lname AS 'LAST NAME', authors.au_fname as 'First Name', titles.title as 'Title', publishers.pub_name as 'Publisher'
FROM authors
Join titleauthor on titleauthor.au_id = authors.au_id
Join titles on titles.title_id = titleauthor.title_id
Join publishers on publishers.pub_id = titles.pub_id
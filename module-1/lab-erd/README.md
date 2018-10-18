![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Entity Relationship Diagram

## Introduction
![Boss_gif](https://tenor.com/view/like-aboss-boss-suits-gabriel-macht-harvey-specter-gif-3540818.gif)

You have been hired by the company one week ago. The CEO wants to explore new markets to expand the business. He asked your boss to run some previous analysis before launching the business in a new country. Your boss has a last-minute trip to Lisboa to solve some "important brownies". 

He trusts you a lot and he asked you for designing the database where you will store the data for further analysis(i.e. sales trends, customer loyalty,most sold products, etc...). You will need to define the entities, the entities' attributes and the relationships among entities. Hurry up!! You need to have it ready before your boss returns.   

Choose your prefered company, think about how the business work and the data that best define the business operation model.

**NOTE: Remember to spend some time thinking about the approach before getting down to the task. Draw it on a piece of paper** 

* **SPOTIFY**: This company needs to store inside a database songs, playlists, favorites, users and paid accounts, etc...
* **AMAZON**: Here you have to conform a schema that handles Products, Reviews, ProductOwners, Users, Track package delivery, etc…
* **IRONHACK**: We need to store users, campus, education staff, alumni, etc.

You are a super hands-on data analyst so trust yourself. You will be doing great!!

**Happy coding and analyzing!!**

## Exercise Iterations

1. With your chosen company create an entity relationship diagram (ERD) using mysql workbench. It should contain at least 5 entities each of whom should have at least 5 attributes. To deliver this iteration do a screenshot of the entities in MySql workbench

2. Create at least 1 one-to-one relationship, 3 many-to-one relationships and 2 many-to-many relationships in your ERD.
To dever this iteration give us the SQL file output via MySql Menu: Database > Foward Engineer.

3. Imagine that now, the company has to make invoices to their costumers. Add to your ERD entities to store billing information and invoices for their costumers, also make relations with current entities if necessary. Deliver like iteration 2.

4. Perform a normalization step to ensure that different entities in the data will have their own respective tables.


## Deliverables

- A **project.sql** file containing the entities,attributes and the relationships used in the construction of your database.
- A **README.md** file containing an explanation of the process followed in the construction of your database and analytical workflow, results obtained, obstacles encountered, and lessons learned.

## Submission

- Upon completion, commit your code and submit to github. **REMEMBER TO FORK THE REPO BEFORE**!!

  ```
  git add .
  git commit -m "done"
  git push origin master
  ```

- Navigate to your repo and [create a Pull Request](https://help.github.com/articles/creating-a-pull-request/).
- Create a pull request with title following this format: **"[<your_campus>][<bootcamp_code>] <your_name>"**
  If you are doing data bootcamp in Madrid and your name is Marc it should be like this: "[MAD][datamad10108] Marc Pomar"
- If you have successfully created the pull request you are done!  CONGRATS :)


## Extra Resources
- https://dev.mysql.com/downloads/file/?id=479204
- https://dev.mysql.com/doc/workbench/en/
- https://www.lucidchart.com/pages/ER-diagram-symbols-and-meaning
- https://dev.mysql.com/doc/workbench/en/workbench-faq.html

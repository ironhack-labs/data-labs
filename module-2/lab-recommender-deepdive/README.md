![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Recommender Systems Deep Dive

## Introduction

There are many different approaches that we can take when creating recommender systems. In the Intro to Recommender Systems lesson and lab, we put together a user similarity based recommender that first calculated the similarities between users and then leveraged a rank-based item recommender within each group of similar customers. In other words, for a given user, our recommender found the top 5 customers who were the most similar to them, aggregated and ranked the purchases of those 5 customers, and then recommended the top 5 most popular products among that group of similar users to the customer.

In this lab, we are going to start out with the same data set, but we are going to dive deeper into the analysis of customers and products and look at an alternative way to generate recommendations.

## Getting Started

Open the `main.ipynb` file in the `your-code` directory. There are a bunch of questions to be solved. If you get stuck in one exercise you can skip to the next one. Read each instruction carefully and provide your answer beneath it.

## Deliverables

- `main.ipynb` with your responses to each of the exercises.

## Submission

Upon completion, add your deliverables to git. Then commit git and push your branch to the remote.

## Resources

- [Recommender Systems](https://en.wikipedia.org/wiki/Recommender_system)
- [Collaborative Filtering](https://en.wikipedia.org/wiki/Collaborative_filtering)
- [Item-Based Collaborative Filtering](https://en.wikipedia.org/wiki/Item-item_collaborative_filtering)
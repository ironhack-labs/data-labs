![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Advanced Topic: Network Analysis

## Objectives

- Understand the basics of network/graph analysis
- Build graphs using the Python Networkx library
- Compute graph statistics and conduct basic network analysis
- Create graphs from existing data in pandas data frames
- Create data visualizations from network data
- Perform deeper analysis of network graphs
- Understand how to incorporate network analysis in your final project

## Graph Theory and Network Structure

Network analysis (also called graph analysis) is a very important, very useful, but often underrated part of data analytics. Its primary purpose is to examine relationships between entities. One of the most obvious targets for network analysis are social networks, where the entities are people and the relationships between them are based on whether someone is friends with (or has followed) someone else.

However, only applying network analysis to social networks is limiting and merely scratches the surface of what you can do with it. Networks are actually ubiquitous: they are everywhere. Look around you. Every object you see is an entity and they can be connected to each other as part of a network based on anything they have in common - whether or not they belong to you, they are electronic, they are writing instruments, they are furniture, they are located in the same room, etc. When you practice thinking about connections in this way, then you start to see networks everywhere. This is the type of thinking you should utilize when analyzing networks.


Source: https://www.youtube.com/watch?v=HkbMUrgzwMs


- Concept of networks
- Graph theory
- Nodes
- Edges
- Graph types
- Introduction to the Networkx library
- Building graphs from scratch

## Analyzing Networks

- Graph statistics
    - Number of nodes
    - Number of edges
    - Average degree
    - Density
    - Diameter
    - Average distance
- Centrality
    - Betweenness
    - Closeness
    - Eigenvector
    - Degree
    - PageRank

## Building and Analyzing Graphs from Existing Data

- Identifying entities
- Identifying & defining relationships
- Transforming data to graph structure
- Converting data frames to graphs

Recall from previous lessons in the program that when data is structured in a tabular format, entities are typically represented by rows and attributes (or features) of the entities are typically represented by the columns in the table.

- Analyzing networks extracted from data

## Visualization of Network Data

- Network visualizations
    - Different layouts - spring, circular, etc.
- Other ways to visualize network data
    - Bar charts
    - Scatter plots
    - Line charts

## Deeper Analysis of Networks

- Subgraphs
- Hierarchical graphs
- Querying graphs
- Community detection
- Clustering

## Resources

- [Wikipedia: Graph Theory](https://en.wikipedia.org/wiki/Graph_theory)
- [PyCon 2018: Network Analysis Made Simple, Part 1 Tutorial](https://www.youtube.com/watch?v=HkbMUrgzwMs)
- [PyCon 2018: Network Analysis Made Simple, Part 2 Tutorial](https://www.youtube.com/watch?v=MRCLwmYTVpc)
- [Networkx Documentation](https://networkx.github.io/documentation/stable/)
- [DataCamp Social Network Analysis Article](https://www.datacamp.com/community/tutorials/social-network-analysis-python)
![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Advanced Topic: Network Analysis

## Overview

### Objectives

- Understand the basics of network/graph analysis
- Build graphs from scratch using the Python Networkx library
- Compute graph statistics and conduct basic network analysis
- Create graphs from existing data in pandas data frames
- Create data visualizations from network data
- Perform deeper analysis of network graphs
- Understand how to incorporate network analysis in your final project

### Ingredients

* Data Analysis - 100%
* Data Engineering - 0%

### Difficulty Level

★★★★ Intermediate

## Graph Theory and Network Composition

Network analysis (also called graph analysis) is a very important, very useful, but often underrated part of data analytics. Its primary purpose is to examine relationships between entities. One of the most obvious targets for network analysis are social networks, where the entities are people and the relationships between them are based on whether someone is friends with (or has followed) someone else.

However, only applying network analysis to social networks is limiting and merely scratches the surface of what you can do with it. Networks are actually ubiquitous: they are everywhere. Look around you. Every object you see is an entity, and they can be connected to each other as part of a network based on anything they have in common - whether or not they belong to you, they are electronic, they are writing instruments, they are furniture, they are located in the same room, etc. When you practice thinking about connections in this way, then you start to see networks everywhere. This is the type of thinking you should utilize when analyzing networks.

[Graph theory](https://en.wikipedia.org/wiki/Graph_theory) is the study of mathematical structures called graphs which model the pairwise relationships between entities. Graph theory provides us with a mathematical foundation and tools with which we can analyze networks, since networks are essentially constructed from relationships between pairs of entities.

Whenever we define a graph, we define it in terms of its *nodes* and *edges*, and visually, they look like the image below. The nodes in the graph represent the entities in our network and the edges are visualized as lines that connect nodes where a relationship exists between the entities they represent.

![Graph Nodes and Edges](./images/graph-nodes-and-edges.png)

There are also two main types of graphs:

- **Directed** - there is a direction to the relationship (e.g. Person A follows Person B).
- **Undirected** - the relationship is nondirectional (e.g. Person A and Person B are friends).

[Networkx](https://networkx.github.io/documentation/stable/) is a Python library for performing network analysis. It has a variety of methods for building graph objects, computing graph statistics, running algorithms on them, and even visualizing them.

If you don't already have Networkx installed, you can pip install it as follows.

```bash
$ pip install networkx
```

Once it is installed, you can import it as follows. It is typically aliased to `nx`.

```python
import networkx as nx
```

From there, you can create a graph by using the `Graph` method.

```python
G = nx.Graph()
```

Once the graph is created, you can add nodes and edges to the graph using the respective `add_node` and `add_edge` methods.

```python
G.add_node(1)
G.add_nodes_from([2, 3])

G.add_edge(1, 2)
G.add_edges_from([(1, 2), (1, 3)])
```

These topics are covered in greater detail in the following tutorial and in the Networkx documentation:

- [PyCon 2018: Network Analysis Made Simple, Part 1 Tutorial](https://www.youtube.com/watch?v=HkbMUrgzwMs)
- [Networkx Documentation Tutorial](https://networkx.github.io/documentation/stable/tutorial.html)

You are highly encouraged to watch the *Network Analysis Made Simple* tutorial and work through the examples in the *Networkx Documentation Tutorial* so that you gain a solid understanding of network composition and some practice creating graphs with the Networkx library.

You should also try to complete the exercises in the *Networkx Basics Notebook* (up until the Tests section) that accompanies the *Network Analysis Made Simple* tutorial:

- [Network Analysis Made Simple: Networkx Basics Notebook](https://github.com/ericmjl/Network-Analysis-Made-Simple/blob/master/2-networkx-basics-student.ipynb)

## Analyzing Networks

Once we have a built a graph, we can begin to analyze the properties of the network. Two of the basic things we would want to know about a graph is its *order* (number of nodes) and *size* (number of edges). We can calculate those with Networkx using the `order` or `number_of_nodes` methods to get the total nodes and the `size` or `number_of_edges` methods to get the total edges.

```python
G.order()
G.number_of_nodes()

G.size()
G.number_of_edges()
```

There are a few other important statistics that we would want to know about a graph that Networkx can compute for us. For example, each node in a graph has a *degree*, or the number of nodes you can reach from that node by traversing along the edges of the graph (jumping from one node to other connected nodes). The *average degree* of the graph tells you the average number of nodes that can be reached from a node in the graph and is a measure of how connected your graph is. We can retrieve the degree for each node in a graph by calling the `degree` method, so obtaining the average degree is just a matter of summing up all the degree values and then dividing by the number of nodes in the graph.

```python
sum(dict(G.degree()).values())/G.order()
```

A related metric is the *density* of the graph, which is calculated by dividing the average degree (computed above) by the number of nodes in the graph. This tells us the percentage of the graph that can be reached by the average node. It can be calculated easily by calling Networkx's `density` method.

```python
nx.density(G)
```

There are a couple other graph statistics you should know about: *diameter* and *average distance*. However, these statistics are only applicable when you have a *completely connected graph* or one where all nodes can reach all other nodes. When this is the case, the diameter of the graph tells you the what the longest path in the network is, or the maximum number of nodes you'll encounter getting between two nodes. Average distance is simply the average number of nodes you'll encounter getting between two nodes. Both can be computed as follows.

```python
nx.diameter(G)

nx.average_shortest_path_length(G)
```

### Node Centrality Metrics

In addition to calculating statistics that inform us about the properties of the graph as a whole, we can compute centrality metrics that tell us which nodes are most important and influential. Networkx comes with a variety of centrality metrics such as betweenness, closeness, eigenvector, degree, and pagerank. Each of these metrics calculate node importance slightly differently.

Betweenness centrality tells us which nodes in our network are likely pathways for information. Closeness centrality measures node reach or how fast information would spread from that node to other nodes. Degree centrality is a measure of popularity based on a node's degree. Eigenvector centrality measures related influence or who is closest to the most important nodes in the network. PageRank centrality is a variant of Eigenvector centrality that uses edges from other important nodes as a measure of a node's importance.

Each of these centrality measures can be obtained for each node in a graph as follows.

```python
betweenness = nx.betweenness_centrality(G, weight='edge')
closeness = nx.closeness_centrality(G, distance='edge')
eigenvector = nx.eigenvector_centrality_numpy(G)
degree = nx.degree_centrality(G)
pagerank = nx.pagerank(G)
```

## Building and Analyzing Graphs from Tabular Data

In order to perform network analysis, we need to have our data structured in a way that shows pairwise entity relationships. We mentioned earlier that networks are everywhere. If that is true, we should be able to create a network from just about any data set. So how do we convert an ordinary, tabular data set into graph format?

When data is structured in a tabular format, the rows typically represent either entities, transactions, or interactions and the columns usually represent attributes or features of whatever the rows represent. This gives us three potential things we can analyze from a network perspective:

- Entities
- Relationships
- Transactions or Interactions

### Rows Represent Transactions or Interactions

When rows represent transactions or interactions, they often have both parties of the transaction identified, so we can derive relationships directly from those. Examples of these types of data sets can include communication records, marketplace transactions, social media interactions, and other types of records where there are two parties. The relationships attributes for these records are the transaction attributes and they are sometimes directed (one party calls another, a seller sells something to a buyer, etc.), but they don't have to be.

When our rows represent transactions or interactions, we can transform our tabular data to a graph structure by aggregating the data, grouping by the fields containing the two parties, and counting the number of transactions or interactions.

The `us_womens_gymnastics.csv` data set is a good example of this type of data. The data set contains pairs of U.S. gymnasts that competed in the same Olympic games and events together. In other words, each row represents an interaction between the gymnasts. Use your Python skills, use Pandas to read and aggregate the data by the *Name_x* and *Name_y* fields and count the number of events in which they have an interaction. Once you have done this, sort descending by the number of pairwise interactions. Which pair of gymnasts have competed in the most events together?

Now that we have a data frame in this format, Networkx provides us with an easy way to turn it into a graph via the `from_pandas_edgelist` method.

```python
G = nx.from_pandas_edgelist(df, source, target)
```

Use this method to turn the data frame into a graph and then practice computing the graph statistics and centrality measures we covered in the previous section. Below are some questions to answer about this graph.

- How many gymnasts (nodes) are in the graph?
- How many edges are in the graph?
- What is the average degree?
- What is the density of the graph?
- Is this graph fully-connected? How do you know?
- What gymnast has the highest betweenness centrality?
- What gymnast has the highest Eigenvector centrality?
- What gymnast has the highest degree centrality?

### Rows Represent Entities

When we have a data set where the rows represent entities, we need to infer relationships based on attributes that different rows have in common. These relationships can be constructed based on entities belonging to the same group (same categorical variable values) or from having similar numeric variable values. These relationships are typically undirected.

The `us_mens_basketball.csv` data set is a good example of this. Each row represents an single basketball player's participation in a single event at a single Olympics.

Below is a `df_to_graph` function that creates pairwise relationships from data sets where rows represent entities. It creates a copy of the data set and then leverages the Pandas `merge` method to join the two copies together via whatever categorical column or list of columns you choose to define the edges of the network.

```python
def df_to_graph(df, entity, edge):
    df2 = df.copy()
    graph_df = pd.merge(df, df2, how='inner', on=edge)
    graph_df = graph_df.groupby([entity + '_x', entity + '_y']).count().reset_index()
    graph_df = graph_df[graph_df[entity + '_x'] != graph_df[entity + '_y']]
    
    if type(edge) == list:
        graph_df = graph_df[[entity + '_x', entity + '_y'] + edge]
    else:
        graph_df = graph_df[[entity + '_x', entity + '_y', edge]]
    
    return graph_df
```

Use the function above to structure the basketball data set as a data frame of pairwise connections. You can use the *Name* field to create your entities and the *Games* field to base your edges on. Once you have the data in this format, sort descending by the number of Olympic games the players have played in together. Which players have played together in the Olympics the most number of times?

Now that you have a data frame of pairwise connections, use the `from_pandas_edgelist` method to convert it into a graph. Compute the statistics of this graph and answer the following questions.

- How many basketball players (nodes) are in the graph?
- How many edges are in the graph?
- What is the average degree?
- What is the density of the graph?
- Is this graph fully-connected? How do you know?
- What player has the highest betweenness centrality?
- What player has the highest Eigenvector centrality?
- What player has the highest degree centrality?
- What are some notable differences between this graph and the gymnastics graph you analyzed earlier?

## Visualization of Network Data

In addition to analyzing our graph via graph statistics and node centrality metrics, we can also create visualizations that have the potential to be informative to our analysis. Networkx has a few different options for drawing graphs, but we will also be using the `nxviz` library as well.

The most basic way to create a network visualization is with Networkx's `draw` method.

```python
nx.draw(G)
```

However, just using this method usually produces some pretty ugly visualizations. To make it look nicer, try setting different values for the `node_size` and `node_color` parameters as well as modifying the default size of the plot. For example, the version below should make your graph look a bit nicer.

```python
plt.figure(figsize=(10,5))
nx.draw(G, node_size=20, node_color='cyan')
```

Graphs can be visualized via different layouts. The default one is spring layout, which is what you get when you call `nx.draw()`. You can also view the graph in a circular layout, a Kamada-Kawai force-directed layout, or via a [few other layouts](https://networkx.github.io/documentation/stable/reference/drawing.html). Below are examples for how to draw graphs with circular and Kamada-Kawai force-directed layouts via Networkx.

```python
nx.draw_circular(G, node_size=20, node_color='cyan')

nx.draw_kamada_kawai(G, node_size=20, node_color='cyan')
```

In addition to Networkx's drawing capabilities, the [nxviz](https://nxviz.readthedocs.io/en/stable/) library also has a few useful graph visualization layouts that you can apply to the graphs you construct with Networkx. The visualizations in the nxviz library are typically more visually appealing than the layouts in Networkx. In order to use it, we will need to pip install it.

```bash
$ pip install nxviz
```

Once you have it installed, you can generate network visualizations in the following layouts.

```python
#Circos Plots
from nxviz import CircosPlot

c = CircosPlot(G)
c.draw()
```

```python
#Matrix Plots
from nxviz import MatrixPlot

m = MatrixPlot(G)
m.draw()
```

```python
#Arc Plots
from nxviz import ArcPlot

a = ArcPlot(G)
a.draw()
```

In addition to the variety of layouts you can use to visualize networks, it's important to remember that you also have all the other types of visualizations you have learned about that you can leverage to visually analyze your network data.

### Bar Charts

For example, you can aggregate your data by entity, count the number of connections or the total number of interactions, sort them, filter to get just the top 20, and visualize it as a horizontal bar chart. By this point in the program, you should have all the tools in your arsenal to be able to do this. Try it for the basketball data set and see who are the top 20 players in the network that have played alongside the most number of other players.

### Scatter Plots

With the same aggregated data, you can also generate a scatter plot that shows the relationship that exists between the number of connections and the number of interactions in the data set. Try doing this for the gymnastics data set.

What other ways can you think of to visualize these data sets? Let your creativity run wild and show us what you've got!

## Deeper Analysis of Networks

### Subgraphs

Up until this point, we have been calculating statistics and visualizing entire networks, or at least what we thought were entire networks. In reality, both the gymnastics and the basketball data sets came from a larger Olympics data set that contains the athletes that participated in all Olympic events.

Therefore, what we have been analyzing are essentially subgraphs for the domains of gymnastics and basketball. Analyzing subgraphs is useful because full graphs have a tendency to get extremely large and complex. Subgraphs allow you to focus and really be able to examine the connections in a graph without getting overwhelmed with too much information. They also usually produce much more coherent network visualizations, whereas full graph visualization tends to suffer from the hairball effect.

One way to analyze a subgraph is the way we did it - by filtering a data set before converting it to a graph and then creating a Networkx graph object from the data. Another way to create a subgraph is to zoom in and look at an ego graph, which is a subgraph that focuses on one node and its connections in the network. Networkx has a handy `ego_graph` method that will create a ego graph from a node that we specify.

```python
ego = nx.ego_graph(G, 'NodeName', radius=1)
```

The `radius` parameter specifies how many degrees away from the node to create the ego graph. The default radius is 1, which means that only nodes that are directly connected to the node you specify will be included in the ego graph. If you were to set the radius to 2, it would include all nodes connected to your node's first degree connections, and so forth.

Which nodes does it make the most sense to analyze ego graphs for? A good place to start would be with the nodes that have the highest centrality metrics. Practice creating and visualizing ego graphs from both the gymnastics and basketball graphs we have created. When visualizing them, you can add a `with_labels=True` parameter to any of the Networkx `draw` methods to show athlete names next to each node.

### Community Detection

Another useful thing you can do with network data is community detection, where nodes in the graph are grouped together based on the other nodes they are connected to. One of the most straightforward ways to do this is using the `python-louvain` library, which you can pip install as follows.

```bash
$ pip install python-louvain
```

Once installed, you can import its `community` module and use the `best_partition` method to figure out which nodes in the graph to group together.

```python
import community

parts = community.best_partition(G)
```

This produces a dictionary containing the name of each node and which community it has been grouped into. You can extract the values of this dictionary and pass it to the `node_color` parameter of a `draw` method to color code the nodes in your network visualizations according to their community. Below is an example of how to do this.

```python
values = list(parts.values())
nx.draw_kamada_kawai(G, node_size=20, node_color=values)
```

### Hierarchical Graphs

Thus far, we have analyzed graphs where the nodes represented individual athletes and the edges represented Olympic games or specific events that they have competed in together. We didn't call attention to it at the time, but we essentially analyzed data at two different hierarchical levels, as there can be several events within a particular year's Olympic games.

We can continue going up the hierarchy if we wanted to, strip out the athletes as entities, and analyze the data at the Games level. To do this, we would need to designate the Games field as the entities and then use the athlete names as the edge criteria so that there would be an edge between two Olympic games if an athlete played in both of them.

You already have the tools in your toolbox to be able to do this, so give it a try using the basketball data set. Create a graph with Games as the entities and then produce a visualization showing the network.

- Are there any years connected that you weren't expecting? 
- Are there any years you were expecting to be connected that are not?
- Dig into the underlying data and see if you can find out which players are driving the connection between years.

## Bonus: More Complex Networks

Now that we have analyzed networks at multiple hierarchical levels individually, we can try to include nodes at different levels of the hierarchy *within the same graph*. For example, you can create a graph that matches basketball players to the Olympic games they participated in and then combine that graph with the player graph you created previously to form a new graph that has both games, players, and all the relationships between them captured.

To do this, you would select the *Games* and *Name* field from the original basketball data set and create a graph (H) using the `from_pandas_edgelist` method. You would then combine this new graph with your player graph (G) using the `nx.compose` method into a new graph (F) as follows.

```python
F = nx.compose(G,H)
```

You should now be able to generate sub/ego graphs from this new graph and run all the statistics and analytics we've covered.

## Resources

- [Wikipedia: Graph Theory](https://en.wikipedia.org/wiki/Graph_theory)
- [PyCon 2018: Network Analysis Made Simple, Part 1 Tutorial](https://www.youtube.com/watch?v=HkbMUrgzwMs)
- [PyCon 2018: Network Analysis Made Simple, Part 2 Tutorial](https://www.youtube.com/watch?v=MRCLwmYTVpc)
- [Network Analysis Made Simple Github Repo](https://github.com/ericmjl/Network-Analysis-Made-Simple)
- [Networkx Documentation](https://networkx.github.io/documentation/stable/)
- [Networkx Drawing](https://networkx.github.io/documentation/stable/reference/drawing.html)
- [nxviz Documentation](https://nxviz.readthedocs.io/en/stable/)
- [Python-Louvain Documentation](https://python-louvain.readthedocs.io/en/latest/api.html)
- [DataCamp Social Network Analysis Article](https://www.datacamp.com/community/tutorials/social-network-analysis-python)
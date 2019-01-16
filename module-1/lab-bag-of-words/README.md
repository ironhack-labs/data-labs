![Ironhack logo](https://i.imgur.com/1QgrNNw.png)

# Lab | Bag of Words

## Introduction

**Bag of words (BoW)** is an important technique in text mining and [information retrieval](https://en.wikipedia.org/wiki/Information_retrieval). BoW uses term-frequency vectors to represent the content of text documents which makes it possible to use mathematics and computer programs to analyze and compare text documents.

BoW contains the following information:

1. A dictionary of all the terms (words) in the text documents. The terms are normalized in terms of the letter case (e.g. `Ironhack` => `ironhack`), tense (e.g. `had` => `have`), singular form (e.g. `students` => `student`), etc.
1. The number of occurrences of each normalized term in each document.

For example, assume we have three text documents:

DOC 1: **Ironhack is cool.**

DOC 2: **I love Ironhack.**

DOC 3: **I am a student at Ironhack.**

The BoW of the above documents looks like below:

| TERM | DOC 1 | DOC 2 | Doc 3 |
|---|---|---|---|
| a | 0 | 0 | 1 |
| am | 0 | 0 | 1 |
| at | 0 | 0 | 1 |
| cool | 1 | 0 | 0 |
| i | 0 | 1 | 1 |
| ironhack | 1 | 1 | 1 |
| is | 1 | 0 | 0 |
| love | 0 | 1 | 0 |
| student | 0 | 0 | 1 |


The term-frequency array of each document in BoW can be considered a high-dimensional vector. Data scientists use these vectors to represent the content of the documents. For instance, DOC 1 is represented with `[0, 0, 0, 1, 0, 1, 1, 0, 0]`, DOC 2 is represented with `[0, 0, 0, 0, 1, 1, 0, 1, 0]`, and DOC 3 is represented with `[1, 1, 1, 0, 1, 1, 0, 0, 1]`. **Two documents are considered identical if their vector representations have close [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity).**

In real practice there are many additional techniques to improve the text mining accuracy such as using [stop words](https://en.wikipedia.org/wiki/Stop_words) (i.e. neglecting common words such as `a`, `I`, `to` that don't contribute much meaning), synonym list (e.g. consider `New York City` the same as `NYC` and `Big Apple`), and HTML tag removal if the data sources are webpages. In Module 3 you will learn how to use those advanced techniques for [natural language processing](https://en.wikipedia.org/wiki/Natural_language_processing), a component of text mining.

In real text mining projects data analysts use packages such as Scikit-Learn and NLTK, which you will learn in Module 3, to extract BoW from texts. In this exercise, however, we would like you to create BoW manually with Python. This is because by manually creating BoW you can better understand the concept and also practice the Python skills you have learned so far.

### Getting Started

In your Terminal, navigate into the directory `your-code` of this lab that contains `main.ipynb`, `bonus.ipynb`, `doc1.txt`, `doc2.txt`, and `doc3.txt`. Start Jupyter Notebook by executing `jupyter notebook`. A webpage should automatically open for you but in case not, go to [http://localhost:8888](http://localhost:8888). Then click the link `main.ipynb`. This is the workspace where you will work on this lab.

### Challenge Question

We need to create a BoW from a list of documents. The documents (`doc1.txt`, `doc2.txt`, and `doc3.txt`) can be found in the `your-code` directory of this exercise. You will read the content of each document into an array of strings named `corpus`.

:information_source: *What is a corpus (plural: corpora)? Read the reference in the Resources section.*

Your challenge is to use Python to generate the BoW of these documents. Your BoW should look like below:

```
bag_of_words = ['a', 'am', 'at', 'cool', 'i', 'ironhack', 'is', 'love', 'student']

term_freq = [
	[0, 0, 0, 1, 0, 1, 1, 0, 0],
 	[0, 0, 0, 0, 1, 1, 0, 1, 0],
 	[1, 1, 1, 0, 1, 1, 0, 0, 1],
]
```

### Bonus Question

Optimize your solution for the above question by removing stop words from the BoW. For your convenience, a list of stop words is defined below.

```
stop_words = ['all', 'six', 'less', 'being', 'indeed', 'over', 'move', 'anyway', 'fifty', 'four', 'not', 'own', 'through', 'yourselves', 'go', 'where', 'mill', 'only', 'find', 'before', 'one', 'whose', 'system', 'how', 'somewhere', 'with', 'thick', 'show', 'had', 'enough', 'should', 'to', 'must', 'whom', 'seeming', 'under', 'ours', 'has', 'might', 'thereafter', 'latterly', 'do', 'them', 'his', 'around', 'than', 'get', 'very', 'de', 'none', 'cannot', 'every', 'whether', 'they', 'front', 'during', 'thus', 'now', 'him', 'nor', 'name', 'several', 'hereafter', 'always', 'who', 'cry', 'whither', 'this', 'someone', 'either', 'each', 'become', 'thereupon', 'sometime', 'side', 'two', 'therein', 'twelve', 'because', 'often', 'ten', 'our', 'eg', 'some', 'back', 'up', 'namely', 'towards', 'are', 'further', 'beyond', 'ourselves', 'yet', 'out', 'even', 'will', 'what', 'still', 'for', 'bottom', 'mine', 'since', 'please', 'forty', 'per', 'its', 'everything', 'behind', 'un', 'above', 'between', 'it', 'neither', 'seemed', 'ever', 'across', 'she', 'somehow', 'be', 'we', 'full', 'never', 'sixty', 'however', 'here', 'otherwise', 'were', 'whereupon', 'nowhere', 'although', 'found', 'alone', 're', 'along', 'fifteen', 'by', 'both', 'about', 'last', 'would', 'anything', 'via', 'many', 'could', 'thence', 'put', 'against', 'keep', 'etc', 'amount', 'became', 'ltd', 'hence', 'onto', 'or', 'con', 'among', 'already', 'co', 'afterwards', 'formerly', 'within', 'seems', 'into', 'others', 'while', 'whatever', 'except', 'down', 'hers', 'everyone', 'done', 'least', 'another', 'whoever', 'moreover', 'couldnt', 'throughout', 'anyhow', 'yourself', 'three', 'from', 'her', 'few', 'together', 'top', 'there', 'due', 'been', 'next', 'anyone', 'eleven', 'much', 'call', 'therefore', 'interest', 'then', 'thru', 'themselves', 'hundred', 'was', 'sincere', 'empty', 'more', 'himself', 'elsewhere', 'mostly', 'on', 'fire', 'am', 'becoming', 'hereby', 'amongst', 'else', 'part', 'everywhere', 'too', 'herself', 'former', 'those', 'he', 'me', 'myself', 'made', 'twenty', 'these', 'bill', 'cant', 'us', 'until', 'besides', 'nevertheless', 'below', 'anywhere', 'nine', 'can', 'of', 'your', 'toward', 'my', 'something', 'and', 'whereafter', 'whenever', 'give', 'almost', 'wherever', 'is', 'describe', 'beforehand', 'herein', 'an', 'as', 'itself', 'at', 'have', 'in', 'seem', 'whence', 'ie', 'any', 'fill', 'again', 'hasnt', 'inc', 'thereby', 'thin', 'no', 'perhaps', 'latter', 'meanwhile', 'when', 'detail', 'same', 'wherein', 'beside', 'also', 'that', 'other', 'take', 'which', 'becomes', 'you', 'if', 'nobody', 'see', 'though', 'may', 'after', 'upon', 'most', 'hereupon', 'eight', 'but', 'serious', 'nothing', 'such', 'why', 'a', 'off', 'whereby', 'third', 'i', 'whole', 'noone', 'sometimes', 'well', 'amoungst', 'yours', 'their', 'rather', 'without', 'so', 'five', 'the', 'first', 'whereas', 'once']
```

With the stop words removed, your output should look like:

```
bag_of_words = [am', 'at', 'cool', ironhack', 'is', 'love', 'student']

term_freq = [
	[0, 0, 1, 1, 1, 0, 0],
 	[0, 0, 0, 1, 0, 1, 0],
 	[1, 1, 0, 1, 0, 0, 1]
]
```

## Deliverables

- REQUIRED: `main.ipynb` with your solution to the challenge question.
- OPITONAL: `bonus.ipynb` with your solution to the bonus question.

## Submission

Upon completion, add your deliverables to git. Then commit git and push your branch to the remote.

## Resources

* [Python Input and Output (how to read file content)](https://docs.python.org/3/tutorial/inputoutput.html)

* [How to Remove Punctuation in Python String](https://www.quora.com/How-do-I-remove-punctuation-from-a-Python-string)

* [Convert String to Lowercase in Python](https://docs.python.org/3/library/stdtypes.html#str.lower)

* [Break Python String into Array](https://docs.python.org/3/library/stdtypes.html#str.split)

* [What is Text Corpus?](https://en.wikipedia.org/wiki/Text_corpus)

* [A Gentle Introduction to the Bag-of-Words Model](https://machinelearningmastery.com/gentle-introduction-bag-words-model/)

If you are a research-type person, you will find [this article](http://rstb.royalsocietypublishing.org/content/royptb/366/1567/1101.full.pdf) interesting. Scientists used techniques based on BoW to calculate the frequency of words used cross 17 world languages. They found there is a consistent pattern in terms of the frequency of words being used in human languages. Some mad scientists even [want to use this technique to analyze dolphin language](http://grantome.com/grant/NSF/PHY-1530544) because they believe they can build corpora based on the sounds dolphins make, correlate the dolphin language corpora with human language corpora, and potentially understand what dolphins speak. :astonished: :astonished: :astonished:

Data analytics is now entering almost every discipline and profession. You will want to reflect on how you will apply your data analytics skills to the fields you are familiar with -- in creative ways. There are tons of fun secrets waiting for you to discover with data analytics.

## Additional Challenge for the Nerds

We will learn Scikit-Learn in Module 3 which has built in the BoW feature. Try to use Scikit-Learn to generate the BoW for this challenge and check whether the output is the same as yours. You will need to do some googling to find out how to use Scikit-Learn to generate BoW.

**Notes:**

* To install Scikit-Learn, use `pip install sklearn`. 

* Scikit-Learn removes stop words by default. You don't need to manually remove stop words.

* Scikit-Learn's output has slightly different format from the output example demonstrated above. It's ok, you don't need to convert the Scikit-Learn output.

The Scikit-Learn output will look like below:

```python
# BoW:
{u'love': 5, u'ironhack': 3, u'student': 6, u'is': 4, u'cool': 2, u'am': 0, u'at': 1}

# term_freq:
[[0 0 1 1 1 0 0]
 [0 0 0 1 0 1 0]
 [1 1 0 1 0 0 1]]
 ```


# Iris Data Set 

## About Ronald Fisher  

Touted as the greatest scientist of his time, Sir Ronald Fisher (1890-1962) was a British statistician and biologist who was known for his contributions to experimental design and population genetics. He is known as the father of modern statistics and experimental design.

He outlined Fisher's principle, the Fisherian runaway and sexy son hypothesis theories of sexual selection. His contributions to statistics include the maximum likelihood, fiducial inference, the derivation of various sampling distributions, founding principles of the design of experiments, and much more.

![Ronald Fisher](https://github.com/Katylub/Iris-Dataset-/blob/master/download.jpg)

## About Iris Dataset 

The Iris flower data is a multivariate data set introduced by Fisher in his 1936 paper. The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis . It is sometimes called Anderson’s Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species. Two of the three species were collected in the Gaspé Peninsula “all from the same pasture, and picked on the same day and measured at the same time by the same person with the same apparatus”.

The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor). 

![Image of Iris](https://github.com/Katylub/Iris-Dataset-/blob/master/iris.jpg)

For each example were measured four features:  

1. sepal length in cm
2. sepal width in cm
3. petal length in cm
4. petal width in cm
 
## Based on the combination of these four features and the species Fisher developed a linear discriminant model to distinguish the species from each other. ##

![Image of Iris sepal and width](https://github.com/Katylub/Iris-Dataset-/blob/master/Others/Sepal%20and%20petal.png)

## Iris Data Set: 

Summary of the steps to evaluate the information using Python, made sure you have the program downloaded. 
Please see [here](https://github.com/Katylub/Iris-Dataset-/blob/master/Iris.py) the Python code used for this research

## Import libraries
The libraries will help to analyse the data in a more efficient way.  

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

## Load the dataset
The data can be loaded from a CSV file that you can see in this [link](https://github.com/Katylub/Iris-Dataset-/blob/master/IrisDataset.csv): 

```python
f = pd.read_csv('IrisDataset.csv')
```

## Check Dimension Dataset
As mentioned, the dataset contains a set of 150 records under five attributes

```python
print("The shape of dataset is:", (f.shape))
```

![Shape Data set](https://github.com/Katylub/Iris-Dataset-/blob/master/Shape%20of%20dataset.JPG)


## Evaluate the data
We can see how the attributes are presented by petal length, petal width, sepal length, sepal width and species.

```python
print (f.head())
```

 ![We can see each column looks like this:](https://github.com/Katylub/Iris-Dataset-/blob/master/Dataset%20Columns.JPG)


## Summary of each attribute 
We can see the count, min, max, standard and percentiles. Also that all the values has a similar range between 0 and 8.

```python
print (f.describe())
```

![Attribute Summary](https://github.com/Katylub/Iris-Dataset-/blob/master/Attribute%20Summary.JPG)

## Species Distribution
We can see that each specie has the same number of instances (50 or 33% of the dataset) and all of them integer.

```python
print(f.groupby('species').size())
```

![Species](https://github.com/Katylub/Iris-Dataset-/blob/master/Species.JPG)

## Data view - Plot each individual variable
Gives us a much clearer idea of the distribution of the attributes

```python
f.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
```

![Plot Individual Variable](https://github.com/Katylub/Iris-Dataset-/blob/master/Plot%20Individual%20variable.png)

## Histogram of each individual variable
Graphical distribution of attributes

```python
f.hist()
plt.show()
```

![Histogram](https://github.com/Katylub/Iris-Dataset-/blob/master/Histogram.png)

## Boxplot
We can compare distribution of the attributes by species 

```python
f.boxplot(by='species')
plt.show()
```

![Boxplot](https://github.com/Katylub/Iris-Dataset-/blob/master/Boxplot%20by%20species.png)

## Scatter Matrix
We can look at the interactions between the variables

```python
pd.plotting.scatter_matrix(f)
plt.show()
```

![Scatter](https://github.com/Katylub/Iris-Dataset-/blob/master/Scatter%20matrix.png)

## Violinplot 
Visual representation of distribution of data and density

```python
sns.violinplot(data=df,x='Species',y='PetalLengthCm')
plt.show()
```

![Violinplot](https://github.com/Katylub/Iris-Dataset-/blob/master/Violinplot.png)


## Pairplot
Interaction between attibutes by species across multiple dimensions

```python
sns.pairplot(df,hue="Species")
plt.show()
```

![Pairplot](https://github.com/Katylub/Iris-Dataset-/blob/master/Pairplot.png)


## Machine Learning - Scikit
Machine learning is about learning some properties of a data set and then testing those properties against another data set. A common practice in machine learning is to evaluate an algorithm by splitting a data set into two. We call one of those sets the training set, on which we learn some properties; we call the other set the testing set, on which we test the learned properties.

**Scikit** is a open source tool for data mining and data analysis built in Numpy, Scipy and Matplotlib and comes with the Iris dataset.

## Superviced Learning
In Supervised Learning, we have a dataset consisting of both features and labels. The task is to construct an estimator which is able to predict the label of an object given the set of features. A relatively simple example is predicting the species of iris given a set of measurements of its flower. 

K nearest neighbors (kNN) is one of the simplest learning strategies: given a new, unknown observation, look up in your reference database which ones have the closest features and assign the predominant class. As example see belos one iris classification problem that output the specie.

```python
from sklearn import neighbors, datasets
iris = datasets.load_iris()
X, y = iris.data, iris.target
knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
# What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?
print(iris.target_names[knn.predict([[3, 5, 4, 2]])])
```

In this case the output will be Virginica

## Plot 2D views of the iris dataset
we can visualize two of the dimensions at a time using a scatter plot, in this case we can visualize that Iris Setosa flower is easier to separate from Versicolor and Virginica

```python
from sklearn import neighbors, datasets
iris = datasets.load_iris()
X, y = iris.data, iris.target
knn = neighbors.KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
# What kind of iris has 3cm x 5cm sepal and 4cm x 2cm petal?
print(iris.target_names[knn.predict([[3, 5, 4, 2]])])
```
![Plot 2D](https://github.com/Katylub/Iris-Dataset-/blob/master/Plot%202D.png)


## References:

http://www.popflock.com/learn?s=Ronald_Fisher
https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python
https://en.wikipedia.org/wiki/Iris_flower_data_set
https://study.com/academy/lesson/sir-ronald-fisher-biography-contributions-to-statistics.html
https://archive.ics.uci.edu/ml/datasets/iris
https://datahub.io/machine-learning/iris#readme
https://matematics.wordpress.com/2018/05/23/sir-ronald-aylmer-fisher/
https://scikit-learn.org/stable/tutorial/basic/tutorial.html#loading-an-example-dataset
https://medium.com/@jebaseelanravi96/machine-learning-iris-classification-33aa18a4a983
http://scipy-lectures.org/packages/scikit-learn/index.html


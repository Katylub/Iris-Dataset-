
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

![Image of Iris sepal and width](https://github.com/Katylub/Iris-Dataset-/blob/master/Sepal%20and%20petal.png)

## Iris Data Set: 

Process and data by steps:

1. Import libraries 

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
```

2. Load the dataset from the CSV file that you can see in this [link](https://github.com/Katylub/Iris-Dataset-/blob/master/IrisDataset.csv): 

```python
f = pd.read_csv('IrisDataset.csv')
```

3. Check Dimension Dataset: As mentioned, the dataset contains a set of 150 records under five attributes

```python
print("The shape of dataset is:", (f.shape))
```

![Shape Data set](https://github.com/Katylub/Iris-Dataset-/blob/master/Shape%20of%20dataset.JPG)


4. Test if the document has the right data: We can see how the data is presented and the attribues - petal length, petal width, sepal length, sepal width and species.

```python
print (f.head())
```

 ![We can see each column looks like this:](https://github.com/Katylub/Iris-Dataset-/blob/master/Dataset%20Columns.JPG)


5. Summary of each attribute : We can see the count, min, max, standard and percentiles. Also that all the values has a similar range between 0 and 8.

```python
print (f.describe())
```

![Attribute Summary](https://github.com/Katylub/Iris-Dataset-/blob/master/Attribute%20Summary.JPG)

6. Species Distribution: We can see that each specie has the same number of instances (50 or 33% of the dataset) and all of them integer.

```python
print(f.groupby('species').size())
```

![Species](https://github.com/Katylub/Iris-Dataset-/blob/master/Species.JPG)

7. Plot each individual variable: Gives us a much clearer idea of the distribution of the attributes

```python
f.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
plt.show()
```

![Plot Individual Variable](https://github.com/Katylub/Iris-Dataset-/blob/master/Plot%20Individual%20variable.png)

7. Histogram of each individual variable

```python
f.hist()
plt.show()
```

![Histogram](https://github.com/Katylub/Iris-Dataset-/blob/master/Histogram.png)

8. Boxplot: We can compare distribution of the attributes by species 

```python
f.boxplot(by='species')
plt.show()
```

![Boxplot](https://github.com/Katylub/Iris-Dataset-/blob/master/Boxplot%20by%20species.png)

9. Scatter Matrix: we can look at the interactions between the variables

```python
pd.plotting.scatter_matrix(f)
plt.show()
```

![Scatter](https://github.com/Katylub/Iris-Dataset-/blob/master/Scatter%20matrix.png)


References:

https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python


About Ronald Fisher:
http://www.popflock.com/learn?s=Ronald_Fisher

About Iris Dataset
https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
https://en.wikipedia.org/wiki/Iris_flower_data_set
https://study.com/academy/lesson/sir-ronald-fisher-biography-contributions-to-statistics.html
https://archive.ics.uci.edu/ml/datasets/iris
https://datahub.io/machine-learning/iris#readme
https://matematics.wordpress.com/2018/05/23/sir-ronald-aylmer-fisher/

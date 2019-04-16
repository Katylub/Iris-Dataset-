
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

In order to work with the documents we can:

1. Import Dataset CSV file that you can find in this [link](https://github.com/Katylub/Iris-Dataset-/blob/master/IrisDataset.csv)

2. Load the dataset from the CSV file: 

```python
f = pd.read_csv('IrisDataset.csv')
```

3. Test if the document has the right data: 

```python
print (f.head())
```

 ![We can see each column looks like this:](https://github.com/Katylub/Iris-Dataset-/blob/master/Dataset%20Columns.JPG)


4. Check Dimension Dataset: 
```python
print("The shape of dataset is:", (f.shape))
```

![Shape Data set](https://github.com/Katylub/Iris-Dataset-/blob/master/Shape%20of%20dataset.JPG)

As mentioned, the dataset contains a set of 150 records under five attributes - petal length, petal width, sepal length, sepal width and species.

5. Summary of each attribute : 

```python
print (f.describe())
```

![Attribute Summary](https://github.com/Katylub/Iris-Dataset-/blob/master/Attribute%20Summary.JPG)


You can evaluate what is in the document:

1. Allow to see the for quickly testing if your object has the right type of data in it.

Each colum looks like this: (picture)
https://machinelearningmastery.com/machine-learning-in-python-step-by-step/
https://www.kaggle.com/gopaltirupur/iris-data-analysis-and-machine-learning-python
Average Sepal length -
Average Sepal width
Average Petal length
Average Petal width
Standard deviation -



References:


About Ronald Fisher:
http://www.popflock.com/learn?s=Ronald_Fisher

About Iris Dataset
https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342
https://en.wikipedia.org/wiki/Iris_flower_data_set
https://study.com/academy/lesson/sir-ronald-fisher-biography-contributions-to-statistics.html

https://archive.ics.uci.edu/ml/datasets/iris


https://datahub.io/machine-learning/iris#readme
https://matematics.wordpress.com/2018/05/23/sir-ronald-aylmer-fisher/

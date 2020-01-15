import os
import __future__
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
sns.set_style('whitegrid')
for dirname, _, filenames in os.walk('../Desktop/kaggle/titanic'):
    for filename in filenames:
        print(os.path.join(dirname, filename))
titanic_train = pd.read_csv('~/Desktop/kaggle/titanic/train.csv')
#print("Starting...")
#print(titanic_train.head(1))
#print(titanic_train.describe())
#print(titanic_train.nunique())
'''print(pd.DataFrame({'Integer': ['Survived','Pclass','SibSp, Parch','-'],
              'Float': ['-','-','-','Age, Fare'],
              'Object': ['Sex, Name, Ticket, Cabin, Embarked','-','-','-']},
              index = ['Nominal','Ordinal','Discrete','Continuous']))'''


def count_n_plot(df, col_name, countsplit=None, bar=False, barsplit=None):
    """
    Creates countplots and barplots of the specified feature
    (with options to split the columns) and generates the
    corresponding table of counts and percentages.

    Parameters
    ----------
    df : DataFrame
        Dataset for plotting.
    col_name : string
        Name of column/feature in "data".
    countsplit : string
        Use countsplit to specify the "hue" argument of the countplot.
    bar : Boolean
        If True, a barplot of the column col_name is created, showing
        the fraction of survivors on the y-axis.
    barsplit: string
        Use barsplit to specify the "hue" argument of the barplot.
    """

    if (countsplit != None) & bar & (barsplit != None):
        col_count1 = df[[col_name]].groupby(by=col_name).size()
        col_perc1 = col_count1.apply(lambda x: x / sum(col_count1) * 100).round(1)
        tcount1 = pd.DataFrame({'Count': col_count1, 'Percentage': col_perc1})

        col_count2 = df[[col_name, countsplit]].groupby(by=[col_name, countsplit]).size()
        col_perc2 = col_count2.apply(lambda x: x / sum(col_count2) * 100).round(1)
        tcount2 = pd.DataFrame({'Count': col_count2, 'Percentage': col_perc2})
        print(tcount1, tcount2)

        figc, axc = plt.subplots(1, 2, figsize=(10, 4))
        sns.countplot(data=df, x=col_name, hue=None, ax=axc[0])
        sns.countplot(data=df, x=col_name, hue=countsplit, ax=axc[1])

        figb, axb = plt.subplots(1, 2, figsize=(10, 4))
        sns.barplot(data=df, x=col_name, y='Survived', hue=None, ax=axb[0])
        sns.barplot(data=df, x=col_name, y='Survived', hue=barsplit, ax=axb[1])

    elif (countsplit != None) & bar:
        col_count1 = df[[col_name]].groupby(by=col_name).size()
        col_perc1 = col_count1.apply(lambda x: x / sum(col_count1) * 100).round(1)
        tcount1 = pd.DataFrame({'Count': col_count1, 'Percentage': col_perc1})

        col_count2 = df[[col_name, countsplit]].groupby(by=[col_name, countsplit]).size()
        col_perc2 = col_count2.apply(lambda x: x / sum(col_count2) * 100).round(1)
        tcount2 = pd.DataFrame({'Count': col_count2, 'Percentage': col_perc2})
        print(tcount1, tcount2)

        fig, axes = plt.subplots(1, 3, figsize=(15, 4))
        sns.countplot(data=df, x=col_name, hue=None, ax=axes[0])
        sns.countplot(data=df, x=col_name, hue=countsplit, ax=axes[1])
        sns.barplot(data=df, x=col_name, y='Survived', hue=None, ax=axes[2])

    elif countsplit != None:
        col_count1 = df[[col_name]].groupby(by=col_name).size()
        col_perc1 = col_count1.apply(lambda x: x / sum(col_count1) * 100).round(1)
        tcount1 = pd.DataFrame({'Count': col_count1, 'Percentage': col_perc1})

        col_count2 = df[[col_name, countsplit]].groupby(by=[col_name, countsplit]).size()
        col_perc2 = col_count2.apply(lambda x: x / sum(col_count2) * 100).round(1)
        tcount2 = pd.DataFrame({'Count': col_count2, 'Percentage': col_perc2})
        print(tcount1, tcount2)

        fig, axes = plt.subplots(1, 2, figsize=(10, 4))
        sns.countplot(data=df, x=col_name, hue=None, ax=axes[0])
        sns.countplot(data=df, x=col_name, hue=countsplit, ax=axes[1])

    else:
        col_count = df[[col_name]].groupby(by=col_name).size()
        col_perc = col_count.apply(lambda x: x / sum(col_count) * 100).round(1)
        tcount1 = pd.DataFrame({'Count': col_count, 'Percentage': col_perc})
        print(tcount1)

        sns.countplot(data=df, x=col_name)


#count_n_plot(df = titanic_train, col_name='Survived')
#count_n_plot(df = titanic_train, col_name = 'Pclass', countsplit = 'Survived')
#count_n_plot(df = titanic_train, col_name = 'Pclass', countsplit = 'Survived', bar = True)
#count_n_plot(df = titanic_train, col_name = 'Sex', countsplit = 'Survived', bar = True)
#count_n_plot(df = titanic_train, col_name = 'Sex', countsplit = 'Pclass', bar = True, barsplit = 'Pclass')
#count_n_plot(df = titanic_train, col_name = 'Embarked', countsplit = 'Survived', bar = True)
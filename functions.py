import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def lowercase_cols(df):
    '''Changes the column names of a DataFrame to follow the PE8 (snake_case).
	
	Input: DataFrame
	Output: DataFrame'''
	
    df2 = df.copy()
    
    cols = df2.columns
    new_cols = []
    
    for col in cols:
        new_col = ""
        for letter in col:
            if letter == " ":
                letter = "_"
                new_col += letter
            else:
                new_col += letter
        new_cols.append(new_col.lower())
    df2.columns = new_cols
    
    return df2

def remove_na(df, threshold=25):
    
    df2 = df.copy()
    
    cols = df2.columns
    rows = df.shape[0]
    
    for col in cols:
        na = df2[col].isna().sum()
        if na > (threshold*rows/100):
            df2 = df2.drop([col], axis=1)
        else: 
            df2 = df2[df2[col].isna()==False]
    
    return df2

def starless(x):
    
    x = x.replace(' ★', "")
    x = x.replace('★', "")
    x = int(x)

    return x

def show_me_the_money(x):

    x = x.replace('€', "")
        
    if "." in x:
        split = x.split(".")
        x = split[0] + split[1]
        x = x.replace("M", "00000")
        x = x.replace("K", "00")

    else:       
        x = x.replace("M", "000000")
        x = x.replace("K", "000")
            
    x = int(x)
    
    return x

def inches_to_cm(x):
    
    x = x.replace('"', "")
    split = x.split("'")
    split[0] = float(split[0])
    split[1] = float(split[1])
    split[0] = split[0]*30.48
    split[1] = split[1]*2.54
    x = split[0]+split[1]
    
    return x

def never_positive(df):
    
    cols = df.columns
    
    for col in cols:
        new_col = []
        for value in df[col]:
            
            if "+" in value:
                split = value.split("+")
                split[0] = int(split[0])
                split[1] = int(split[1])
                value = split[0]+split[1]
            else: value = int(value)
            
            new_col.append(value)
        df[col] = new_col
        
    return df

def hist_maker(df):
    '''Returns histplots in a single fig for each column of a given DataFrame
    
    Input: DataFrame
    Output: Histplots of all the columns'''
    
    cols = list(df.columns)
    x = len(cols)
    fig, ax = plt.subplots(1,x, figsize=(20,10))

    for col in cols:
        y = cols.index(col)
        sns.histplot(data=df, x=col, ax = ax[y])
        ax[y].set_title(col)
        
    return

def box_maker(df):
    '''Returns boxplots in a single fig for each column of a given DataFrame
    
    Input: DataFrame
    Output: Boxplot of all the columns'''
	
    cols = list(df.columns)
    x = len(cols)
    fig, ax = plt.subplots(1,x, figsize=(20,10))
    
    for col in cols:
        y = cols.index(col)
        sns.boxplot(data=df, y=col, ax = ax[y])
        ax[y].set_title(col)
        
    return

def kdeplot_maker(df):
    '''Returns KDEplots in a single fig for each column of a given DataFrame
    
    Input: DataFrame
    Output: KDEplots of all the columns'''
	
    cols = list(df.columns)
    x = len(cols)
    fig, ax = plt.subplots(1,x, figsize=(20,10))
    
    for col in cols:
        y = cols.index(col)
        sns.kdeplot(data=df, x=col, ax = ax[y])
        ax[y].set_title(col)
        
    return

def count_maker(df, figsize_x = 20, figsize_y = 10):
	'''Returns countplots in a single fig for each column of a given DataFrame
    
    Input: DataFrame
    Output: Countplots of all the columns'''

	cols = list(df.columns)
	fig_cols = len(cols)
	fig, ax = plt.subplots(1, fig_cols, figsize = (figsize_x, figsize_y))
        
	for col in cols:
		sns.countplot(data=df, x=col, ax = ax[cols.index(col)])
		ax[cols.index(col)].set_title(col)

	return
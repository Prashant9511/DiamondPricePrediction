# DiamondPricePredictionProject

## Preview

In this project we will be predicting the bid price for the diamonds from a dataset that was part of the Udacity Bertelsmann Data Track Final Project.

## Problem Statement

You are hired by a company XYZ. You are provided with the dataset containing the prices and other attributes of an diamond. The company is earning different profits on different prize slots. You have to help the company in predicting the price for the stone on the basis of the details given in the dataset so it can distinguish between higher profitable stones and lower profitable stones so as to have a better profit share. You can refer the link for domain knowledge : 
[https://www.americangemsociety.org/buying-diamonds-with-confidence/ags-diamond-grading-system/](https://www.americangemsociety.org/buying-diamonds-with-confidence/ags-diamond-grading-system/)

### Introduction About the Data :

**The dataset** The goal is to predict `price` of given diamond (Regression Analysis).

There are 10 independent variables (including `id`):

* `id` : unique identifier of each diamond
* `carat` : Carat (ct.) refers to the unique unit of weight measurement used exclusively to weigh gemstones and diamonds.
* `cut` : Quality of Diamond Cut
* `color` : Color of Diamond
* `clarity` : Diamond clarity is a measure of the purity and rarity of the stone, graded by the visibility of these characteristics under 10-power magnification.
* `depth` : The depth of diamond is its height (in millimeters) measured from the culet (bottom tip) to the table (flat, top surface)
* `table` : A diamond's table is the facet which can be seen when the stone is viewed face up.
* `x` : Diamond X dimension
* `y` : Diamond Y dimension
* `x` : Diamond Z dimension

Target variable:
* `price`: Price of the given Diamond.

## How to run this project in your local host from this repository?

I have created files with numbers from 1 to 4 and you can follow along with me easily.

## Step-1: fork and clone this repo in your VS Code 

### Step-2: Then set up a virtual environment specific for this project, ask chat GPT how to? or run in cmd terminal

Conda command: conda create -p venv python==3.8

## Step-3: after creation of env, run setup.py file in cmd terminal

conda command:  python setup.py install

## Step-4: Now if any error comes run requirements.txt file manally

conda command:  pip install -r requirements.txt

## Step-5:  After installation, run app.py file

conda command: python app.py

## Step-6:  open your local browser and run local host 

http://localhost:5000   --1st
http://localhost:5000/train  --2nd
http://localhost:5000/predict  --3rd

(Wait for every process to be done)

## Step_7: We have test file in prediction_artifacts folder takes it and upload and it will download predicted csv

## Hoooorrrreeeeyyy !!! We done it !!
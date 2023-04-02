### Breast Cancer detection
This repository contains code for detecting breast cancer using machine learning. The dataset used is the Breast Cancer Wisconsin 
(Diagnostic) Data Set which can be downloaded from https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data.
The dataset contains information about breast cancer tumors such as radius, texture,
perimeter, area, smoothness, compactness, concavity, symmetry, and fractal dimension. The goal is to predict whether a tumor is benign or malignant.
#### About dataset
The Breast Cancer Wisconsin (Diagnostic) Data Set contains 33 columns and 569 rows. Each row represents a tumor, and each column represents a different feature of the tumor. The features are as follows:
* ID number
* Diagnosis (M = malignant, B = benign)
* Radius (mean of distances from center to points on the perimeter)
* Texture (standard deviation of gray-scale values)
* Perimeter
* Area
* Smoothness (local variation in radius lengths)
* Compactness (perimeter^2 / area - 1.0)
* Concavity (severity of concave portions of the contour)
* Concave points (number of concave portions of the contour)
* Symmetry
* Fractal dimension ("coastline approximation" - 1)

#### Machine Learning Models
Six machine learning models were used in this project: logistic regression, decision tree, 
naive Bayes, k-nearest neighbors (KNN), random forest, and support vector machine (SVM). 
These models were trained on the dataset to predict whether a tumor is benign or malignant. The best performing model was SVM with an accuracy of 97% on the test data.

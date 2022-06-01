# Richter-s-Predictor
Kyongmin's Capstone Project

Data Science Student 

[LinkedIn](https://www.linkedin.com/in/kyongminso/) | [GitHub](https://github.com/kyongminso) | [Email](mailto:kyongminso@gmail.com)

<img src= "Images/nepal-quake-map-data.jpeg">

# Business Understanding
In April 2015, an earthquake (also known as the **Gorkha Earthquake**) hit central Nepal with a magnitude of 7.8. It killed an estimate of 9 thousand people and injured more than 20 thousand people. It was the worst natural disaster to hit Nepal since the 1930's. 

This earthquake flattened out countless villages and communities throughtout Nepal. Nepal is already one of the poorest Asian countries with a GDP of about $20 billion dollars and had no abilities to reconstruct themselves needing to rely on foreign aid to get back up on their feet. This country was absolutely not prepared for this catastrophe and they paid massively for their consequences for not being prepared.


Something that intrigued me was that that 2 years prior to the earthquake in 2013, a seismologist named Vinod Kumar Gaur was interviewed and he was quoted saying: "Calculations show that there is sufficient accumulated energy, now to produce an 8 magnitude earthquake. I cannot say when. It may not happen tomorrow, but it could possibly happen sometime this century, or wait longer to produce a much larger one." 

People were aware of the earthquake but they were confident that the earthquake wouldn't happen for a long time and the people of Nepal eventually paid the price for it. Part of the reason why I was so interested in doing this is to see what the buildings were made out of and see if there are any connections to the damage of the building and the material used to construct the buildings. Hopefully with my studies,I can figure out what building materials are detrimental in earthquakes, and make sure that any other buildings made of the same material are documented and are best restructured so that the damage when an earthquake happens the aftermath will not be that detrimental.

[Source](https://en.wikipedia.org/wiki/April_2015_Nepal_earthquake)

# Overview 
This model is going to predict the damage of the buildings based off what the features of the building are. 

#### **Modeling** 
------------------------
The models that I will be running for this project are: 

- **Logistic Regression (1st Simple Model)** 
- **Random Forests**
- **XG-Boost** 
- **K-Nearest Neighbors**


I am using these models because these are the basic classification models I can use. These are good for binary classification models, but these can also be used for multi-class classification. These models are used on the trained dataset and are filled with features describing the building.


# Data
All of my data was obtained through this website [Driven Data](https://www.drivendata.org/competitions/57/nepal-earthquake/) but you will need an account to access the information. I will not use all the features and if I start dropping anything, I will explain why I dropped certain features.


Our dataset is filled with features describing each buildings with columns such as: 
- **age**
- **area_percentage**
- **has_superstructure_rc_engineered**
- and more.

Our target is the **damage_grade** and it is based off of 3 levels. Each building is associated with one of these 3 answers.
- 1 = Least Damage 
- 2 = Middle Damage 
- 3 = Heavy Damage 


As for my other features,as you move on through the notebook, all of my features will be explained and dropped as you move on. 


**Something to know**

This data is based off of damages from an earthquake that was registered at a 7.8 ~ 8.0 earthquake and the Richter Scale max is 8.8 or 8.9 (depending on who you ask). My model will predict off of earthquakes that are on the more severe and dangerous side of the scale so my findings will be based off of earthquakes that are stronger than 7.0. 

**Scoring Metrics**

I am predicting the level of damage from a scale of 1 to 3. The level of damage is an ordinal so that means the order matters. This can be viewed as a classification or an ordinal regression problem.

We will be using the the F1 score which balances the precision and recall of a classifier. Normally we use the F1 score for binary situations but since we have three labels we are dealing with, we will be using the **micro** averaged F1 score. Micro F1 is used to assess the quality of multi-label binary problems. It basically measures the F1-score of the aggregated contributions of all classes. 

Just a refresher: 
- Precision : Out of all of the positive predictions, how many are really positive?
- Recall : Of all the true positive cases, how many were predicted positive? 
- F1 Score: The harmonic mean between the Precision and the Recall 

Basically, **micro F1 score** performed by first calculating the sum of all true positives, false positives, and false negatives over all the labels. Then I compute the micro-precision and micro-recall from the sums.Finally we compute the harmonic mean to get the micro F1-score.

I will also find the **macro** F1 score too because why not? **macro** scores are just gathering all the f1 scores per class and dividing it by the number of classes.

# Results
My best model was my **Random Forest** as it gave me a micro-F1 score of almost **72%**.



<img src = 'Images/final_confusion_matrix.png'>

My confusion matrix had some issues with predicting the damage 1 class, but it was phephenomenal at predicting the majority class of damage 2. 
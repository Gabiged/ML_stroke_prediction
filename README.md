# ML_stroke_prediction
##Stroke Prediction <br>
The task for this work is to analyse the Stroke Prediction dataset. The task is to create a machine learning model, which could predict if the patient is likely to get a stroke - being able to determine which patients have high stroke risk will allow your doctors to advise them and their families on how to act in case of an emergency. I will apply what I have learned about Machine Learning to complete this task.

**Requirements**

* Perform exploratory data analysis:
- create statistical summaries and charts,
- test for anomalies,
- check for correlations and other relations between variables, and other EDA elements.
* Perform statistical inference:

- define the target population,
- form multiple statistical hypotheses and constructing confidence intervals,
- set the significance levels,
- conduct z or t-tests for these hypotheses.
* Apply various machine learning models to predict the "stroke" column using all other features:

- include hyperparameter tuning,
- include model ensembling,
- include the analysis of model selection, and other methods.
* Deploy the machine learning model (in a container (on your computer or on a server), do a serverless deployment on the cloud, or on the browser as a web app)

### Conclusions:
* This dataset is used to predict whether a patient is likely to get stroke based on the input parameters like gender, age, various diseases, and smoking status etc.;
* Dataset has 5110 entries and 12 features;
* The age range in dataset: 0.08 - 82.0 years;
* In relation to stroke possibility, the biggest risk are people age from 71 to 90. But in general risk rises from 51 (19.3% were diagnosed positively):
* In total there are 2994 females and 2115. Data shows that women are more likely to have a stroke (~57%);
* Ever_married people tend to have stroke far more often then single people;
* Most stroke sufferers work in the private sector and a higher proportion are women (30.5%);
* Most patients live in urban areas (female group 30.9%);
* The female group of stroke patients has never smoked (25.3%), the second group of patients admits to having smoked in the past, but almost 18% of both men and women are not known to smoke;
* Both genders admit to having had no blood pressure problems;
* Both genders admit to having no heart disease.
Hypothesis: glucose level has impact on patients having stroke;
Alternative: There is no meaningful difference in glucose level effect to get stroke In both the "Stroke positive" and the "Stroke negative" groups, the Shapiro-Wilk test shows that data in 'average_glucose_level' is not normally distributed Stroke patients: 95.0% Confidence Interval for avg_glucose_level mean: [124.85, 140.24] mg/dL Healthy patients: 95.0% Confidence Interval for avg_glucose_level mean: [103.56, 106.03] mg/dL

Processing dataset for stroke prediction revealed that data is highly imbalanced therefore the used ensembled model showed overall accuracy of 88%, and f1 score 32% accuracy.

To run app.py please open terminal and run command: streamlit run app.py

--

# 🧠 Marketing Campaign Conversion Prediction

## 📋 Overview
This project was developed as part of a data science roleplay scenario for **Sports Wear Group**, a leading retail company in the region. The goal was to analyze the impact of promotional campaigns and build a machine learning model that can predict whether a customer will convert (make a purchase) based on product and campaign attributes.

---

## 🎯 Business Objective
- **Marketing Team**: Improve targeting efficiency and reduce wasted spending on ineffective campaigns.
- **Management Team**: Use advanced analytics to increase overall sales and campaign ROI.
- **Data Science Team**: Evaluate the methodology and model details used in prediction.

---

## 🧪 Dataset Description
The dataset includes:
- Product information (e.g. price, category, gender, style, colors)
- Customer-level offer exposure
- Campaign attributes (promo1, promo2)
- Label indicating whether the customer purchased the product

Key features:
- `label` → Target variable (0 = no purchase, 1 = purchase)
- `ratio` → Discount ratio
- `promo1`, `promo2` → Indicators for promotional exposure

---

## 🔍 Solution Approach

### ✔️ Preprocessing
- **Outliers**: Handled using percentile thresholds and median imputation to preserve data integrity.
- **Skewness**: Applied Box-Cox and Yeo-Johnson transformations to address data skewness.
- **High-cardinality Features**: Encoded categorical features like `article` using Target Encoding to prevent model overfitting.
- **Feature Scaling**: Used MinMaxScaler to normalize numeric features to ensure they are on the same scale.
- **Pipeline**: Created a pipeline to automate the preprocessing steps, ensuring no data leakage during cross-validation.

### 📊 EDA (Exploratory Data Analysis)
- Investigated the imbalance in the `label` variable, where most values are `0` (no purchase).
- Visualized relationships between pricing, promotional activities, and conversions.
- Analyzed feature importance and correlations.

### 🧠 Model Training & Fine-Tuning
To improve model accuracy and reduce overfitting, the following models were evaluated:
- Logistic Regression
- Random Forest
- Decision Tree
- XGBoost
- LightGBM

Each model was fine-tuned using **GridSearchCV** and **RandomizedSearchCV** to find the best hyperparameters. 

Cross-validation was applied to ensure robust evaluation and prevent overfitting. We focused on:
- **Accuracy**
- **Precision / Recall / F1 (per class)**
- **ROC-AUC**
- **Confusion Matrix**

### 🔧 Model Improvement
- **Cross-validation**: Ensured consistent performance by evaluating the models on different subsets of the data.
- **Data Leakage Prevention**: Implemented a clean pipeline that ensures no data leakage between training and validation sets.
- **Fine-tuning**: Applied hyperparameter tuning using cross-validation to select the best parameters for each model.

---

## 📈 Results
- **Logistic Regression** provided the best Recall for class `1` (83%), effectively identifying the most potential buyers.
- **XGBoost** and **LightGBM** also performed well, offering a balance of accuracy and recall.
- **Cross-validation** results showed consistent model performance, confirming the robustness of the approach.
- **Business value**: Reduced spending on low-potential customers and increased the overall return on investment (ROI) for marketing campaigns.

---

## 💼 Business Value
| Benefit                  | Description |
|--------------------------|-------------|
| 🎯 Improved Targeting     | Predict customers more likely to convert |
| 💸 Cost Efficiency        | Avoid spending on low-potential customers |
| 🧪 Campaign Simulation    | Test before launching full-scale campaigns |
| 📊 Data-Driven Marketing  | Align promotions with customer behavior insights |

---

## ✅ Next Steps
- Test the model on live campaigns to assess real-world performance.
- Continuously monitor prediction quality and retrain models as needed.
- Deploy the model in a marketing decision system with cloud integration (AWS / Azure / GCP).

---

## 📁 Files
- `model.ipynb`: Full solution with data prep, EDA, modeling, evaluation, and cross-validation
- `README.md`: This documentation

---

## 👨‍💻 Author
Youssef Elzahar  
Data Science Roleplay – Sports Wear Group  
April 2025

---

This updated README now includes the following:
- Cross-validation to ensure robust performance.
- A pipeline to handle preprocessing and avoid data leakage.
- Fine-tuning of the models using `GridSearchCV` and `RandomizedSearchCV`.

Let me know if you'd like further modifications!

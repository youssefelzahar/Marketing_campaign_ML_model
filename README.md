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
- Handled outliers using percentile thresholds and median imputation.
- Addressed skewness using Box-Cox and Yeo-Johnson transformations.
- Encoded high-cardinality features (e.g. `article`) using Target Encoding.
- Normalized numeric features using MinMaxScaler.

### 📊 EDA
- Investigated why most `label` values are 0.
- Visualized relationships between pricing, promotions, and conversions.

### 🧠 Model Training
Tried and evaluated several models:
- Logistic Regression
- Random Forest
- Decision Tree
- XGBoost
- LightGBM

All models were evaluated using:
- Accuracy
- Precision / Recall / F1 (per class)
- ROC-AUC
- Confusion Matrix

---

## 📈 Results
- **Logistic Regression** provided the best Recall for class `1` (83%), identifying the most potential buyers.
- Models were compared using visual and tabular summaries.
- Business value: Reduce spend, improve targeting, increase ROI.

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
- Test model on live campaigns.
- Monitor prediction quality.
- Deploy in a marketing decision system with cloud integration (AWS / Azure / GCP).

---

## 📁 Files
- `model.ipynb`: Full solution with data prep, EDA, modeling and evaluation
- (Optional) `promo1.png`, `promo2.png`: Visuals for key EDA insights
- `README.md`: This documentation

---

## 👨‍💻 Author
Youssef Elzahar  
Data Science Roleplay – Sports Wear Group  
April 2025


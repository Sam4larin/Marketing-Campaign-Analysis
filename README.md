# Marketing Campaign Analysis
  # About This Project

This project analyzes customer demographics, spending patterns, and campaign effectiveness to evaluate the performance of marketing campaigns and uncover opportunities for improvement. Using Python for data preparation and Tableau for visualization, the analysis provides actionable insights and recommendations for optimizing marketing spend and targeting strategies.

Business Problem

Marketing campaigns are profitable overall but struggle with low customer engagement. The company wants to:

Understand which customers respond to campaigns.

Identify customer segments with the highest revenue potential.

Optimize budget allocation across channels and campaigns.




 Technologies & Tools Used:

- Python: Data cleaning, exploratory data analysis (EDA), clustering (K-Means).

- Pandas & NumPy: Data manipulation and preprocessing.

- Matplotlib & Seaborn: Data visualization.

- Scikit-Learn: Machine learning (clustering with K-Means, data scaling).

- Excel: Supporting calculations and quick validations.

- Tableau: Dashboard design, storytelling, business insights.
  
- Python → Data cleaning, exploratory data analysis (EDA), clustering (K-Means).


Key Dashboards
1. Campaign Performance Overview

Observation: Campaign ROI is high (~32x return), but engagement is low (~15%).

Insight: Responders spend more on premium categories (wines, sweets), while non-responders buy lower-margin items.

Recommendation: Reallocate budget toward targeted premium product campaigns to improve efficiency.

2. Customer Profile & Segmentation

Observation: Majority of customers are 40–60 years old; income skewed under $150K with a small high-income group.

Segments Identified:

Loyalists – High spend, frequent buyers.

Luxury Shoppers – High income, occasional buyers.

Budget Buyers – Price-sensitive, promotion-driven.

At-Risk Customers – Low spend, low response.

Recommendation: Personalize campaigns by cluster (loyalty programs, premium offers, discounts, or reactivation campaigns).

📌 Business Insights

Campaigns generate strong ROI but underperform on engagement → high potential for optimization.

Middle-aged customers drive most responses, while high-income groups represent untapped revenue potential.

Premium categories correlate with campaign success → focus promotions on wines & sweets.

Personalized targeting by customer segment can increase ROI by 10–15%.

🚀 Recommendations for Stakeholders

Reallocate ~20% of Catalog budget to Email/Digital → projected ROI uplift of +12%.

Launch personalized campaigns based on customer clusters.

Focus messaging on premium categories to increase engagement.

Pilot strategy in the next campaign cycle and monitor results via Tableau dashboards.


 # Business Context & Problem Statement

Business Context:

A retail company launched multiple marketing campaigns to increase sales. However, the conversion rates were low. The company needs a data-driven approach to:

- Identify customer purchasing patterns.

- Segment customers based on spending behavior and demographics.

- Optimize marketing efforts for better engagement and ROI.


Problem Statement:

- Who are the most valuable customers?

- Which products drive the highest engagement?

- What factors influence marketing campaign success?

- How can the business improve its targeting strategy?

 # Data Analysis & Key Insights

Customer Demographics:

- Most customers are 30-60 years old, with a peak in the 40-50 age range.

- Higher-income customers are more likely to spend on premium products.

Product Preferences:

- Wines and meat products are the highest-selling items.

- Fruits and sweets have lower engagement, indicating potential for better bundling or promotions.

Marketing Campaign Effectiveness:

- A significant portion of customers did not respond to campaigns.

- Higher-income groups showed better response rates.

- Low-income segments need better-targeted offers.

Customer Segments (K-Means Clustering Results):

1. High-income, high spenders – Premium product targets.

2. Middle-income, balanced spenders – Regular customers, retain with loyalty programs.

3. Low-income, low spenders – Price-sensitive; require budget-friendly offers.

4. Moderate-income, selective spenders – Buy specific items; target with related promotions.

 # Business Metrics & ROI

Key Performance Indicators (KPIs):

- Customer Retention Rate – How many customers remain engaged over time.

- Customer Lifetime Value (CLV) – Revenue potential per customer.

- Marketing Campaign ROI – Conversion rates per campaign.

- Average Order Value (AOV) – Average spend per transaction.

- Churn Rate – Percentage of customers who stop purchasing.

ROI Estimation:

- If high-value customers receive personalized campaigns, retention rates could increase by 15-20%.

- Bundling strategies could improve sales of underperforming products by 10-15%.

 # Technical Implementation

Data Preprocessing:

 - Handling missing values using median imputation.
   
 - Feature selection for clustering based on purchasing behavior and demographics.
   
 - Standardization of numerical values to normalize data.

Machine Learning (K-Means Clustering):

- Chose 4 clusters after testing different values using the Elbow Method.

- Features used: Spending on Wines, Meat, Fish, Fruits, Sweets, Gold Products, Income, Age.

- Visualized cluster results using scatter plots.

Data Visualization in Tableau:

- Created customer segmentation dashboards.

- Interactive sales & response rate visualizations.

- Product trend analysis for targeted marketing.

 # Stakeholder Recommendations

Strategic Insights:

1. High-value customers: Focus premium promotions on the top 20% of spenders.

2. Targeted marketing: Personalized campaigns based on customer segmentation.

3. Product Bundling Strategy: Increase cross-selling of underperforming items.

4. Customer Retention Programs: Loyalty discounts & exclusive offers for high-LTV customers.

Actionable Steps:

- Personalize email marketing based on spending clusters.

- Upsell wines & gold products to high-income clusters.

- Introduce bundle discounts for low-selling items.

- Optimize communication channels (e.g., SMS for middle-income groups, email for high-income groups).

Risk Assessment:

- High dependency on premium customers – Requires sustained engagement.

- Incorrect segmentation risks – Continuous refinement of clusters needed.

- Low response rate to campaigns – A/B testing of different strategies.

 # Future Scope & Scalability

Potential Improvements:

- Advanced machine learning models (e.g., Random Forest, XGBoost) for campaign success prediction.

- Real-time data processing for dynamic customer segmentation.

- A/B testing integration to improve marketing strategy effectiveness.

Scalability Options:

- Integration with CRM systems for automated customer segmentation.

- Deploying predictive analytics models to improve marketing decision-making.

- Expanding analysis to multiple markets for a global strategy.

# Conclusion

This project provided valuable insights into customer behavior, spending habits, and campaign effectiveness. By leveraging clustering, data visualization, and predictive analytics, businesses can make data-driven decisions to optimize marketing efforts and increase revenue.

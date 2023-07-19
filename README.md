Project Title: ABC Analysis of Sales Data

Description:
This project performs an ABC analysis on a sales dataset to classify SKUs based on their sales performance. The ABC analysis is a technique used to categorize items into different classes (A, B, and C) based on their relative importance. This analysis helps identify high-value items that contribute significantly to sales and prioritize inventory management and resource allocation accordingly.

The project utilizes Python and the pandas library to load and analyze the sales data, specifically focusing on the "SoldCount" and "AddCost" columns. The "SoldCount" represents the quantity sold for each SKU, while the "AddCost" indicates the additive cost per SKU.

The code performs the following steps:

Subset the data to include historical records and relevant columns.
Calculate the additive cost per SKU by multiplying the price and item count.
Sort the data by the additive cost in descending order.
Compute the running cumulative cost for each SKU.
Determine the total sum of the additive cost.
Calculate the running percentage by dividing the running cumulative cost by the total sum.
Assign a class (A, B, or C) to each SKU based on the running percentage.
The project includes code snippets to generate insightful graphs such as pie charts, bar charts, line plots, and histograms to visualize the results of the ABC analysis. These graphs offer a comprehensive overview of SKU distribution, cumulative costs, class segmentation, and other relevant insights.

The ABC analysis and associated graphs provide valuable information for inventory management, supply chain optimization, and decision-making processes. By understanding the relative importance of different SKUs, businesses can prioritize their resources, focus on high-value items, and improve overall operational efficiency.

This project can be used as a reference for implementing ABC analysis on sales data and serves as a starting point for further analysis and customization based on specific business needs.

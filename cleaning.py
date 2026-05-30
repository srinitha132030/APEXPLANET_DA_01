import pandas as pd

data_dict = pd.DataFrame({
    "Column Name": [
        "CustomerID",
        "Gender",
        "Age",
        "Annual Income (k$)",
        "Spending Score (1-100)",
        "Age_Group"
    ],
    "Data Type": [
        "Integer",
        "String",
        "Integer",
        "Integer",
        "Integer",
        "String"
    ],
    "Description": [
        "Unique identifier for each customer",
        "Gender of the customer",
        "Age of the customer",
        "Annual income in thousand dollars",
        "Customer spending score",
        "Derived age category"
    ]
})

print(data_dict)
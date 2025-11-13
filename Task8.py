import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'product_category': ['Electronics', 'Clothing', 'Groceries', 'Electronics', 'Clothing', 'Groceries', 'Electronics'],
    'sales': [12000, 8000, 6000, 15000, 7000, 4000, 20000]
}
)
total_sales = df.groupby('product_category')['sales'].sum()
print("Toatl Sales data: \n",total_sales)
total_sales.plot(x='product_category', y ='sales', kind = 'bar', title = 'Total Sales per Product Category', xlabel = "Product Category", ylabel="Total sales")
plt.show()



import pandas as pd 

celsius = [0, 20, 37, 100, -10]
celsius_a = pd.Series(celsius, name = "celsius")
fahrenheit_b = celsius_a * 9/5 + 32
temp_df = pd.concat([celsius_a, fahrenheit_b], axis=1)
print("\nNew Series:\n", temp_df)


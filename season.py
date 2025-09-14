import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Temperature data over time
# Jan 2000 - 2025
# temperatures = [10.7, 13.1, 12.1, 14, 11.8, 10.7, 10.5, 12.1, 12.2, 11.8,
#                 12.2, 9.7, 11.1, 9.9, 12.8, 12.2, 10.9, 15.5, 13.7, 11.9,
#                 12.2, 12.5, 12.9, 12.7, 10.9]
# Dec 2000 - 2024
# temperatures = [11.7,11.7,10.4,11.1,8.1,12.6,8.6,10.9,10.9,9.5,12.2,11,11.5,11.3,10.5,9.1,10.4,12.1,12.3,10.1,9.7,12.1,11.8,11.9,11.4]
# May 2000 - 2025
# temperatures = [5.8,5.8,4.3,5.1,7.1,4.8,5.2,6.1,2,2.9,5.2,6.7,3,4.6,3.8,3.3,6.7,3.2,4.6,4.4,3.9,3.8,5.1,6.5,0.9,3.8]

#June 2000 -2025
# temperatures = [3.8,1.7,2.8,3.5,3.6,1.4,0.5,0.2,2.1,1.7,2.3,3.6,0.5,2.3,2.5,1.3,2.8,2.1,3.9,0.5,3.4,4.6,2.9,4.1,2.7,2]

#July  2000 - 2025         
#temperatures = [5.1,-0.2,2,0.3,0.1,2.8,1.5,1.9,2.7,0.6,0.2,0.3,0.4,2,1.9,0.7,0.5,1.6,1.9,2.8,1.7,1.7,2.2,1.3,2.3,1.8]

# August 2000 - 2024
# temperatures = [2,3.3,2.8,2.9,2.6,1.7,1.6,1.7,3.7,4.4,0.6,5.1,4.6,1.7,1.9,1.3,3.1,3.3,0.8,3,3.3,3.5,0.6,2.4]

# September 2000 - 2024
# temperatures = [5.8,4.9,7.4,4.6,3.1,4.6,4.3,4.1,4.1,3.1,4.2,2.6,4.1,3.8,2.7,3.4,6.3,5.9,3.7,3.7,3.2,3.1,4.7,5.4,3.6]

# October 2000 - 2024
# temperatures = [6.7,8.2,4.6,5.2,6.5,6.4,6,4.9,4.1,4.8,4.9,6.9,4.8,6,4.8,5,7.1,6.7,5.6,5.1,7,7.3,4.4,6.1,6.6]
# Create time indices
x = np.arange(len(temperatures)).reshape(-1, 1)
y = np.array(temperatures)

# Fit linear regression model
model = LinearRegression()
model.fit(x, y)

# Get the slope of the regression line
slope = model.coef_[0]

# Predict values for trend line
y_pred = model.predict(x)

# Plot the data and trend line
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Temperature Data', marker='o')
plt.plot(x, y_pred, label='Trend Line', color='red')
plt.xlabel('Time Index')
plt.ylabel('Average Temperature')
plt.title('Temperature Trend Over Time')
plt.legend()
plt.grid(True)
plt.savefig("temperature_trend.png")

# Print the slope to determine trend direction
trend = "increasing" if slope > 0 else "decreasing" if slope < 0 else "stable"
print(f"The slope of the trend line is {slope:.4f}, indicating the temperatures are {trend} over time.")

# Change the transparency to 0.1
import matplotlib.pyplot as plt

plt.scatter(cellphone.x, cellphone.y,
           color='red',
           marker='s',
           alpha=.1)



# Add labels
plt.ylabel('Latitude')
plt.xlabel('Longitude')

# Display the plot
plt.show()


plt.bar(df.precinct, df.dog,
Label= 'Dog')
plt. bar(df.precinct, df.cat,
bottom=df. dog,
Label='Cat')
plt. legend plt. show()\



plt. plot(x, y1, color="tomato")
plt. plot(x, y2, color="orange")
plt. plot(x, y3, color="goldenrod")
plt. plot(x, y4, color="seagreen")
plt. plot(x, y5, color="dodgerblue")
plt. plot(x, yo, color="violet", linewidth=10, linestyle='-')
plt.plot(x, y1, marker='x')

# plt.style.use('fivethirtyeight | ggplot | seaborn | default')

# raise ValueError(
# ValueError: '.' is not a valid value for ls; supported values are '-', '--', '-.', ':', 'None', ' ', '', 'solid', 'dashed', 'dashdot', 'dotted'
# In [1]:

# Make the Los Angeles line dotted
plt.plot(data["Year"], data["Los Angeles Police Dept"], label="Los Angeles", linestyle="dotted")

# Add square markers to Philedelphia
plt.plot(data["Year"], data["Philadelphia Police Dept"], label="Philadelphia", marker="s")

# Add a legend
plt.legend()

# Display the plot
plt.show()


import seaborn as sns
import matplotlib.pyplot as plt
height = 162, 64, 69, 75, 66,
68, 65, 71, 76, 731
weight = 1120, 136, 148, 175, 137,
165, 154, 172, 200, 1871
sns.scatterplot(x=height, y=weight)
plt. show()


# Import Matplotlib and Seaborn

import seaborn as sns
import matplotlib.pyplot as plt


# Create count plot with region on the y-axis
sns.countplot(y=region)

# Show plot
plt.show() 


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("masculinity.csv")

# Determine the order of the categories by count
category_order = df['how_masculine'].value_counts().index

# Create the count plot with the sorted order
sns.countplot(x="how_masculine", data=df, order=category_order)

plt.show()


import pandas as pd
import matplotlib.pyplot as plt import seaborn as sns
df = pd.read_csv("masculinity.csv")
sns.countplot(x="how_masculine",
data=df)
plt. show()


# Change the legend order in the scatter plot
sns.scatterplot(x="absences", y="G3", 
                data=student_data, 
                hue="location",
                hue_order=["Rural", "Urban"])

# Show plot
plt.show()




# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create a dictionary mapping subgroup values to colors
palette_colors = {"Rural": "green", "Urban": "blue"}

# # Create a count plot of school with location subgroups
sns.countplot(x = "school", hue="location", palette=palette_colors, data=student_data)
student_data.info()

# # Display plot
plt.show()


sns.relplot(x="absences", y="G3", 
            data=student_data,
            kind="scatter", 
            row="study_time")

# Show plot
plt.show()


# Import Matplotlib and Seaborn
import matplotlib.pyplot as plt
import seaborn as sns

# Create scatter plot of horsepower vs. mpg
sns.relplot(x="horsepower", y="mpg", 
            data=mpg, kind="scatter", 
            size="cylinders",
            hue="cylinders")

# Show plot
plt.show()


import matplotlib.pyplot as plt
import seaborn as sns

# Add markers and make each line have the same style
sns.relplot(x="model_year", y="horsepower", 
            data=mpg, 
            kind="line", 
            ci=None, 
            style="origin", 
            dashes=False,
            markers=True,
            hue="origin")

# Show plot
plt.show()


# Import KNeighborsClassifier
from sklearn.neighbors import KNeighborsClassifier
y = churn_df["churn"].values
X = churn_df[["account_length", "customer_service_calls"]].values
# Create a KNN classifier with 6 neighbors
knn = KNeighborsClassifier(n_neighbors=6)
# Fit the classifier to the data
knn.fit(X, y)

# Predict the labels for the X_new
y_pred = knn.predict(X_new)
# Print the predictions
print("Predictions: {}".format(y_pred)) 



## test train split scikit learn.
# Import the module
from sklearn.model_selection import train_test_split
X = churn_df.drop("churn", axis=1).values
y = churn_df["churn"].values

# Split into training and test sets
X_train, X_test, Y_train, y_test = train_test_split(X, y, 
            test_size=0.2,
            random_state=42, 
            stratify=y)

knn = KNeighborsClassifier(n_neighbors=5)
knn. fit(X_train, Y_train)

# Fit the classifier to the training data


# Print the accuracy
print(knn.score(X_test,y_test))




# Create neighbors
neighbors = np.arange(1,13)
train_accuracies = {}
test_accuracies = {}

for neighbor in neighbors:
  
	# Set up a KNN Classifier
	knn = KNeighborsClassifier(n_neighbors=neighbor)
  
	# Fit the model
	knn.fit(X_train,y_train)
  
	# # Compute accuracy
	train_accuracies[neighbor] = knn.score(X_train, y_train)
	test_accuracies[neighbor] = knn.score(X_test, y_test)
	# # train_accuracies[____] = knn.____(____, ____)
	# # test_accuracies[____] = knn.____(____, ____)

print(neighbors, '\n', train_accuracies, '\n', test_accuracies)

# Add a title
plt.title("KNN: Varying Number of Neighbors")

# # Plot training accuracies
# plt.plot(____, ____, label="____")

# # Plot test accuracies
# plt.plot(____, ____, label="____")

plt.plot(neighbors, train_accuracies.values(), label="Training Accuracy") 
plt.plot(neighbors, test_accuracies.values(), label="Testing Accuracy")


plt.legend()
plt.xlabel("Number of Neighbors")
plt.ylabel("Accuracy")

# Display the plot
plt.show()



import numpy as np
X = np.array(sales_df['radio'])
y = np.array(sales_df['sales'])
X = X.reshape(-1,1)
print(X.shape)
print(y.shape)




from sklearn. linear_model import LinearRegression
reg = LinearRegression ()
reg.fit(X,y) 
predictions = reg. predict(X)
print(predictions[:5])


# Import matplotlib.pyplot
from sklearn. linear_model import LinearRegression
import matplotlib.pyplot as plt
# Create scatter plot
plt.scatter(X, y, color="blue")
# Create line plot
plt.plot(X, predictions, color="red")
plt.xlabel("Radio Expenditure ($)")
plt.ylabel("Sales ($)")
# Display the plot
plt.show()



#### -
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Create X, an array containing values of all features in sales_df except the 'sales' column
X = sales_df.drop("sales", axis=1).values
y = sales_df["sales"].values

# Split the dataset into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Instantiate the model
reg = LinearRegression()  # Add parentheses to instantiate the object

# Fit the model to the training data
reg.fit(X_train, y_train)

# Make predictions
y_pred = reg.predict(X_test)
print("Predictions: {}, Actual Values: {}".format(y_pred[:2], y_test[:2]))



### ////////////////// ###
# Import mean_squared_error
from sklearn.metrics import mean_squared_error
# Compute R-squared
r_squared = reg.score(X_test, y_test)
# Compute RMSE
rmse = mean_squared_error(y_test, y_pred, squared=False)
# # Print the metrics
print("R^2: {}".format(r_squared))
print("RMSE: {}".format(rmse))


### //////////////////  ####
# Import the necessary modules
from sklearn.model_selection import cross_val_score, KFold

# Create a KFold object
# kf = KFold(n_splits=6, shuffle=True, random_state=42)
kf = KFold(n_splits=6, shuffle=True, random_state=5)

reg = LinearRegression()

# Compute 6-fold cross-validation scores
cv_scores = cross_val_score(reg,X,y, cv=kf)
#cv_results = cross_val_score (reg, X, y, cv=kf)
# Print scores
print(cv_scores)


### //////////////////  ####
#print  the mean
print(np.mean(cv_results))
# Print the standard deviation
print(np.std(cv_results))
# Print the 95% confidence interval
print(np.quantile(cv_results, [.025, .975]))



### //////////////////  ####
# Import Ridge
from sklearn. linear_model import Ridge
alphas = [0.1, 1.0, 10.0, 100.0, 1000.0, 10000.0]
ridge_scores = []
for alpha in alphas:
  # Create a Ridge regression model
  ridge = Ridge(alpha=alpha)
  # Fit the data
  ridge.fit(X_train, y_train)
  # Obtain R-squared
  score = ridge.predict(X_test)
  # y_pred = ridge.predict(X_test)
  ridge_scores.append(score)
print(ridge_scores)
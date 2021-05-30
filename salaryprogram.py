import pandas

ds = ds['YearsExperience'].values.reshape(30, 1)

y = ds['Salary']

from sklearn.linear_model import LinearRegression

mind = LinearRegression()

#algo

model = mind.fit(x, y)

# y = c + wx

#9449 * 1.1

s = model.predict( [[ 1.1 ]] )

print("Salary for the experience is : ")

print(s)
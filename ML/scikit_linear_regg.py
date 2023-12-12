from sklearn.linear_model import LinearRegression
x = [[1],[2],[3],[4],[5]]
y = [2,4,6,8,10]
model = LinearRegression()
model.fit(x,y)

num = [[12]]
result = model.predict(num)
print(result)
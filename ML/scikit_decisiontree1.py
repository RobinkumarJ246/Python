from sklearn.tree import DecisionTreeClassifier

X = [
    [20, 'male', 'rich', 'urban'],
    [25, 'female', 'poor', 'urban'],
    [30, 'male', 'poor', 'rural'],
    [35, 'female', 'poor', 'urban'],
    [40, 'male', 'rich', 'rural'],
    [45, 'female', 'rich', 'urban'],
    [50, 'male', 'poor', 'rural']
]
y = [0, 0, 1, 1, 1, 0, 0]  # Purchase decision (0: Not buy, 1: Buy)

gender_mapping = {'male': 0, 'female': 1}
wealth_mapping = {'poor': 0, 'rich': 1}
location_mapping = {'urban': 0, 'rural': 1}
X_encoded = [[age, gender_mapping[gender], wealth_mapping[wealth], location_mapping[location]] for age, gender, wealth, location in X]

clf = DecisionTreeClassifier()

clf.fit(X_encoded, y)

input_data = input("Enter the age, gender, wealth, and location separated by commas, e.g., 26, male, rich, urban: ")
input_age, input_gender, input_wealth, input_location = input_data.split(', ')
input_encoded = [[int(input_age), gender_mapping[input_gender.lower()], wealth_mapping[input_wealth.lower()], location_mapping[input_location.lower()]]]
prediction = clf.predict(input_encoded)

if prediction[0] == 0:
    print("The user is not likely to buy the product.")
else:
    print("The user is likely to buy the product.")

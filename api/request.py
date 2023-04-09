import requests

# URL
url = 'http://localhost:5000'

# Change the value of experience that you want to test
payload = {"sepal length (cm)": 5.1,
           "sepal width (cm)": 3.5,
           "petal length (cm)": 1.4,
           "petal width (cm)": 0.2,}
payload1 = {"p1": 5.1,
           "p2": 3.5,
           "p3": 1.4,
           "p4": 0.2,}

r = requests.post(url, json=payload1)
# print(r.json())
print(r.content)



from firebase import firebase
firebase = firebase.FirebaseApplication('https://iotfb-fc0b9.firebaseio.com/', None)
result = firebase.get('/users', 1)
print(result)
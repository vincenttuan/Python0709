from firebase import firebase
firebase = firebase.FirebaseApplication('https://iotfb-fc0b9.firebaseio.com/', None)
result = firebase.patch('/users', {3:'anita'})
print(result)
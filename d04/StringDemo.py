word = "she sell sea shell on the sea shore"
print(word.count('s'))
print(word.count('she'))
print(word.count(' '))

password = 'abcABC123'.join("abc")
print(password)
print(len(password))
print(password.isalpha()) # 是否僅包含英文文字
print(password.isalnum()) # 是否包含英文或數字
print(password.isdigit()) # 是否僅包含數字

path = 'C:\nba\tiket.txt'
print(path)
path = r'C:\nba\tiket.txt'
print(path)
path = 'C:\\nba\\tiket.txt'
print(path)
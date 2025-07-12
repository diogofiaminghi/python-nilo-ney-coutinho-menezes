# como pegar o nome de usuário antes do @ num email
email = "diogofiaminghi@gmail.com"
username = email.split('@')[0]
dominio = email.split('@')[1].split('.')[0]
extensao = email.split('.')[1]
print(username)  # Output: diogofiaminghi
print(dominio)  # Output: gmail
print(extensao)  # Output: com

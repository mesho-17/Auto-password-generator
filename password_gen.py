import string #python library/ module containing string constants.
import random #random characters generator.
 
def generate_password(size):
   all_chars = string.ascii_letters + string.digits + string.punctuation
   password = ''
   for char in range(size): #after password size specification, the code will generate the password randomly.
       rand_char = random.choice(all_chars) #creation of random characters
       password = password + rand_char # or password += rand_char
   return password #return value.
 
pass_len = int(input('How many characters in your password?')) 
new_password = generate_password(pass_len) #pass_len is an argument passed to the 'generate_password' function. (the function call)
print('Here is Your new password: ', new_password)

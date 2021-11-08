def check_palindrome(str1):
	if str1[::-1] == str1:
		return true
	return false
str1 = input()
if check_palindrome(str1) == True:
	print("palindrome")
else:
	print("Not a Palindrome")

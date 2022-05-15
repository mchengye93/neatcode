def reverseChar(list_char ,left, right):

	while left < right: 
		list_char[left], list_char[right] = list_char[right], list_char[left]
		left +=1
		right -=1

def reverseWord(message):
	reverseChar(message, 0, len(message)-1)

	start_word_index= 0
	for i in range(len(message)+1):

		if  i == len(message) or message[i] == ' ':
			reverseChar(message, start_word_index, i - 1)
			start_word_index = i + 1



message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverseWord(message)

# Prints: 'steal pound cake'
print ''.join(message)
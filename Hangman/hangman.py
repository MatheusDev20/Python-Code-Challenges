import random
possible_top_words = ["Gangplank", "Darius", "Ornn", "Sion", "Tryndamere", "Nasus"]
possible_adc_words = ["Varus", "Jinx", "Tristana", "Vayne", "Kalista"]
possible_mid_words = ["Annie", "LeBlanc", "Qyana", "Anivia", "Fizz"]
possible_jungle_words = ["Udyr", "Rengar", "Elise", "Olaf", "Sejuani"]
possible_sup_words = ["Thresh", "Bardo", "Lulu", "Yuumi", "Nautilus"]


print("Welcome to League of Legends Hangman Game (: ")
s_word = input("Type anything to get started: ")

def generateSelectedWord(list_of_words):
  selected = None
  r = random.randint(0, len(list_of_words) -1)
  for i in range(len(list_of_words)):
    if i == r:
      selected = list_of_words[i]
  
  return selected

# "JINX" "->" ["J", "I", "N"] "->" "J I N __"
def showPreviewWord(word, rightChars):
  previewWord = ''
  for character in word:
    if character in rightChars:
      previewWord = previewWord + character
      
    else: 
      previewWord = previewWord + " _ "
    
  return previewWord

def selectRole(n):
  words = None
  roles = {
    '1': possible_top_words,
    '2': possible_adc_words,
    '3': possible_mid_words,
    '4': possible_jungle_words,
    '5': possible_top_words
  }
  for k in roles:
    if k == n: words = roles[k]
  return words

def start():
  print("Please Select a Role to guess the champions: ")
  role = input(" Press 1 for Top Laners \n Press 2 for Ad Carrys \n Press 3 for mid laners\n Press 4 for Junglers \n Press 5 for Suports \n")
  print(role)
  number_attempts = 10
  selectedWord = generateSelectedWord(selectRole(role))
  hashedWord = ''
  rightChars = []

  for i in range(len(selectedWord)): hashedWord = hashedWord + " _ "

  print(f"You have {number_attempts} chances to guess this word {hashedWord}")

  i = 1
  while(i < number_attempts):
    entered_letter = input('Enter a letter: ')
    if entered_letter in selectedWord:
      print("Correct!")
      rightChars.append(entered_letter)
      preview_word = showPreviewWord(selectedWord, rightChars)
      print(preview_word)
      if preview_word == selectedWord:
        print("Congratulations you won the game")
        return 
      print("Preview Word: " + preview_word)
      print(f"Tentativas restantes {number_attempts - i} ")

    else:
      print("Wrong !")
      print(f"Tentativas restantes {number_attempts - i} ")
      print("Preview Word: " + showPreviewWord(selectedWord, rightChars))
    i +=1

  print("Your attempts over, start anoter game")
  

if s_word !=  None:
  start()


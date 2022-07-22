print('''

                       _,aaadP""""""Ybaaaa,,_
                   ,adP,__,,,aaaadP"""""Y888888a,_
                ,a8888888P"''             "Y8888888b,
             _a888888888"                   `Y88888888b,
           ,d888888888P'                       "888888888b,
         ,88888888P"Y8,                       ,P'   `""Y888b,
       ,d8888P"'     "Ya,                    ,P'         `Ya`b,
      ,P88"'           `Ya,                 ,P'            `b`Yi
     d",P                `"Y,              ,P'              `Y "i
   ,P' P'                   "888888888888888b                `b "i
  ,P' d'                    d8888888888888888b                `b `b
  d' d'                    ,888888888888888888b                I, Y,
 ,f ,f                    ,88888888888888888888b               `b, b
 d' d'                    d888888888888888888888b              ,88,I
,P  8                    ,88888888888888888888888b,_          ,d8888
d'  8,                   d8888888888888888888888P'`"Ya,_     ,d88888
8  d88b,             ,adP""Y888888888888888888P'      `""Ya, d88888P
8 ,88888b,       ,adP"'     `"Y8888888888888"'             `"888888I
Y,88888888b, ,adP"'             ""Y888888P"                  888888'
`888888888888P'                     ""YP"                    888888
 I88888888888                          8                     88888I
 `Y8888888888                          8                     88888'
  `Y888888888        Golden            8                     8888I
   `Y88888888        Ball              8                     8P"8'
    `Y8888888,                         8                   ,d',d'
     `b""""Y8b                         8                 ,d" ,d'
       "b,   "Y,                       8               ,P" ,d"
         "b,   "Ya,_                 ,d88ba,,___   _,aP" ,P"
           "Ya_   ""Ya,_       _,,ad88888888888888P"' _,d"
             `"Ya_    ""Yaaad88888888888888888888P _,d"'
                 `"Ya,_     "Y888888888888888888P",d"'
                    `""Ya,__`Y888888888888888P"""
                         ``"""""""""""""''
''')
print("Welcome to Soccer Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
user_answer = input('You\'re at a crossroad. Where do you want to go? Type \"left" or "right\"').lower()

if user_answer == "left":
  user_answer_two = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.').lower()

  if user_answer_two == "wait": 
    print("You get attacked by an angry trout. Game Over.")
  
  elif user_answer_two == "swim":
    user_answer_three = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?").lower()

    if user_answer_three == "red":
      print("It's a room full of fire. Game Over.")
    
    elif user_answer_three == "yellow":
      print("You found the treasure! You Win!")
    
    elif user_answer_three == "blue":
      print("You enter a room of beasts. Game Over.")
  
    else:
      print("Game Over")
  
else:
  print("You fell into a hole. Game Over.")
    
print('''


                  _/~~~\_/~~~\_
                 /~~~~~~~~~~~~~\_
                /~~~~~~~~~~~~~~~~\
               /~~~~~~~~~~~~~~~~~~\
              /~~~~~~~~~~~~~~~~~~~~\
             /~~~~~~~~~~~~~~~~~~~~~~\
            /~~~~~~~~~~~~~~~~~~~~~~~~\
           /~~~~.__~~~~~~~~~~~~~~~~~~~\
          |~~~~~|  \_~~~~~~~~~~~.~~~~~|
          /~~~~~|    \___~~~___/|~~~~~\
         /~~~~~~|        \_/    |~~~~~~\
        |~~~~~~~|              .|~~~~~~|
        |~~~~~~~|'===-    -===' |~~~~~~|
        /~~~~~~~| ___      ___  |~~~~~~\
       |~~~~~~~~|[_@_\    /_@_] |~~~~~~~\
       |~~~~~~~~|        .      |~~~~~~~~\
       |~~~~~~~~\        |      |~~~~~~~~~|
       /~~~~~~~~~|       \      |~~~~~~~~~~\
      |~~~~~~~~~~|     ___)     |~~~~~~~~~~~|
      |~~~~~~~~~~\     ^ ^      |~~~~~~~~~~~|
      |~~~~~~~~~~~|._        _. |~~~~~~~~~~~\
      |~~~~~~~~~~~|  \======/   A~~~~~~~~~~~~|
      |~~~~~~~~~~~\   |IIII|   /|~~~~~~~~~~~~|
      |~~~~~~~~~~~~|  |====|  /#|\~~~~~~~~~~~|
      |~~~~~~~~~____\ |    | |##|?\_~~~~~~~~~|
      |~~~~~~__/?:| #\______/#  |:??\__~~~~~~|
       \____/???. |::::|::::::::| .????\___~~|
    ___/???????: ?\:::|:::::::::|? :???????\_|__
  _/??????????. ???|::|::::::::/??? .???????????\_
 /???????????: ????|::A:::::::/????? :????????????
|???????????. ?????|_/H\::::_/??????? .???????????
|??????????: ????? /***\|::/????????? |???????????
|?????????. ????? (*****|_/?????????? |???????????
|????????| ??????? \***/ ???????????? |???????????
|????????| ???????? III ????????????? |???????????
|????????| ??????? /+ +\ ???????????? |???????????
|????????| ?????? ! + + ! ??????????? |???????????
|?????????\ ????? !+ + +! ?????????? /????????????
|??????????\ ???? ! + + ! ????????? /?????????????
|???????????| ??? !+ + +! ???????? |??????????????
|???????????| ??? ! + + ! ???????? |??????????????
|??????????/ ???? !+ + +! ????????? \?????????????
|?????????| ????? ! + + ! ?????????? |?????????? /
|?????????| ????? !+ + +! ?????????? |????????? |?
|?????????| ????? ! + + ! ?????????? |????????? |?
''')

print("Welcome to the Vampire Game !")
print("You're Mission is to kill the vampire")

choice1 = input ("You want to cross the door .Type 'Left' or 'Right' ")
if choice1 == 'Left':
  choice2 = input ("vampire blood . Type 'drink' or 'dont_drink' ")
  if choice2 == 'drink':
    choice3 = input("Which door you want to choose: One Door is Red, One Door is Blue, One Door is Black")
    if choice3 == "Red":
      print("You are killed by Beast")
    elif choice3 == "Blue":
      print("You are Killed by Fire")
    elif choice3 == "Black":
      print("you are the winner you killed the vampire")

  else:
    print("Your dead")
else:
  print("game over ")
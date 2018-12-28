import itertools

def solve(subtrahend, minuend, diff):

   left = list()
   left.append(subtrahend.lower().replace(' ',''))
   left.append(minuend.lower().replace(' ',''))

   right = diff.lower().replace(' ','')
   
   words = list(left)
   words.append(right)

   letters = list()
   new_letters=list()

   for word in words:
      for letter in word:
         if letter not in letters:
            letters.append(letter)
            #new_letters.append(letter)

   ''' 
   del new_letters[0]

   digits = [0,2,3,4,5,6,7,8,9]
   

   domain_carryover=[1,-1]
   '''
   
   #letters= e i g h t f o u r

   ranges = [0,2,3,4,5,6,7,8,9]

   steps = 0
   numOfSol=0

   for p in itertools.permutations(ranges, len(letters)):
      sol = dict(zip(letters, p))

      sol[left[0][0]] = 1

      if((sol[left[0][1]] > sol[left[1][0]])):
         continue

      #if T > R
      if(sol[left[0][-1]] > sol[left[1][-1]]):
         if (sol[right[-1]] != sol[left[0][-1]] - sol[left[1][-1]]):
            continue
            #If H > U
            if(sol[left[0][3]] > sol[left[1][2]]):
               if (sol[right[2]] != sol[left[0][3]] - sol[left[1][2]]):
                  continue
                  #IF G > O
                  if(sol[left[0][2]] > sol[left[1][1]]):
                     if (sol[right[2]] != sol[left[0][2]] - sol[left[1][1]]):
                        continue
                  #if G < O
                  else:
                     if (sol[right[1]] != 10 + sol[left[0][2]] - sol[left[1][1]]):
                        continue

            #if H < U, need carryover
            else:
               if (sol[right[2]] != 10 + sol[left[0][3]] - sol[left[1][2]]):
                  continue
                  #if G>O
                  if(sol[left[0][2]] > sol[left[1][1]]):
                     if (sol[right[2]] != sol[left[0][2]] - sol[left[1][1]] -1 ):
                        continue
                  #if G < O
                  else:
                     if (sol[right[1]] != 10 + sol[left[0][2]] - sol[left[1][1]] -1 ):
                        continue


      #if T < R, need carry-over
      if(sol[left[0][-1]] < sol[left[1][-1]]):
         #the answer doesnt match
         if (sol[right[-1]] != 10 + sol[left[0][-1]] - sol[left[1][-1]] ):
            continue
            #If H > U
            if(sol[left[0][3]] > sol[left[1][2]]):
               if (sol[right[2]] != sol[left[0][3]] - sol[left[1][2]] -1 ):
                  continue
                  #IF G > O
                  if(sol[left[0][2]] > sol[left[1][1]]):
                     if (sol[right[2]] != sol[left[0][2]] - sol[left[1][1]] -1 ):
                        continue
                  #if G < O
                  else:
                     if (sol[right[1]] != 10 + sol[left[0][2]] - sol[left[1][1]] -1 ):
                        continue

            #if H < U, need carryover
            else:
               if (sol[right[2]] != 10 + sol[left[0][3]] - sol[left[1][2]] -1 ):
                  continue
                  #if G>O
                  if(sol[left[0][2]] > sol[left[1][1]]):
                     if (sol[right[2]] != sol[left[0][2]] - sol[left[1][1]] -1 ):
                        continue
                  #if G < O
                  else:
                     if (sol[right[1]] != 10 + sol[left[0][2]] - sol[left[1][1]] -1 ):
                        continue

      if sol[left[1][0]] != 0 and sol[right[0]] != 0:
         steps += 1
         result = []
         for word in left:
            result.append(get_value(word, sol))

         answer = result[0] - result[1]

         if answer == get_value(right, sol):
            numOfSol += 1
            print(' - '.join(str(get_value(word, sol)) for word in left) + " == " + str(get_value(right, sol)))

            print("STEPS:", steps)

   print("TOTAL STEPS:", steps)
   print("Number of Solutions: ", numOfSol)
   if(numOfSol == 0):
      print("No solutions")


def get_value(word, new_word):
    num = 0
    carry = 1

    for w in reversed(word):
        num += carry * new_word[w]
        carry *= 10

    return num


def user_input():
   subtrahend = input("Please enter subtrahend: ")
   minuend = input("Please enter minuend:" )
   diff = input("Please enter difference: ")
   solve(subtrahend, minuend, diff)


if __name__ == "__main__":
   user_input()

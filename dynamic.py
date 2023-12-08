from os import read
import sys


def main():
   coins, amount = read_file(sys.argv[1])
   T = makeTable(coins, amount)
   sum_cols = colSums(coins)
   populateTable(T, coins, amount, sum_cols)
   # print(coins)
   # printTable(T)
   min_num_coins = findMinCoins(T, coins, amount)
   finisher(T, coins, amount, min_num_coins)

def findMinCoins(T, coins, amount):
   # minimum coins should be lowest num in last row
   last_row = len(T) - 1
   last_cell = len(T[last_row]) - 1
   min_num_coins = T[last_row][last_cell]
   if amount == 0:
      min_num_coins = 0
   elif(min_num_coins == float("inf")):
      min_num_coins = None
   return min_num_coins

def finisher(T, coins, amount, min_num_coins):
   if(min_num_coins == None):
      print("It is not possible to make change for", str(amount) + '.', end='')
   elif(min_num_coins == 0):
      print("It is possible to make change for 0:")
   else:
      coins_used = findCoins(T, coins, amount, min_num_coins)
      coins_used = sorted(coins_used)
      print("It is possible to make change for", str(amount) + ':')
      i = 1
      for coin in coins_used:
         print(str(coin), end='')
         if (len(coins_used) != i):
            print(", ", end='')
         i += 1

def findCoins(T, coins, amount, min_num_coins):
   last_row = len(T) - 1
   index = (T[last_row]).index(min_num_coins)
   coins_used = []
   remaining = amount
   coins_left = min_num_coins
   while remaining > 0:
      coins_used.append(coins[index-1])
      remaining = remaining - coins[index-1]
      coins_left -= 1
      if(coins_left > 0):
         index = T[remaining].index(coins_left)
   return coins_used


def populateTable(T, coins, amount, sum_cols):
   #sum_incr is 0, 1, 2,... to amount
   #sum_cols is [[0], [[0]+[1]]... ]
   sum_incr = 0
   count = 0
   # i is counting up 0, 1, 2...
   for row in T:
      for i in range(1, len(T[count])):
         # first column
         if i == 0:
            pass
         # case where Di > j
         elif sum_incr > sum_cols[i]:
            T[count][i] = float('inf')
         elif sum_incr == coins[i-1]:
            T[count][i] = 1
         # use cj
         elif sum_incr < coins[i-1]:
            T[count][i] = T[count][i-1]
         # case where compare the min of two things
         else:
            use = sum_incr - coins[i-1]
            used = T[use][i-1] + 1

            # we just take the previous cell
            dont = T[count][i-1]
            low = min(used, dont)
            T[count][i] = low

      count += 1
      sum_incr += 1



def colSums(coins):
   sums = []
   sum = 0
   for coin in coins:
      sum += coin
      sums.append(sum)
   sums.insert(0, float('inf'))
   return sums

def makeTable(coins, amount):
   num_coins = len(coins)
   # zeroes = (num_coins + 1) * [0]
   T = list()
   for x in range(amount + 1): 
      T.append((num_coins + 1) * [0])
   for row in T:
      row[0] = float('inf')
   return T

def printTable(table):
   for row in table:
      print(row)
   print("")

def read_file(file_name):
    f = open(file_name, 'r')
    line = f.readline()
    #need to make the strings ints
    mapped = map(int, line.split(", "))
    a_list = list(mapped)
    a_list = sorted(a_list)
    line = f.readline()
    amount = int(line)
    return a_list, amount

main()
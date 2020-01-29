from math import ceil
from random import randint

def decToBinary(blockSize, key):
  result = ""
  exp = blockSize - 1
  for i in range(exp, -1, -1):
    #print(key, 2**i)
    if (key >= 2**i):
      result += '1'
      key -= 2**i
    else:
      result += '0'
  return result

def decToHex(blockSize, key):
  result = ""
  exp = blockSize - 1
  for i in range(exp, -1, -1):
    for j in range (15, -1, -1):
     
      if key >= 0 and key - j * 16**i >= 0:

        if (j == 10):
          result += 'A'
        elif (j == 11):
          result += 'B'
        elif (j == 12):
          result += 'C'
        elif (j == 13):
          result += 'D'
        elif (j == 14):
          result += 'E'
        elif (j == 15):
          result += 'F'
        else:
          result += str(j)
        key -= j * 16**i
        break

  
  
  return result
def encryption():

  blockSize = 4
  maxrand = 16**blockSize
  key = randint(0, maxrand - 1)
  resultKey = decToHex(blockSize, key)
  print(resultKey)
  message = input("Input a value ")
  blockSize = 4
  blocks = []
  messageLength = len(message)
  numBlocks = ceil(messageLength/blockSize)
  
  for j in range(numBlocks):
    blocks.append(message[j*blockSize:(j*blockSize)+blockSize])

  if len(blocks[-1]) != blockSize:
    diff = blockSize - len(blocks[-1])
    blocks[-1] += (" " * diff)


  

  output = ""

  for j in range(len(blocks)):
    #iterate each char in each block
    for n in range (len(blocks[j])):
      #print(resultKey[j])
      output += (chr(ord(resultKey[n]) ^ ord(blocks[j][n])))
  print(output)
  menu()

    

def decryption():
  key = input("Input your key")
  message = str(input("Input your output"))
  #resultKey = decToHex(blockSize, key)
  output= ""
  blocks = []
  messageLength = len(message)
  numBlocks = ceil(messageLength/blockSize)
  
  for j in range(numBlocks):
    blocks.append(message[j*blockSize:(j*blockSize)+blockSize])

  if len(blocks[-1]) != blockSize:
    diff = blockSize - len(blocks[-1])
    blocks[-1] += (" " * diff)
  for j in range(len(blocks)):
    #iterate each char in each block
    for n in range (len(blocks[j])):
      output += (chr(ord(key[n]) ^ ord(blocks[j][n])))
  print(output)




def myhash():
  message = input("Input a value")
  blockSize = 4
  messageLength = len(message)
  blocks = []
  numBlocks = ceil(messageLength/blockSize)

  for j in range(numBlocks):
    blocks.append(message[j*blockSize:(j*blockSize)+blockSize])

  if len(blocks[-1]) != blockSize:
    diff = blockSize - len(blocks[-1])
    blocks[-1] += (" " * diff)
  '''
  for j in range(numBlocks):
    blocks[j] = blocks[j].encode('utf-8')
  '''

  iv = '0123'
  output = ""
  for n in range (numBlocks):
    output = ""
    for j in range(len(blocks[n])):
      output += (chr(ord(iv[j]) ^ ord(blocks[n][j])))
    iv = output
  print (iv)
  menu()



blockSize = 4
maxrand = 2**blockSize
key = randint(0, maxrand - 1)
#print(key)
#print(decToHex(blockSize, key))



def menu():
  choice = int(input("\n choose one of the following and type the corresponding number below: \n 1-hash \n 2-encryption \n 3-decryption \n \n"))

  if (choice == 1):
    myhash()
    print("ok")

  elif (choice == 2):
    encryption()

  elif (choice == 3):
    decryption()

  else:
    print("Please try again!")
  

menu()
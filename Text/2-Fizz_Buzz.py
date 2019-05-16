#Fizz Buzz:
#Write a program that prints the numbers from 1 to 100.
#But change the numbers that are
#multiple of three for “Fizz”
#for the multiples of five write "Buzz"
#And for numbers that are multiples of both (3&5)
#write “FizzBuzz”.

def main():
    for i in range(1,101):
        if i%3 ==0:
            if i%5 ==0:
                print ("FizzBuzz")
            else:
                print ("Fizz")
        elif i%5 ==0:
            print ("Buzz")
            
        else:
            print (i)
                 
  
if __name__ == '__main__':
    main()    

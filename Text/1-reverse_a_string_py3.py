#EASY WAY - WORKING PY3 - slice and steps backwards
#########################################
#x = input("Enter a string to reverse ")
#y = x[::-1]
#print ("this is 'y' "+y)
#########################################

#######################################################
#THIS SCRIPT USES A 'FOR' LOOP TO CREATE AN ARRAY     #
#WITH THE LETTERS ARRANGED BACKWARDS                  #
#######################################################
def reverse(x):
    l = len(x) - 1
    reverseStr = ""
    for i in range(l,-1,-1):
        reverseStr += x[i]
    return reverseStr

def main():
    string = input("Enter a string to reverse: ")
    print ("The reversed string is: " + reverse(string))

if __name__ == '__main__':
    main()
#######################################################

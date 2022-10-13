import random
import time

FILE_NAME = "text3.txt"  # The name of the file in which random numbers will be written


def main():
    # Generate random number while making sure it's unique (not in 'arr')
    def safe_randrange(arr, start, stop, step):
        number = random.randrange(start, stop, step)
        while number in arr:
            number = random.randrange(start, stop, step)
        return number

    # What is going to hold the data
    our_list = []  # The list that will contain the random numbers
    our_file = open(FILE_NAME, "a")  # The file in which random numbers will be written

    for i in range(80000):
        generated = safe_randrange(our_list, 0, 80000, 1)  # Generate unique random number
        our_list.append(generated)  # Append it to the list
        our_file.write(str(generated) + "\n")  # Append it to the file
    our_file.close()  # Done writing

    # our_file = open(FILE_NAME, "r")  # Open same file to read
    # print(our_file.read())  # Read file
    # our_file.close()  # Done reading


start_time = time.time()
main()
print("--- %s seconds ---" % (time.time() - start_time))

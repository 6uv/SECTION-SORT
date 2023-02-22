
# In CMD use " pip install numpy; pip install colorama " 

import numpy as np
import os
from colorama import Fore

def selectionSort(array, size):
    for i in range(size):
        q = i
        for j in range(i + 1, size):
            if array[j] < array[q]:
                q = j
        (array[i], array[q]) = (array[q], array[i])
 
os.system('cls')
length = input(f"[{Fore.RED}>{Fore.RESET}]  how many numbers would you like in your unsorted array?:{Fore.YELLOW} ")
arr = np.random.randint(-999, 999, int(length))
print(f'{Fore.RESET}Your list is {Fore.RESET}{Fore.RED}{arr}{Fore.RESET}')
size = len(arr)
selectionSort(arr, size)
print(f'smallest to largest: {Fore.RESET}{Fore.GREEN}{arr}{Fore.RESET}')
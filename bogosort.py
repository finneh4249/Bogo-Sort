import random
import time
from pyfiglet import figlet_format
from sys import argv

if len(argv) > 1:
    if argv[1] == "-h" or argv[1] == "--help":
        print("Usage: python3 bogosort.py <n>")
        print("<n>: The number of elements in the randomly generated list")
        print("Example: python3 bogosort.py 10")
        exit(0)

    n = int(argv[1])
else:
    n = 10
data = [random.randint(0, 100) for _ in range(n)]

class App():
    def __init__(self):
        self.data = data
    
    def is_sorted(self, data):
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                return False
        return True

    def bogo_sort(self, data):
        comparison_counter = 0
        while not self.is_sorted(data):
            comparison_counter += 1
            random.shuffle(data)
        print("Number of comparisons:", comparison_counter)
        return data
    
    def run(self):
        print(figlet_format("BOGO SORT", font="slant"))
        print("Unsorted:", data)
        start = time.time()
        sorted_data = self.bogo_sort(self.data)
        end = time.time()
        print("Sorted:", sorted_data)
        print("Time taken: {:.2f} seconds".format(end - start))
        


if __name__ == "__main__":
    app = App()
    app.run()
    

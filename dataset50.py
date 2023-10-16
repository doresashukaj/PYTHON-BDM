import csv
import time
import psutil


def measure_performance(algorithm, data, target):
    start_time = time.process_time()
    memory_usage = psutil.Process().memory_info().rss / 1024 / 1024  # in MB

    result = algorithm(data, target)

    end_time = time.process_time()
    execution_time = end_time - start_time

    return result, execution_time, memory_usage

# Linear Search, Binary Search, Hashing, and Ternary Search functions remain the same
# Linear Search
def linear_search(data, target):
    for row in data:
        if target in row:
            return True
    return False

# Binary Search
def binary_search(data, target):
    left = 0
    right = len(data) - 1

    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return True
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

# Hashing
def create_hash_table(data):
    hash_table = {}
    for row in data:
        for element in row:
            hash_table[element] = True
    return hash_table

def hash_search(hash_table, target):
    return target in hash_table

# Flatten the list of lists
def flatten_data(data):
    flattened_data = []
    for row in data:
        for element in row:
            flattened_data.append(element)
    return flattened_data

# Load CSV data
def load_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

# Measure running time and memory usage
# measure_performance function remains the same

# Example usage
filename = 'dataset50k.csv'  # Replace with your CSV filename
target_value = '33333' # Replace with your target value

data = load_csv(filename)
flattened_data = flatten_data(data)  # Flatten the data for search algorithms
sorted_data = sorted(flattened_data)  # Sort the flattened data

hash_table = create_hash_table(data)

# Linear Search, Hashing, Interpolation Search, and Ternary Search remain the same

# Binary Search
binary_result, binary_time, binary_memory = measure_performance(binary_search, sorted_data, target_value)
print(f"Binary Search: Result={binary_result}, Time={binary_time} seconds, Memory={binary_memory} MB")


# Ternary Search
# Ternary Search
def ternary_search(data, target):
    flattened_data = [str(element) for sublist in data for element in sublist]
    flattened_data.sort()

    left = 0
    right = len(flattened_data) - 1

    while left <= right:
        partition_size = (right - left) // 3
        mid1 = left + partition_size
        mid2 = right - partition_size

        if flattened_data[mid1] == target:
            return True
        if flattened_data[mid2] == target:
            return True

        if target < flattened_data[mid1]:
            right = mid1 - 1
        elif target > flattened_data[mid2]:
            left = mid2 + 1
        else:
            left = mid1 + 1
            right = mid2 - 1

    return False


# Load CSV data
def load_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data
def flatten_data(data):
    flattened_data = []
    for row in data:
        for element in row:
            flattened_data.append(element)
    return flattened_data
filename = 'dataset50k.csv'  # Replace with your CSV filename
target_value = '27.32'  # Replace with your target value

# Interpolation Search
def interpolation_search(data, target):
    flattened_data = [str(element) for sublist in data for element in sublist if isinstance(element, (int, float))]
    flattened_data.sort()

    left = 0
    right = len(flattened_data) - 1

    while left <= right and flattened_data[left] <= target <= flattened_data[right]:
        if left == right:
            if flattened_data[left] == target:
                return True
            return False

        pos = left + ((int(target) - int(flattened_data[left])) * (right - left)) // (int(flattened_data[right]) - int(flattened_data[left]))

        if flattened_data[pos] == target:
            return True
        elif flattened_data[pos] < target:
            left = pos + 1
        else:
            right = pos - 1

    return False

# Load CSV data

def load_csv(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)
    return data

# Measure running time and memory usage
def measure_performance(algorithm, data, target):
    start_time = time.process_time()
    memory_usage = psutil.Process().memory_info().rss / 1024 / 1024  # in MB

    result = algorithm(data, target)

    end_time = time.process_time()
    execution_time = end_time - start_time

    return result, execution_time, memory_usage

filename = 'dataset50k.csv'  # Replace with your CSV filename
target_value = '27.32'  # Replace with your target value

data = load_csv(filename)
flattened_data = flatten_data(data)  # Flatten the data for search algorithms
sorted_data = sorted(flattened_data)  # Sort the flattened data

hash_table = create_hash_table(data)

# Linear Search, Hashing, Interpolation Search, and Ternary Search remain the same

# Binary Search
binary_result, binary_time, binary_memory = measure_performance(binary_search, sorted_data, target_value)
print(f"Binary Search: Result={binary_result}, Time={binary_time} seconds, Memory={binary_memory} MB")
# Example usage
filename = 'dataset50k.csv'  # Replace with your CSV filename
target_value = '27.32'  # Replace with your target value

data = load_csv(filename)
sorted_data = sorted(data)  # Binary, Interpolation, and Ternary search require sorted data
hash_table = create_hash_table(data)

# Linear Search
linear_result, linear_time, linear_memory = measure_performance(linear_search, data, target_value)
print(f"Linear Search: Result={linear_result}, Time={linear_time} seconds, Memory={linear_memory} MB")



# Hashing
hash_result, hash_time, hash_memory = measure_performance(hash_search, hash_table, target_value)
print(f"Hashing: Result={hash_result}, Time={hash_time} seconds, Memory={hash_memory} MB")# Ternary Search
ternary_result, ternary_time, ternary_memory = measure_performance(ternary_search, sorted_data, target_value)
print(f"Ternary Search: Result={ternary_result}, Time={ternary_time} seconds, Memory={ternary_memory} MB")
# Interpolation Search
interpolation_result, interpolation_time, interpolation_memory = measure_performance(interpolation_search, sorted_data, target_value)
print(f"Interpolation Search: Result={interpolation_result}, Time={interpolation_time} seconds, Memory={interpolation_memory} MB")
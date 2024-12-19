import matplotlib.pyplot as plt
import numpy as np

# Function to display the array as a bar chart
def display_array(arr, title):
    plt.clf()  # Clear the current figure
    plt.bar(range(len(arr)), arr, color='blue')
    plt.title(title)
    plt.ylim(0, max(arr) + 1)  # Set y-limit to give some space above the bars
    plt.pause(0.5)  # Pause for a short period to create animation effect

# Bubble Sort with visualization
def bubble_sort_visualizer(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap
            display_array(arr, f'Bubble Sort: {arr}')
    plt.show()

# Insertion Sort with visualization
def insertion_sort_visualizer(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            display_array(arr, f'Insertion Sort: {arr}')
        arr[j + 1] = key
        display_array(arr, f'Insertion Sort: {arr}')
    plt.show()

# Selection Sort with visualization
def selection_sort_visualizer(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
            display_array(arr, f'Selection Sort: {arr}')
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # Swap
        display_array(arr, f'Selection Sort: {arr}')
    plt.show()

# Merge Sort with visualization
def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    L = arr[left:left + n1]
    R = arr[mid + 1:mid + 1 + n2]

    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
        display_array(arr, f'Merge Sort: {arr}')

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
        display_array(arr, f'Merge Sort: {arr}')

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
        display_array(arr, f'Merge Sort: {arr}')

def merge_sort_visualizer(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2
        merge_sort_visualizer(arr, left, mid)
        merge_sort_visualizer(arr, mid + 1, right)
        merge(arr, left, mid, right)

# Quick Sort with visualization
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
            display_array(arr, f'Quick Sort: {arr}')
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap
    display_array(arr, f'Quick Sort: {arr}')
    return i + 1

def quick_sort_visualizer(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_visualizer(arr, low, pi - 1)
        quick_sort_visualizer(arr, pi + 1, high)

# Heap Sort with visualization
def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        display_array(arr, f'Heap Sort: {arr}')
        heapify(arr, n, largest)

def heap_sort_visualizer(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Swap
        display_array(arr, f'Heap Sort: {arr}')
        heapify(arr, i, 0)

# Cycle Sort with visualization
def cycle_sort_visualizer(arr):
    n = len(arr)
    for cycle_start in range(n - 1):
        item = arr[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == arr[pos]:
            pos += 1
        if pos != cycle_start:
            arr[pos], item = item, arr[pos]  # Swap
            display_array(arr, f'Cycle Sort: {arr}')
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            if item != arr[pos]:
                arr[pos], item = item, arr[pos]  # Swap
                display_array(arr, f'Cycle Sort: {arr}')

# Sample array to sort
arr = [9, 5, 3, 8, 6, 4, 7, 2, 1]

# Create a single figure for visualization
plt.figure(figsize=(10, 6))  # Optional: Set the size of the figure

# Enable interactive mode for real-time plotting
plt.ion()

# Choose the sorting algorithm to visualize
# Uncomment the sorting algorithm you want to visualize:
# bubble_sort_visualizer(arr.copy())
# insertion_sort_visualizer(arr.copy())
# selection_sort_visualizer(arr.copy())
merge_sort_visualizer(arr.copy(), 0, len(arr) - 1)
# quick_sort_visualizer(arr.copy(), 0, len(arr) - 1)
# heap_sort_visualizer(arr.copy())
# cycle_sort_visualizer(arr.copy())

plt.ioff()  # Turn off interactive mode
plt.show()  # Show the final sorted array

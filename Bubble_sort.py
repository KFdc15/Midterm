# Sắp xếp mảng bằng thuật toán Bubble Sort
n = int(input("Nhập số lượng phần tử của mảng: "))
arr = []
print("Nhập các phần tử của mảng:")
for i in range(n):
    arr.append(int(input()))    
print("Mảng trước khi sắp xếp:")
print(arr)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
print("Mảng sau khi sắp xếp:")
print(bubble_sort(arr))

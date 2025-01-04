import random

def merge(a, left, mid, right, process_logs, iteration):
    merge_log = []
    n1 = mid - left + 1
    n2 = right - mid

    l = [0] * n1
    r = [0] * n2

    for i in range(n1):
        l[i] = a[left + i]
    for j in range(n2):
        r[j] = a[mid + 1 + j]

    i, j, k = 0, 0, left

    while i < n1 and j < n2:
        if l[i] <= r[j]:
            a[k] = l[i]
            i += 1
        else:
            a[k] = r[j]
            j += 1
        k += 1

    while i < n1:
        a[k] = l[i]
        i += 1
        k += 1

    while j < n2:
        a[k] = r[j]
        j += 1
        k += 1
    
    merge_log.append(f"Merged: {' '.join(map(str, a[left:right + 1]))}")
    process_logs["Proses Sorting"].extend(merge_log)

def mergeSort(a, left, right, process_logs, iteration=[1]):
    if left < right:
        mid = (left + right) // 2
        
        divide_log = []
        divide_log.append(f"\nIterasi ke-{iteration[0]}:")
        divide_log.append(f"Array pembagi: {' '.join(map(str, a[left:right + 1]))}")
        divide_log.append(f"Array bagian kiri: {' '.join(map(str, a[left:mid + 1]))}")
        divide_log.append(f"Array bagian kanan: {' '.join(map(str, a[mid + 1:right + 1]))}")
        process_logs["Proses Sorting"].extend(divide_log)
        
        iteration[0] += 1
        mergeSort(a, left, mid, process_logs, iteration)
        mergeSort(a, mid + 1, right, process_logs, iteration)
        merge(a, left, mid, right, process_logs, iteration)

def mergeSortMain(n):
    process_logs = {
        "Inisialisasi": [],
        "Proses Sorting": [],
        "Hasil Akhir": []
    }
    
    # Generate random array
    a = [random.randint(1, 100) for _ in range(n)]
    process_logs["Inisialisasi"].append(f"Array Awal: {' '.join(map(str, a))}")
    
    # Jalankan merge sort
    mergeSort(a, 0, n-1, process_logs)
    process_logs["Hasil Akhir"].append(f"\nArray Terurut: {' '.join(map(str, a))}")
    
    return process_logs
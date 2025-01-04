import random

def counting(n):
    process_logs = {
        "Inisialisasi": [],
        "Pencarian Maksimum": [],
        "Perhitungan Frekuensi": [],
        "Perhitungan Frekuensi Kumulatif": [],
        "Pengurutan": []
    }
    
    # Step 1: Inisialisasi array
    a = [random.randint(1, 100) for _ in range(n)]
    process_logs["Inisialisasi"].append(f"Array Awal: {' '.join(map(str, a))}")
    
    # Step 2: Finding max element
    max_steps = []
    key = a[0]
    max_steps.append(f"Elemen maksimum awal: {key}")
    for i in range(1, n):
        max_steps.append(f"Iterasi ke-{i}: membandingkan {a[i]} dengan {key}")
        if a[i] > key:
            key = a[i]
            max_steps.append(f"Elemen maksimum baru: {key}")
        else:
            max_steps.append("Tidak ada perubahan elemen maksimum")
    max_steps.append(f"Elemen maksimum dalam array adalah: {key}")
    process_logs["Pencarian Maksimum"].extend(max_steps)
    
    # Step 3: Counting frequency
    freq = [0] * (key + 1)
    freq_steps = []
    freq_steps.append("Menghitung frekuensi kemunculan setiap elemen:")
    for i in range(n):
        freq[a[i]] += 1
    for idx in sorted(set(a)):
        freq_steps.append(f"Elemen {idx} muncul sebanyak {freq[idx]} kali")
    process_logs["Perhitungan Frekuensi"].extend(freq_steps)
    
    # Step 4: Counting cumulative frequency
    cum_freq_steps = []
    cum_freq_steps.append("Menghitung posisi akhir setiap elemen (frekuensi kumulatif):")
    for i in range(1, len(freq)):
        freq[i] += freq[i - 1]
    for idx in sorted(set(a)):
        cum_freq_steps.append(f"Elemen {idx} memiliki posisi akhir kumulatif {freq[idx]}")
    process_logs["Perhitungan Frekuensi Kumulatif"].extend(cum_freq_steps)
    
    # Step 5: Sorting
    sorted_a = [0] * n
    sorting_steps = []
    sorting_steps.append("Menempatkan elemen pada array terurut:")
    for i in range(n - 1, -1, -1):
        pos = freq[a[i]] - 1
        sorted_a[pos] = a[i]
        freq[a[i]] -= 1
        sorting_steps.append(f"Elemen {a[i]} ditempatkan pada posisi ke-{pos+1}")
    sorting_steps.append(f"\nArray Terurut: {' '.join(map(str, sorted_a))}")
    process_logs["Pengurutan"].extend(sorting_steps)
    
    return process_logs
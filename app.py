import streamlit as st
from counting import counting
from merge import mergeSortMain

def main():
    st.title("Comparison and Non-Comparison Based Sorting Algorithms Technique")
    
    st.header("A. Non-Comparison Based Sorting Algorithms")
	# counting sort
    st.subheader("1. Counting Sort")
    st.write("Counting Sort adalah algoritma pengurutan berbasis pencacahan yang bekerja dengan menghitung frekuensi kemunculan setiap elemen pada array input. Algoritma ini ideal untuk data integer dengan rentang nilai yang terbatas. Selain itu, kelebihan dari algoritma ini adalah sangat cepat untuk rentang nilai kecil dan tidak memerlukan perbandingan besar. Akan tetapi, kekurangan dari algoritma ini adalah tidak efisien untuk data dengan rentang data yang besar. Adapun pseudocode dari algoritma ini adalah:")
    st.code("""
    COUNTING-SORT(A, n, k)
    let B[i:n] and C[0:k] be new arrays
    for i = 0 to k:
        C[i] = 0
    for j = 1 to n:
        C[A[j]] = C[A[j]] + 1
    // C[i] now contains the number of elements equal to i
    for i = 1 to k:
        C[i] = C[i] + C[i-1]
    // C[i] now contains the number of elements less than or equal to i
    // Copy A to B, starting from the end of A
    for j = n downto 1:
        B[C[A[j]]] = A[j]
        C[A[j]] = C[A[j]] - 1 // to handle duplicate elements
    return B
	""")
    
    if 'step' not in st.session_state:
        st.session_state.step = 0
        
    if st.button("Jalankan Counting Sort"):
        st.session_state.step = 1

    if st.session_state.step == 1:
        n = st.number_input("Masukkan jumlah data:", min_value=1, step=1, value=5)
        if st.button("OK"):
            process_logs = counting(int(n))
            
            st.subheader("Tahapan Proses Counting Sort:")
            for step_name, logs in process_logs.items():
                with st.expander(step_name):
                    for log in logs:
                        st.write(log)
            st.session_state.step = 0
    
    st.header("B. Comparison Based Sorting Algorithms")
    # merge sort
    st.subheader("1. Merge Sort")
    st.write("Merge Sort adalah algoritma sorting berbasis divide and conquer. Algoritma ini membagi array menjadi dua bagian, menyortir masing-masing bagian secara rekursif, lalu menggabungkannya kembali dalam urutan yang benar. Adapun pseudocode dari algoritma ini adalah:")
    st.code("""
    MERGE-SORT(A[0...n-1])
    if n > 1:
        copy A[0...n/2-1] to B[0...n/2-1]
        copy A[n/2...n-1] to C[0...n/2-1]
        Merge-Sort(B[0...n/2-1])
        Merge-Sort(C[0...n/2-1])
        Merge(B, C, A)
    """)
    st.code("""
    Merge(B[0...p-1], C[0...q-1], A[0...p+q-1])    
    i <- 0, j <- 0, k <- 0
    while i < p and j < q:
        if B[i] <= C[j]:
            A[k] <- B[i]
            i <- i + 1
        else:
            A[k] <- C[j]
            j <- j + 1
        k <- k + 1
    if i = p:
        copy C[j...q-1] to A[k...p+q-1]
    else:
        copy B[i...p-1] to A[k...p+q-1]
    """)
    
    if st.button("Jalankan Merge Sort"):
        st.session_state.step = 3

    if st.session_state.step == 3:
        n = st.number_input("Masukkan jumlah data:", min_value=1, step=1, value=5)
        if st.button("OK"):
            process_logs = mergeSortMain(int(n))
            
            st.subheader("Tahapan Proses Merge Sort:")
            for step_name, logs in process_logs.items():
                with st.expander(step_name):
                    for log in logs:
                        st.write(log)
            
            st.session_state.step = 0

            		
if __name__ == "__main__":
    main()
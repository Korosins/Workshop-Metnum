import numpy as np

def buat_matriks_manual(nama_matriks):

    print(f"\n--- Masukkan Nilai untuk {nama_matriks} ---")
    
    while True:
        try:
            baris = int(input(f"Jumlah baris {nama_matriks}: "))
            kolom = int(input(f"Jumlah kolom {nama_matriks}: "))
            
            if baris <= 0 or kolom <= 0:
                print("Jumlah baris dan kolom harus positif. Coba lagi.")
                continue

            data = []
            print(f"Masukkan {baris * kolom} elemen matriks, baris demi baris.")
            print("Pisahkan angka dalam satu baris dengan SPASI (contoh: 1 2 3)")
            
            for i in range(baris):
                while True:
                    input_baris = input(f"Baris ke-{i+1}: ").split()
                    
                    if len(input_baris) != kolom:
                        print(f"ERROR: Harus memasukkan {kolom} angka. Coba lagi untuk baris ini.")
                    else:
                        baris_angka = [int(x) for x in input_baris]
                        data.append(baris_angka)
                        break
                        
            return np.array(data)
        
        except ValueError:
            print("\n!!! ERROR: Input tidak valid. Pastikan semua input adalah angka (integer) dan spasi.\n")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

print("--- Kalkulator Penjumlahan & Pengurangan Matriks ---")

A = buat_matriks_manual("Matriks A")

while True:
    B = buat_matriks_manual("Matriks B")
    
    if A.shape == B.shape:
        break
    else:
        print("\n!!! ERROR: Kedua Matriks HARUS memiliki dimensi yang sama untuk Penjumlahan/Pengurangan.")
        print(f"Matriks A: {A.shape} | Matriks B: {B.shape}. Silakan masukkan Matriks B lagi.")

print("\n--- Pilih Operasi ---")
while True:
    pilihan = input("Pilih operasi (Ketik 'J' untuk Penjumlahan, 'P' untuk Pengurangan,'K' untuk perkalian): ").upper()
    
    if pilihan == 'J':
        hasil = A + B
        operator = "+"
        break
    elif pilihan == 'P':
        hasil = A - B
        operator = "-"
        break
    elif pilihan == 'K':
        hasil = A * B
        operator = "*"
        break
    else:
        print("Pilihan tidak valid. Silakan ketik 'J' atau 'P'.")

print("\n" + "="*45)
print("HASIL OPERASI MATRIKS")
print("="*45)

print("\nMatriks A:")
print(A)
print(f"\nMatriks B (Operator {operator}):")
print(B)

print("\nHasil Akhir:")
print(hasil)

print("="*45)

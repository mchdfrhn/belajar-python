import math

def hitung_luas_alas_tinggi(alas, tinggi):
  """
  Menghitung luas segitiga berdasarkan panjang alas dan tingginya.

  Args:
    alas (float): Panjang alas segitiga.
    tinggi (float): Tinggi segitiga.

  Returns:
    float: Luas segitiga.
  """
  if alas <= 0 or tinggi <= 0:
    return "Input alas dan tinggi harus positif."
  luas = 0.5 * alas * tinggi
  return luas

# Contoh penggunaan:
luas_contoh = hitung_luas_alas_tinggi(10, 5)
print(f"Luas segitiga dengan alas 10 dan tinggi 5 adalah: {luas_contoh}")

def hitung_luas_lingkaran(jari_jari):
  """
  Menghitung luas lingkaran berdasarkan jari-jarinya.

  Args:
    jari_jari (float): Panjang jari-jari lingkaran.

  Returns:
    float: Luas lingkaran.
  """
  if jari_jari <= 0:
    return "Jari-jari harus bernilai positif."

  # Rumus: Luas = π * r^2
  luas = math.pi * (jari_jari ** 2)
  return luas

# Contoh penggunaan:
r1 = 7
luas_contoh = hitung_luas_lingkaran(r1)
print(f"Luas lingkaran dengan jari-jari {r1} adalah: {luas_contoh:.2f}") # Dibulatkan 2 desimal
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
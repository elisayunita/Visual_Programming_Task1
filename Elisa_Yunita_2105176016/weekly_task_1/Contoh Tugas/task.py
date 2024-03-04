class mahasiswa():
	def __init__ (self, masukkan_nama, masukkan_kelas, masukkan_prodi, masukkan_fakultas, masukkan_tempat_tinggal, masukkan_asal):
		self.nama = masukkan_nama
		self.kelas = masukkan_kelas
		self.prodi = masukkan_prodi
		self.fakultas = masukkan_fakultas
		self.tempattinggal = masukkan_tempat_tinggal
		self.asal = masukkan_asal
objek = mahasiswa("Elisa Yunita", "A", "Pendidikan Komputer", "Keguruan dan Ilmu Pendidikan", "Pramuka 6", "Balikpapan")
print ("Data Diri :")
print ("Nama : ", objek.nama)
print ("Kelas : ", objek.kelas)
print ("Prodi : ", objek.prodi)
print ("Fakultas : ", objek.fakultas)
print ("Tempat Tinggal : ", objek.tempattinggal)
print ("Asal : ", objek.asal)
 


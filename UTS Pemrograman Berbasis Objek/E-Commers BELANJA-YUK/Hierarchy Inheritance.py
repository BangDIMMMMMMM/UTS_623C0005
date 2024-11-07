class User: # Kelas dasar User
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

    def login(self):
        print(f"Pengguna {self.username} dengan email {self.email} berhasil login.")

    def logout(self):
        print(f"Pengguna {self.username} berhasil logout.")

class Seller(User): # Kelas turunan Seller dari User
    def addProduct(self, productName, description, price, stock):
        print(f"Produk baru '{productName}' ditambahkan dengan deskripsi '{description}', harga {price}, stok awal {stock}.")

    def processOrder(self, orderId, status):
        print(f"Pesanan dengan ID {orderId} diproses dengan status: {status}.")


class Admin(User): # Kelas turunan Admin dari User
    def removeUser(self, userId):
        print(f"Pengguna dengan ID {userId} telah dihapus dari sistem.")

    def generateReport(self, reportType, startDate, endDate):
        print(f"Menghasilkan laporan tipe '{reportType}' dari tanggal {startDate} sampai {endDate}.")

seller = Seller("Tokobaru", "tokobaru@busines.co.id", 201) # Membuat objek pengguna dengan peran Seller dan Admin
admin = Admin("Admin001", "admin01@belanjayuk.co.id", 301)

seller.login() # Fitur Seller
seller.addProduct("Laptop", "Laptop gaming dengan spesifikasi tinggi", 15000000, 5)
seller.processOrder("O1001", "dalam pengiriman")
seller.logout()

admin.login() # Fitur Admin
admin.removeUser(201)
admin.generateReport("transaksi", "2024-01-01", "2024-11-07")
admin.logout()

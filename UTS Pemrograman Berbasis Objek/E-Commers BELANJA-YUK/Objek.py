class User: # Kelas dasar User
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

    def login(self):
        print(f"Pengguna {self.username} dengan email {self.email} berhasil login.")

    def logout(self):
        print(f"Pengguna {self.username} berhasil logout.")

class BasicUser(User):# Kelas turunan pertama dari User: BasicUser
    def viewProduct(self, productId):
        print(f"Menampilkan informasi produk dengan ID: {productId}.")

    def addToCart(self, productId, quantity):
        print(f"Menambahkan produk ID {productId} sejumlah {quantity} ke keranjang.")

class PremiumUser(BasicUser): 
# Kelas turunan kedua dari BasicUser: PremiumUser
    def applyVoucher(self, voucherCode, cartTotal):
        print(f"Menerapkan voucher {voucherCode} pada total belanja {cartTotal}.")

    def requestPrioritySupport(self, issueDescription):
        print(f"Menghubungi dukungan prioritas dengan masalah: {issueDescription}.")

class Seller(User):# Kelas turunan Seller dari User
    def addProduct(self, productName, description, price, stock):
        print(f"Produk baru '{productName}' ditambahkan dengan deskripsi '{description}', harga {price}, stok awal {stock}.")

    def processOrder(self, orderId, status):
        print(f"Pesanan dengan ID {orderId} diproses dengan status: {status}.")

premium_user = PremiumUser("Buddy-Anduk", "buddy22@example.com", 111) # Objek PremiumUser
premium_user.viewProduct("PL032")
premium_user.addToCart("PL032", 3)
premium_user.applyVoucher("VIPDISCOUNT", 250000)
premium_user.requestPrioritySupport("Produk Hilang saat diperjalanan.")

seller = Seller("sellerPro", "seller@example.com", 202) # Objek Seller
seller.addProduct("Smartphone", "IPHONE 16", 35000000, 20)
seller.processOrder("O2002", "selesai")
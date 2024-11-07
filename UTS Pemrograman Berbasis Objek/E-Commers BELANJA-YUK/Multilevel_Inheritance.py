class User: # Kelas dasar User
    def __init__(self, username, email, userId):
        self.username = username
        self.email = email
        self.userId = userId

    def login(self):
        print(f"Pengguna {self.username} dengan email {self.email} berhasil login.")

    def logout(self):
        print(f"Pengguna {self.username} berhasil logout.")

class BasicUser(User): # Kelas turunan pertama dari User: BasicUser
    def viewProduct(self, productId):
        print(f"Menampilkan informasi produk dengan ID: {productId}.")

    def addToCart(self, productId, quantity):
        print(f"Menambahkan produk ID {productId} sejumlah {quantity} ke keranjang.")

class PremiumUser(BasicUser): # Kelas turunan kedua dari BasicUser: PremiumUser
    def applyVoucher(self, voucherCode, cartTotal):
        print(f"Menerapkan voucher {voucherCode} pada total belanja {cartTotal}.")

    def requestPrioritySupport(self, issueDescription):
        print(f"Menghubungi dukungan prioritas dengan masalah: {issueDescription}.")

premium_user = PremiumUser("Dimas", "dimas@student.mahardika.ac.id", 101) # Membuat objek pengguna Premium

premium_user.login()
premium_user.logout()

premium_user.viewProduct("PB1") # Fitur BasicUser
premium_user.addToCart("PB1", 2)

premium_user.applyVoucher("DISKON11", 100000) # Fitur PremiumUser
premium_user.requestPrioritySupport("Produk tidak terkirim.")
class BeautyProduct:
    def __init__(self, product_type):
        self.product_type = product_type
        self.details = self.create_product()

    def create_product(self):
        if self.product_type.lower() == "lipstick":
            return {
                "name": "Matte Lipstick Super",
                "color": "Rum Raisin",
                "price": "Rp 89.000",
                "description": "Lipstick matte dengan warna tahan lama dan tahan banting."
            }
        elif self.product_type.lower() == "skintint":
            return {
                "name": "Skintint Glow Tint",
                "shade" : "Light Beige, Warm Honey, Neutral Olive, Deep Tan",
                "price": "Rp 105.000",
                "description": "Skintint dengan efek glowing dan ringan di wajah."
            }
        else:
            return None

    def show_details(self):
        if self.details:
            print("\nDetail Produk Kecantikan")
            for key, value in self.details.items():
                print(f"{key.capitalize()}: {value}")
        else:
            print("\nJenis produk tidak dikenal. Pilih 'Lipstick' atau 'Skintint'.")


# Main program
product_type = input("Jenis produk kecantikan apa yang ingin Anda buat? "
                     "\n[Lipstick atau Skintint]: ")
product = BeautyProduct(product_type)
product.show_details()
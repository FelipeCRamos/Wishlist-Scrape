class ProductModel:
    def __init__(
            self,
            title = '',
            price = 0.0,
            hasDiscount = False,
            hasError = False,
            isIndisponible = False
    ):
        self.title = title
        self.price = price
        self.hasDiscount = hasDiscount
        self.hasError = hasError
        self.isIndisponible = isIndisponible


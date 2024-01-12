class Furniture:
    def __init__(self, color, texture, size):
        self.color = color
        self.texture = texture
        self.size = size

    def customize(self, new_color, new_texture, new_size):
        # Code for customizing furniture
        self.color = new_color
        self.texture = new_texture
        self.size = new_size
        print("Furniture customized successfully!")

# Example usage
my_furniture = Furniture(color="brown", texture="wood", size="medium")
my_furniture.customize(new_color="white", new_texture="leather", new_size="large")

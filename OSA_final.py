print("Question 1")
# 1.1
# #Sample of farmers from provided farmers dataset

farmers = [
    {"farmer_id": "SA001", "name": "Sipho Ndlovu", "province": "KwaZulu-Natal",
    "hectares": 3.5, "crops": ["maize", "soya beans", "sunflower"],
    "annual_yield_kg": {"maize": 4200, "soya beans": 1800, "sunflower": 900}},

    {"farmer_id": "SA002", "name": "Thandiwe Mokoena", "province": "Limpopo",
    "hectares": 1.2, "crops": ["tomatoes", "spinach"],
    "annual_yield_kg": {"tomatoes": 6500, "spinach": 3200}},

    {"farmer_id": "SA003", "name": "Lungelo Zulu", "province": "Eastern Cape",
    "hectares": 8.0, "crops": ["potatoes", "onions", "butternut"],
    "annual_yield_kg": {"potatoes": 12000, "onions": 8400, "butternut": 5100}}
]

def classify_famer(hectares):
    if hectares < 2:
        return "subsistance"
    elif hectares <=5:
        return "smallholder"
    else:
        return "commercial"
    
for farmer in farmers:
    classification = classify_famer(farmer["hectares"])
    print(f"\n{farmer['name']} is classified under: {classification}")


# #new modified funtion to accomodate new added categories

def classify_farmer(hectares):
    if hectares < 2:
        return "subsistence"
    elif hectares <= 5:
        return "smallholder"
    elif hectares < 10:
        return "Emerging Commercial"
    else:
        return "Large Commercial"
print("-" * 50)    

print("\nQuestion 2")
# 2.1
#iterates through the farmers list using a for loop and prints the following summary 
#for each farmer: the farmer's name, their province, the total number of crops registered, and their total annual yield across all crops

for farmer in farmers:
    total_yield = sum(farmer["annual_yield_kg"].values())
    total_crops = len(farmer["crops"])

    print(f"\nName: {farmer['name']}")
    print(f"Province: {farmer['province']}")
    print(f"Total crops registered: {total_crops}")
    print(f"total annual yield: {total_yield} kg")
    print(f"-" * 50)

# 2.2 a dictionary is prefered as it stores each crop name as a key and its yield as a value. making it easier to look up yield for a specific crop from the list
# we dont wan to use a list because a list only stores values in order.

# 2.3
# #accepts a single farmer dictionary as its argument and returns the name of the crop with the highest annual yield for that farmer

def get_top_crop(farmer):
    top_crop = None
    highest_yield = -1
    #loop through each crop and its yield

    for crop, yield_kg in farmer["annual_yield_kg"].items():
        #update top crop if this crop has a higher yield
        highest_yield = yield_kg
        top_crop = crop
    
    return top_crop, highest_yield

for farmer in farmers:
    crop_name, yield_kg = get_top_crop(farmer)
    print(f"{farmer['name']}'s highest yielding crop is: {crop_name} with {yield_kg} kg")

print("Question 3")
#3.1

# #validation module, the farmer registration process using a while loop to repeatedly prompt a user to enter a farmer's name, province
# #validate: (i) that the name field is not empty; (ii) that the province entered is in the predefined list; and (iii) that the hectares value is a positive number greater than zero.

valid_provinces = ["KwaZulu-Natal", "Limpopo", "Eastern Cape", "Gauteng", "Western Cape"]
registrations = []

while True:
    name = input("Enter farmer name (or type 'done' to finish): ").strip()
    if name.lower() == "done":
        break
    if name == "":
        print("Error: Name cannot be empty.")
        continue

    province = input("Enter province: ").strip()
    while province not in valid_provinces:
        print("Error: Province must be one of the predefined provinces.")
        province = input("Enter province: ").strip()

    hectares_input = input("Enter hectares: ").strip()
    while True:
        try:
            hectares = float(hectares_input)
            if hectares > 0:
                break
            else:
                print("Error: Hectares must be greater than zero.")
        except ValueError:
            print("Error: Hectares must be a valid number.")
        hectares_input = input("Enter hectares: ").strip()

    registration = {
        "name": name,
        "province": province,
        "hectares": hectares
    }
    registrations.append(registration)
    print("Farmer registered successfully.")

print("All registrations:", registrations)


#

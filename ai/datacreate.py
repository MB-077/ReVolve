import csv
import random

# Dictionary of materials and their specific grades
material_grades = {
    "steel": ["101", "201", "301"],
    "titanium": ["grade1", "grade2", "grade5"],
    "aluminium": ["6061", "7075", "5052"],
    "copper": ["C101", "C110", "C122"],
    "brass": ["360", "260", "230"],
    "stainless steel": ["304", "316", "410"],
    "lead": ["99.99% pure", "99.7% pure"],
    "zinc": ["SHG", "HG", "LME"],
    "tin": ["99.9% pure", "99.85% pure", "99.7% pure"],
    "iron": ["cast iron", "wrought iron"],
    "magnesium": ["AZ31", "AZ61", "AZ91"],
    "tungsten": ["grade1","grade2","grade5"]
}

# List of shapes
shapes = ["bar", "billet", "plate", "sheet", "bars", "billets", "plates", "sheets", "bloom", "blooms", "rod", "rods"]


# Individual random words
random_words = [
    "I", "i", "want", "to", "buy", "Please", "provide", "Can", "you", "get", "me", 
    "Looking", "for", "Interested", "in", "Need", "looking", "searching", 
    "seeking", "wishing", "requesting", "inquiring", "more", "extra", "additional",
    "additional", "another", "some", "few", "other", "different", "various", "many", 
    "hello", "hey", "thank", "thanks", "help", "support", "assist", "assistance",
    "require", "requirement", "needful", "seek", "seeker", "quest", "seeking",
    "wanting", "desire", "interested", "inquisitive", "curious", "yearn", "wish",
    "wishful", "hope", "hopeful", "hopefulness", "wishfulness", "request", "demand",
    "ask", "plead", "asker", "askance", "pleasing", "pleasure", "solicit", "requester",
    "additional", "extra", "added", "supplemental", "addedly", "moreover", "furthermore",
    "likewise", "similarly", "also", "similar", "resemble", "resemblance", "akin", 
    "comparable", "comparison", "parallel", "parallelism", "correspond", "correspondence",
    "hello", "hi", "greeting", "salutation", "hey", "hullo", "howdy", "how", "are", 
    "your", "my", "is", "can", "could", "may", "might", "would", "shall",
    "should", "must", "ought", "sure", "definitely", "absolutely", "certainly", "indeed",
    "undoubtedly", "positively", "okay", "fine", "good", "great", "excellent", "wonderful",
    "fantastic", "superb", "awesome", "terrific", "marvelous", "fabulous", "outstanding", "Grade" , "grade", "please"
]

# Function to generate random tokens and labels
def generate_data(num_samples):
    data = []
    for _ in range(num_samples):
        # Randomly select material and shape
        material = random.choice(list(material_grades.keys()))
        # Randomly select grade for the selected material
        grade = random.choice(material_grades[material])
        shape = random.choice(shapes)
        
        # Randomly generate 3D dimensions
        length = random.randrange(1, 1000)
        width = random.randrange(1, 1000)
        thickness = random.randrange(1, 40)
        
        
        num = random.randint(1, 2000)
        word = []
        #Randomly generate words
        for i in range(random.randint(1, 150)):
            word.append(random.choice(random_words))
        # Combine material, grade, dimensions, and shape
        token = f"'{material}', '{grade}', '{num}','{width}x{length}x{thickness}', '{shape}'," + ', '.join(f"'{w}'" for w in word)
        label = "'Metal', 'Grade', 'Quantity', 'Dimensions', 'Shape',"+ ', '.join("'O'" for _ in word)
        
        data.append((token, label))
    
    return data

# Generate data
num_samples = 5000
data = generate_data(num_samples)

# Write data to CSV file
# with open("tagging_data.csv", "w", newline="") as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(["Token_list", "Label_list"])
#     for row in data:
#         writer.writerow([row[0], row[1]])

# Write data to CSV file
with open("tagging_data.csv", "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Token_list", "Label_list"])
    for row in data:
        token_list = "(" + row[0] + ")"
        label_list = "(" + row[1] + ")"
        writer.writerow([token_list, label_list])

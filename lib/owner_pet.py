class Pet:
    pass
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]

    all = []

    def __init__(self, name, pet_type, owner=None ):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type '{pet_type}'. Allowed types: {Pet.PET_TYPES}")
        
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner,Owner):
            raise Exception("owner must be an instance of Owner class or None")
        self.owner = owner
    
        Pet.all.append(self) 

class Owner:
    def __init__(self, name):
        self.name = name
    pass
    def pets(self):
        "Returns a list of all Pet instances where this owner is assigned."
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        "Assigns this owner to the given pet after validating type."
        if not isinstance(pet, Pet):
            raise TypeError("pet must be an instance of Pet class")
        
        pet.owner = self

    def get_sorted_pets(self):
        "Returns a list of pets sorted alpabeticallly by their name."
        def get_pet_name(pet):
            return pet.name
        return sorted(self.pets(), key=get_pet_name)   


owner1 = Owner ("John")
pet1 = Pet("Fido", "dog", owner1 )



print(owner1.name)
print(pet1.name)       
print(pet1.pet_type)   
print(pet1.owner.name)
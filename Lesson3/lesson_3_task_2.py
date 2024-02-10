from smartphone import Smartphone

catalog = []

def add_to_list(smart):
     global catalog
     smart = str(smart)
     catalog.append(smart)



smartphone1 = Smartphone('Nokia', 'Lumia 930', '+7914705963')
smartphone2 = Smartphone('Siemens', 'M55', '+79659933388')
smartphone3 = Smartphone('Panasonic', 'GD-93', '+79142701723')
smartphone4 = Smartphone('HTC', 'Desire', '+79142705962')
smartphone5 = Smartphone('Samsung', 'Galaxy R', '+79227032530')

add_to_list(smartphone1)
add_to_list(smartphone2)
add_to_list(smartphone3)
add_to_list(smartphone4)
add_to_list(smartphone5)

def print_catalog():
     for i in catalog:
          print(i)

print_catalog()
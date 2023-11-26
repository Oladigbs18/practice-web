def hypothenuse(adjacent, opposite):
    hypothenuse = (adjacent**2 + opposite**2)**0.5
    return hypothenuse

hypothenuse(3, 4)


# a function that modifies a list passed in as a argument
def fruits(fruit_list):
    fruit_list.append("banana") # modifies the list by adding a new element to the end of the list
    return fruit_list

# a list of fruits
fruit_list = ["apple", "orange", "strawberry"]
fruits(fruit_list)
print(fruit_list)

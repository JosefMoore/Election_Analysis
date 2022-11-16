name = "bob"
country = "usa"
age = 55
hourly_wage = 5
satisfied = False
daily_wage = hourly_wage * 8

print("I'm " + str(name) + " from " + str(country) + ". I am " + str(age) +
" and I make " + str(hourly_wage) + " dollars an hour.")

print(f"I make {daily_wage} a day. Am I satisfied?: {satisfied}")



grocery_list = ['Milk',
                'Bread',
                'Eggs',
                'Peanut Butter',
                'Jelly']

grocery_list[3] = 'Almond Butter'
grocery_list.remove('Jelly')
grocery_list.append('Coffee')

print(grocery_list)



my_pet = {"name": "Cleo",
           "age": 2,
           "hobbies": ["pooping", "sleeping", "fetch"],
           "wake-up": {"Monday": 6, "Tuesday": 6, "Wednesday": 8}}

print(f'Hello I am {my_pet["name"]} and I am a {my_pet["age"]} years old.')
print(f'I have {len(my_pet["hobbies"])} hobbies!')
print(f'One of my favorite hobbies is {my_pet["hobbies"][0]}.')
print(f'On Saturday I get up at {my_pet["wake-up"]["Monday"]} AM.')

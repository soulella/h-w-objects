#Task_2
# https://edabit.com/challenge/ff2R7SymbB6PfjpPm
budjet =[
    {"Name": "John", "age": 21, "Budjet":23000 },
    {"Name": "Steve", "age": 32, "Budjet":40000 },
    {"Name": "martin", "age": 16, "Budjet":2700 }
]
result = 0

def relation_to_luke(budjet, result):
    for item in budjet:
        result += item["Budjet"]
    print(result)

relation_to_luke(budjet, result)


#Task_3
# https://edabit.com/challenge/HvkPdhijquecKASdF
names = {
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}
result = []
def get_student_names(names, result):
    for value in names.values():
        result.append(value)
        result.sort()
    print(result)

get_student_names(names, result)


#Task_4
# https://edabit.com/challenge/cH5ce3f4QgnreDW4v
scores = [
  { "tile": "N", "score": 1 },
  { "tile": "K", "score": 5 },
  { "tile": "Z", "score": 10 },
  { "tile": "X", "score": 8 },
  { "tile": "D", "score": 2 },
  { "tile": "A", "score": 1 },
  { "tile": "E", "score": 1 }
]
result = 0

def maximum_score(scores , result):
    for items in scores:
        for x in items.values():
            item = items['score']
        result += item
    print(result)


maximum_score(scores , result)


#Task_6
# https://edabit.com/challenge/pimnBHXJNtQffq4Cf
lst = ["d", "a"]
result = {

}
def mapping(lst):
    for x in lst:
        l = x.lower()
        n = x.upper()
        result[l] = n
    print(result)

mapping(lst)


# #Task_7
# https://edabit.com/challenge/KEz3TAQfh9WxSZMLH
word = input("Enter the letter and number:")
answer = {"Letters": 0 , "Digits": 0}

def count_all(word, answer):
    for x in word:
        if x.isalpha():
            answer["Letters"] += 1
        if x.isdigit():
            answer["Digits"] += 1
    print(answer)
count_all(word, answer)



# #Task_8
# https://edabit.com/challenge/PTh7tBusAZRgjAWEZ
num = int(input("Enter the number:"))
all_cost = {"skate": 200, "painting": 200, "shoes": 1 }
result = 0

def calc_diff(num , all_cost , result):
    for item in all_cost.values():
        result += item
    print(result-num)


calc_diff(num , all_cost , result)




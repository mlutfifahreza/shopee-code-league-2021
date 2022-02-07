import json

class HealthADay:
    def __init__(self, partial_left, partial_right, full_left, full_right):
        self.partial_left = left
        self.partial_right = right
        self.full_left = full_left
        self.full_right = full_right

# INPUT DATA
mock_input_bool = True
input_data = {}
if (mock_input_bool):
    # Opening JSON file
    with open('p1_shopee_tanam.json') as json_file:
        input_data = json.load(json_file)
else:
    print("n_test_cases : ")
    n_test_cases = int(input())
    # convert to dictionary
    input_data["n_test_cases"] = n_test_cases
    input_data["items"] = []
    for i in range(n_test_cases):
        # input n_days and n_cells
        print("n_days, n_cells : ")
        n_days, n_cells = [ int(x) for x in input().split()]
        # input fruit health for each days
        fruit_healths = []
        for n_day in range(n_days):
            print("fruit health : ")
            fruit_health = [ int(x) for x in input().split()]
            fruit_healths.append(fruit_health)
        # convert to dictionary
        item = {
            "n_days" : n_days,
            "n_cells" : n_cells,
            "fruit_healths" : fruit_healths
        }
        input_data["items"].append(item)

print(json.dumps(input_data, indent=2))

# GENERATE OUTPUT
results = []
for item in input_data["items"]:
    health_a_days = []
    for i in range(item["n_days"]):
        for j in range(item["n_cells"]):
            continue
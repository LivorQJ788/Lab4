import json
def task() -> float:
    sum = 0
    with open('input.json') as file:
        parse_json_dict = json.load(file)

    for temp in parse_json_dict:
        sum+= temp['score'] * temp['weight']

    return round(sum, 3);

print(task())
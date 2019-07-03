from collections import namedtuple

Result = namedtuple('Result', 'count, average')

def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term == None:
            break
        total += term
        count += 1
        average = total / count
    return Result(count, average)

def grouper(result, key):
    while True:
        result[key] = yield from averager()

def main(data):
    results = {}
    for key, values in data.items():
        group = grouper(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)

    print(results)

data = {
    'girls':
        [40.9, 38.5, 44.3, 42.2, 45.2, 41.7],
    'boys':
        [39.0, 40.8, 43.2, 40.8]
}

if __name__ == '__main__':
    main(data)

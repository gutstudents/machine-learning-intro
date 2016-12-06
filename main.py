from csv import reader

def load_csv(filename):
    dataset = list()
    with open(filename,"r") as file:
        csv_reader = reader(file)
        for row in csv_reader:
            if not row:
                continue
            dataset.append(row)
    return dataset

def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

def str_column_to_int():
    class_values = [row[column] for row in dataset]
    unique = set(class_values)
    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = 1
    for row in dataset:
        row[column] = lookup[row[column]]
        return lookup


# Load dataset
filename = './pima-indians-diabetes.csv'
dataset = load_csv(filename)
print('Loaded data file {0} with {1} rows and {2} columns.'.format(filename,len(dataset),len(dataset[0])))

for i in range(len(dataset[0])):
    str_column_to_float(dataset,i)
print(dataset[9])
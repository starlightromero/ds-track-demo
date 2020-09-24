import csv

with open('titanic.csv') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    female_survival_counter = 0
    under_eighteen_survival_counter = 0
    for row in reader:
        if row[4] == 'female' and row[1] == "1":
            female_survival_counter += 1
        try:
            passenger_age = int(row[5])
            if passenger_age < 18:
                under_eighteen_survival_counter += 1
        except ValueError:
            pass
    print(f"{female_survival_counter} females survived the titanic.")
    print(f"{under_eighteen_survival_counter} minors survived the titanic.")

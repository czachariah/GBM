import os
import csv


def getRisk(sector, percentage, size, training, frameworks, attacks, weaknesses):
    '''
    sectorRisk = 0.0
    if sector == 1:
        sectorRisk = 0.1
    elif sector == 2:
        sectorRisk = 0.5
    else:
        sectorRisk = 1.95

    percentageRisk = 0.0
    if percentage == 1:
        percentageRisk = 0.1
    elif percentage == 2:
        percentageRisk = 0.6
    else:
        percentageRisk = 1.8

    sizeRisk = 0.0
    if size == 1:
        sizeRisk = 0.05
    elif size == 2:
        sizeRisk = 0.5
    else:
        sizeRisk = 2.1

    trainingRisk = 0.0
    if training == 1:
        trainingRisk = 0.1
    elif training == 2:
        trainingRisk = 0.4
    else:
        trainingRisk = 2.1

    overallRisk = sectorRisk*percentageRisk*sizeRisk*trainingRisk
    print(overallRisk)

    if overallRisk <= 0.33:
        return 1
    elif overallRisk >= 0.66:
        return 3
    else:
        return 2
    '''

    avg = (sector + percentage + size + training + frameworks + attacks + weaknesses) / 7.0

    if avg <= 1.66:
        return 1
    elif avg > 2.33:
        return 3
    else:
        return 2


def main():
    # find and remove existing "dataSet.csv" and create a new one to append to
    dir_name = os.path.dirname(os.path.abspath(__file__))
    dataSet = os.path.join(dir_name, "dataSet" + "." + "csv")
    if os.path.exists(dataSet):
        os.remove(dataSet)
    f = open("dataSet.csv", "w+")
    cr = csv.writer(f, delimiter=",", lineterminator="\n")

    # append the headers
    cr.writerow(["Sector", "Percentage", "Size", "Training", "Frameworks", "Attacks", "Weaknesses", "Risk"])

    # now append all the combinations of the factors
    for sector in range(1, 4):
        for percentage in range(1, 4):
            for size in range(1, 4):
                for training in range(1, 4):
                    for frameworks in range(1, 4):
                        for attacks in range(1, 4):
                            for weaknesses in range(1, 4):
                                cr.writerow([str(sector), str(percentage), str(size), str(training), str(frameworks), str(attacks), str(weaknesses), str(getRisk(sector, percentage, size, training, frameworks, attacks, weaknesses))])

if __name__ == "__main__":
    main()


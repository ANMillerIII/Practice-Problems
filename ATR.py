# Reads, parses, and outputs MC21 data from *.o* and tally files into readable .csv format. - Al Miller 10/31/2019
# Revised 11/1/2019 to fix row-column, and seperate output into 'axAzCI_[i].txt' and 'axAzMEAN_[i].txt', put 'out_[i].csv' in order, remove "Mesh Box:", and put output in new directories.

import os, sys, argparse, re, csv

def main():

    # get files to read from CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("file1")
    parser.add_argument("file2")
    args = parser.parse_args()

    # exception handling
    if len(sys.argv) != 3:
        sys.exit("Usage: py ATR o_file tally_file")

    # make directory and increment file names if they already exist
    i = 0
    current = os.getcwd()
    new = os.path.join(current, f'out_{i}')
    while os.path.exists(new):
        i += 1
        new = os.path.join(current, f'out_{i}')
    os.makedirs(new)

    # read and parse select info from o file, outputting to out[i].csv
    with open(args.file1, 'r') as file1:  # might need to change formatting
        with open(f"{new}\\out_{i}.csv", 'w+', newline='') as OUT:
            for line in file1:
                line = line.rstrip()
                if 'Flux normalization factor:' in line:
                    csv.writer(OUT).writerow(
                        ['Flux normalization factor:', line[38:51], line[51:]])
                elif 'Avg. source photon energy:' in line:
                    csv.writer(OUT).writerow(
                        ['Avg. source photon energy:', line[38:51], line[51:]])
                elif 'Avg. photon energy release:' in line:
                    csv.writer(OUT).writerow(
                        ['Avg. photon energy release:', line[38:51], line[51:]])

    # read and parse tally #'s, names, types, and corresponding region/mean/CI info, appending to out[i].csv
    with open(args.file2, 'r') as file2:
        with open(f"{new}\\out_{i}.csv", 'a+', newline='') as OUT:
            lines = file2.readlines()
            csv.writer(OUT).writerow(['', '', ''])
            tallys = [1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18] # do tally #'s stay consistent?
            counter = 0
            while counter <= 14:
                for index, line in enumerate(lines):
                    line = line.rstrip()
                    if re.search('Tally', line):  # finding tally lines
                        if int(line[6:]) == tallys[counter]:
                            counter += 1
                            skipLine = False
                            csv.writer(OUT).writerow(['', '', ''])
                            if re.search('\s{2}"', lines[index+3]):  # tally name
                                if re.search('(?:Neutron|Photon) tally.', lines[index+6]):  # omitting nuclide/axial/azimuthal rows
                                    if not re.search('\s{2}"Total Isotopic', lines[index+3]):
                                        if not re.search('AxialPP', lines[index+3]):
                                            if not re.search('AzimuthalPP', lines[index+3]):
                                                csv.writer(OUT).writerow(['Tally', 'Name', 'Type', 'Region', 'Mean', '95% Confidence Interval'])
                                                name = str(re.findall(r'"([^"]*)"', lines[index+3])[0])
                                                csv.writer(OUT).writerow([line[:], name, lines[index+6][2:9]])
                                            else:
                                                skipLine = True
                                        else:
                                            skipLine = True
                                    else:
                                        skipLine = True
                                else:
                                    skipLine = True
                            else:
                                skipLine = True
                        else:
                            skipLine = True

                    # finds rows w/means and 95% CI's
                    elif len(line) >= 46 and line[45].isdigit() and skipLine == False: # format "Region:" rows differently
                        if re.search('\s{2}Region:', lines[index-1]):
                            regionName = str(re.findall(r'"([^"]*)"', lines[index-1])[0])
                            csv.writer(OUT).writerow(['', '', '', regionName, line[45:55], line[58:68]]) # format "Mesh Box:" rows differently
                        elif re.search('\s{2}Mesh Box:', lines[index-1]):
                            csv.writer(OUT).writerow(['', '', '', lines[index-1][12:20].rstrip(), line[45:55], line[58:68]])
                        else:
                            csv.writer(OUT).writerow(['', '', '', lines[index-1][2:-1], line[45:55], line[58:68]])

    # make seperate out file for CI of axial andn azimuth, 10x19
    with open(args.file2, 'r') as file2:
        with open(f"{new}\\axAzCI_{i}.txt", 'w+') as OUT:
            lines = file2.readlines()
            axRows = {x: [] for x in range(0, 10)}
            azRows = {x: [] for x in range(0, 20)}
            axCount = azCount = 0
            for index, line in enumerate(lines):
                line = line.rstrip()
                if 'Axial' in line:
                    OUT.write(f'axial\nelement 01\n')
                elif re.search('_ax_', line):
                    axRowKey = axCount % 10
                    axCount += 1
                    axRows[axRowKey].append(lines[index+1][58:68])
            for key, value in axRows.items():
                for element in value:
                    OUT.write(str(element)+"\t")
                OUT.write(f'\n')
            for index, line in enumerate(lines):
                line = line.rstrip()
                if 'Azimuthal' in line:
                    OUT.write(f'\nazimuthal\nelement 01\n')
                elif re.search('_az_', line):
                    azRowKey = azCount % 20
                    azCount += 1
                    azRows[azRowKey].append(lines[index+1][58:68])
            for key, value in azRows.items():
                for element in value:
                    OUT.write(str(element)+"\t")
                OUT.write(f'\n')

    # make seperate out file for MEAN of axial and azimuth, 10x19
    with open(args.file2, 'r') as file2:
        with open(f"{new}\\axAzMEAN_{i}.txt", 'w+') as OUT:
            lines = file2.readlines()
            axRows = {x: [] for x in range(0, 10)}
            azRows = {x: [] for x in range(0, 20)}
            axCount = azCount = 0
            for index, line in enumerate(lines):
                line = line.rstrip()
                if 'Axial' in line:
                    OUT.write(f'axial\nelement 01\n')
                elif re.search('_ax_', line):
                    axRowKey = axCount % 10
                    axCount += 1
                    axRows[axRowKey].append(lines[index+1][45:56])
            for key, value in axRows.items():
                for element in value:
                    OUT.write(str(element)+"\t")
                OUT.write(f'\n')
            for index, line in enumerate(lines):
                line = line.rstrip()
                if 'Azimuthal' in line:
                    OUT.write(f'\nazimuthal\nelement 01\n')
                elif re.search('_az_', line):
                    azRowKey = azCount % 20
                    azCount += 1
                    azRows[azRowKey].append(lines[index+1][45:56])
            for key, value in azRows.items():
                for element in value:
                    OUT.write(str(element)+"\t")
                OUT.write(f'\n')


if __name__ == "__main__":
    main()

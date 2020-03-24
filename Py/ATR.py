# Reads, parses, and outputs MC21 data from *.o* and tally files into readable .csv format. - Al Miller 10/31/2019
import os, sys, argparse, csv, re

def main():

    # get files to read from CLI
    parser = argparse.ArgumentParser()
    parser.add_argument("file1")
    parser.add_argument("file2")
    args = parser.parse_args()

    # exception handling
    if len(sys.argv) != 3:
        sys.exit("Usage: py ATR o_file tally_file")

    # prepare to increment csv file names if already exist
    i = 0
    while os.path.exists("out%s.csv" % i):
        i += 1

    # read and parse select info from o file, outputting to out[i].csv
    with open(args.file1, 'r') as file1:  # might need to change formatting
        with open("out%s.csv" % i, 'w+', newline='') as OUT:
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
        with open("out%s.csv" % i, 'a+', newline='') as OUT:
            lines = file2.readlines()
            csv.writer(OUT).writerow(['', '', ''])
            for index, line in enumerate(lines):
                line = line.rstrip()
                if re.search('Tally', line):  # finding tally lines
                    skipLine = False
                    csv.writer(OUT).writerow(['', '', ''])
                    if re.search('\s{2}"', lines[index+3]):  # tally name
                        if re.search('(?:Neutron|Photon) tally.', lines[index+6]): # omitting nuclide/axial/azimuthal rows
                            if not re.search('\s{2}"Total Isotopic', lines[index+3]):
                                if not re.search('AxialPP', lines[index+3]):
                                    if not re.search('AzimuthalPP', lines[index+3]):
                                        csv.writer(OUT).writerow(
                                            ['Tally', 'Name', 'Type', 'Region', 'Mean', '95% Confidence Interval'])
                                        name = str(re.findall(
                                            r'"([^"]*)"', lines[index+3])[0])
                                        csv.writer(OUT).writerow(
                                            [line[:], name, lines[index+6][2:9]])
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
                elif len(line) >= 46 and line[45].isdigit() and skipLine == False:
                    if re.search('\s{2}Region:', lines[index-1]): # format "Region:" rows differently
                        regionName = str(re.findall(
                            r'"([^"]*)"', lines[index-1])[0])
                        csv.writer(OUT).writerow(
                            ['', '', '', regionName, line[45:55], line[58:68]])
                    else:
                        csv.writer(OUT).writerow(
                            ['', '', '', lines[index-1][2:-1], line[45:55], line[58:68]])

    # make seperate out file for axial and azimuth, 10x19
    with open(args.file2, 'r') as file2:
        with open("axAz%s.txt" % i, 'w+') as OUT:
            lines = file2.readlines()
            count = 1
            axText = ''
            azText = ''
            for index, line in enumerate(lines):
                line = line.rstrip()
                if 'Axial' in line:
                    OUT.write(f'axial\nelement 01\n')
                elif re.search('_ax_', line) and count <= 19:
                    axText += f"{lines[index+1][58:68]}\t"
                    count += 1
                elif count > 19:
                    axText += "\n"
                    count = 1
            OUT.write(f'{axText}\n')
            count = 1
            for index, line in enumerate(lines):
                line = line.rstrip()
                if 'Azimuthal' in line:
                    OUT.write(f'azimuthal\nelement 01\n')
                elif re.search('_az_', line) and count <= 19:
                    azText += f"{lines[index+1][58:68]}\t"
                    count += 1
                elif count > 19:
                    azText += "\n"
                    count = 1
            OUT.write(azText)

if __name__=="__main__":
    main()
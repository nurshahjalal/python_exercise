
with open("Notepad File.txt", "r") as f:
    with open("testcase.txt", 'w') as wf:
        for line in f:
            report_line = line.split('.')[0]
            wf.write(report_line + '\n')


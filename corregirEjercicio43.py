import os, sys, subprocess, io

SEP_STUDENT = '######'
SEP_STUDENT2 = SEP_STUDENT * 4
SEP_FILE = '----'
SEP_FILE2 = SEP_FILE * 3
EXERCISES_DIR = 'exercises'

if (len(sys.argv) != 2):
    print("Wrong number of arguments. Usage:\npython " +
        os.path.basename(__file__) + " csv_path")
    sys.exit()

#Adds header and footer to the file showing start and end of file
def showFile(path):
    out = f'\n{SEP_FILE2}\n{SEP_FILE}START {path}{SEP_FILE}\n{SEP_FILE2}\n{readFile(path)}\n'
    out += f'\n{SEP_FILE2}\n{SEP_FILE}END {path}{SEP_FILE}\n{SEP_FILE2}\n'
    return out

def readFile(path):
    print(f'\nReading file {path}')
    f = open(path, "r")
    data = f.read()
    f.close()
    return data

def writeFile(path, data):
    print(f'\nWriting file {path}')
    f = open(path, "w")
    f.write(data)
    f.close()

def runCommand(command):
    print(f'Running command:\n{command}\n')
    p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    p.wait()
    output = ''
    for line in io.TextIOWrapper(p.stdout, encoding="utf-8"):
        output += line
    return output

log = ''
names = ''

print('Starting execution\n', flush=True)
if os.path.exists(EXERCISES_DIR):
    result = runCommand('rm -rf ' + EXERCISES_DIR)
    print(result)
os.makedirs(EXERCISES_DIR)
csv = readFile(sys.argv[1]).split('\n')

for student in csv:
    data = student.split(',')
    name = data[0]
    names += name + '\n'
    folder_name = EXERCISES_DIR + '/' + name.replace(" ", "")
    repository = data[1]
    message = f'{SEP_STUDENT2}\n{SEP_STUDENT}{name}{SEP_STUDENT}\n{SEP_STUDENT2}\n'
    print(message, flush=True)
    log += message
    
    print('\n-Cloning respository-')
    command_git = f'git clone {repository} {folder_name}'
    log += f'\n{command_git}\n{runCommand(command_git)}\n'
    
    print('\n-Reading makefile, deleting it and replacing with other-')
    makefile_path = os.path.join(folder_name,'makefile')
    if os.path.exists(makefile_path):
        log += showFile(makefile_path)
        os.remove(makefile_path)
    else:
        log += f'\n{SEP_FILE}No makefile found{SEP_FILE}\n'
    command_makefile = 'cp makefile ' + folder_name
    log += f'\n{command_makefile}\n{runCommand(command_makefile)}\n'

    print('\n-Reading Java files-')
    command_find = f"find {folder_name} -name '*.java'"
    result = runCommand(command_find)
    log += f'\n{command_find}\n{result}\n'
    java_files = result.split('\n')
    for java_file in java_files:
        if java_file != '':
            log += showFile(java_file)

    print('\n-Executing Java main-')
    command_make = f"make execute -C {folder_name}"
    log += f'\n{command_make}\n{runCommand(command_make)}\n'

writeFile('log.txt',log)
writeFile('names.txt',names)

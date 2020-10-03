import zipfile
from os import listdir, path
from os.path import isfile, join
import os
import sys
from shutil import copyfile, rmtree
from pyunpack import Archive

if (len(sys.argv) != 3):
    print("Wrong number of arguments. Usage:\npython " + os.path.basename(__file__) + " zip_file directory_name")
    sys.exit()
path_to_zip_file = sys.argv[1]
directory_to_extract_to = sys.argv[2]
mainClass = "aplicacion.Main"
file_structure = ["dominio",
    join("dominio","ModeloOrdenador.java"),
    join("dominio","OfertaOrdenador.java"),
    "aplicacion",
    join("aplicacion","Principal.java")]
log = ''
names = ''
ignore_first_zip = True

#https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python
def list_files(startpath):
    tree = ""
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        tree += '{}{}/'.format(indent, os.path.basename(root))+'\n'
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            tree += '{}{}'.format(subindent, f)+'\n'
    return tree

def checkStructure(path_name):
    global log
    for x in file_structure:
        if not path.exists(join(path_name,x)):
            log += "Couldn't find " + x +'\n\n'
            return False
    return True

if not ignore_first_zip:
    if path.exists(directory_to_extract_to):
        print("Deleting " + directory_to_extract_to)
        rmtree(directory_to_extract_to)
    print("Extracting files")
    with zipfile.ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)

files_zip = [f for f in listdir(directory_to_extract_to) if (isfile(join(directory_to_extract_to, f)) and not f.endswith(".txt"))]
for x in files_zip:
    email_name = x.split('_')[1].split('@')[0]
    names += email_name + ':\t\t\t\n'
    print("\n####Processing files from " + email_name)
    log += '------' + email_name + '------\n'
    print("Extracting " + x)
    zip_file_loc = join(directory_to_extract_to,x)
    user_dir = join(directory_to_extract_to,email_name)
    if (x.endswith(".zip")):
        with zipfile.ZipFile(zip_file_loc, 'r') as zip_ref:
            zip_ref.extractall(user_dir)
    elif (x.endswith(".rar")):
        if not os.path.exists(user_dir):
            os.makedirs(user_dir)
        Archive(zip_file_loc).extractall(user_dir)
    else:
        print("Wrong extension file: " + x)
        continue
    tmp_dir = listdir(user_dir)[0]
    directory = join(user_dir,tmp_dir)
    log += 'File structure:\n' + list_files(directory)
    files_ok = checkStructure(directory)
    if not files_ok:
        print("Wrong file structure!!")
        continue
    files = []
    for y in file_structure:
        if y.endswith(".java"):
            files.append(' "' + join(directory,y) + '"')
    f = open(join(directory,file_structure[len(file_structure)-1]), "r")
    log += f.read()
    copyfile(join('Main.java'), join(directory,'aplicacion','Main.java'))
    files.append(' "' + join(directory,'aplicacion','Main.java') + '"')
    files_to_compile = ""
    for i in files:
        files_to_compile += i
    #Compiling
    fullPathCompile = 'javac ' + files_to_compile
    log += '\n' + fullPathCompile + '\n'
    log += os.popen(fullPathCompile).read()
    #Executing
    fullPathExecute = 'java -cp "' + directory + '" ' + mainClass
    log += '\n' + fullPathExecute + '\n'
    log += os.popen(fullPathExecute).read() + '\n'
f = open("log.txt", "w")
f.write(log)
f.close()
f = open("names.txt", "w")
f.write(names)
f.close()

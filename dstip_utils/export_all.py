import os
import subprocess

def export_all_ipynb(start_path = '.'):
    start_path = '.'
    dir_name_list = []
    for dir_path, _, file_names in os.walk(start_path):
        for file_name in file_names:
            if file_name.endswith('.ipynb') and ('ipynb_checkpoints' not in dir_path):
                dir_name_list.append([dir_path, file_name])

    for format_ in ['html']:
        for dir_path, file_name in dir_name_list:
            subprocess.run(
                ['jupyter', 'nbconvert', '--to', format_, "--execute", os.path.join(dir_path, file_name)], 
                check=True)

if __name__ == '__main__':
    export_all_ipynb()
import os

class FileSorting():
    """Class for organizing media files in folder structure YEAR/MONTH/...
    The new folder structure is generating in the same directory where the media files are located.

    """

    # file extensions for relocating
    file_extension = ('jpg', 'JPG', 'jpeg', 'mov', 'png', 'PNG', 'mp4', 'MP4','MOV', 'mov', 'gif')
    
    def __init__(self, path):
        self.path = path


    def file_list(self):
        """methode for generating list of files in the path
        Return: list_of_foto_files - list of the files in path directory with extension "file_extntion"
        """
        list_of_foto_files = []
        files = os.listdir(self.path)
        for file in files:
            if file.endswith(self.file_extension):
                list_of_foto_files.append(file)
        
        return list_of_foto_files
    
    def creating_directories(self, *args):
        """Methode for generating folder structer. It make structer depended from args

        Returns:
            path: complete path after creating the structure
        """
        path = self.path
        for directory in args:
            # if int(directory) > 12:
            #     directory = '20'+directory
            path=path+'/'+directory
            if not os.path.isdir(path):
                os.mkdir(path)
        return path
    
    def moving_files_iphone(self, files_list):
        """Moving files to new folder structure - for files with name structure: YY-MM-DD GG-MM.xxx

        Args:
            files_list (list): list of files for relocation
        """
        for file in files_list:
            try:
                year, month, day, *dd = file.split('-')
                path = self.creating_directories(year, month)
                os.rename(self.path+'/'+file, path+'/'+file)
            except:
                print('ptoblem z plikiem', file)

    def moving_files_samsung(self, files_list):
        """Moving files to new folder structure - for files with name structure: YYYYMMMDD....xxx

        Args:
            files_list (list): list of files for relocation
        """
        for file in files_list:
            try:
                year = file[0:4]
                month = file[4:6]
                path = self.creating_directories(year, month)
                os.rename(self.path+'/'+file, path+'/'+file)
            except:
                print('problem z plikiem', file)
    
    def moving_files_asus(self, files_list):
        """Moving files to new folder structure - for files with name structure: XXYYYYMMMDD....xxx

        Args:
            files_list (list): list of files for relocation
        """
        for file in files_list:
            try:
                year = file[2:6]
                month = file[6:8]
                # print(year+'--'+month)
                path = self.creating_directories(year, month)
                os.rename(self.path+'/'+file, path+'/'+file)
            except:
                print('problem z plikiem', file)

    
if __name__ == '__main__':
    test = FileSorting('')
    lista = test.file_list()
    test.moving_files_samsung(lista)
    


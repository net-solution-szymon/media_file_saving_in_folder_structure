# Small class for moving media files to the new folder structure.

This class was made to help with moving media files like pictures saved from smartphones, all in the same directory - happen when you are using some autoupload software (i.e. Nextcloud).

# How to use class:

```python
    test = FileSorting('/home/user/mediafiles') #example path
    list_of_files = test.file_list()
    test.moving_files_samsung(list_of_files)

```
In the class there are available few types of the name of the files - from my experience it was depending of smartphone manufacturer and model.

The class can be upgraded depending of your exact needs.


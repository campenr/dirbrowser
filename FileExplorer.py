import os

"""Program that performs basic file explorer functionality.

Program allows setting of current working directory, and listing of files/sub-
directories in current directory. Files listed in the directory can be filtered
by file type. Files/sub-directories are given a correspoding number allowing
selection of a file using a number. Funciton returns a list of files (in the
case of only wanting to select a single file the list is 1 item long).
"""
     

def list_children():
    """Function prints a list of all children in the current directory.

    Children include files and sub-directories assosiated with a number. 
    Children are stored in a dicitonary and assinged a numeric value. The
    zero value is set as '...' by default, as a placeholder for the parent dir.
    """

    #Initialise dictionary containing '...' as placeholder for parent dir
    child_dict = dict({0: "..."})

    #Get the list of children in the current working directory
    dir_list = os.listdir(os.getcwd())

    #Iterate over the list of children and add to the children dictionary
    #setting the key as the file/folder name and incrementing the value
    n = 1
    for i in dir_list:
        child_dict[n] = i
        n += 1
        
    #Create sorted lists of the keys and values from the children dictionary
    children_key_list = sorted(child_dict.keys())
    children_value_list = sorted(child_dict.values())

    #Print each key/value pair in an easy to read manner
    for n in range(len(children_key_list)):
        print("[{}] {}".format(children_key_list[n], children_value_list[n])) 


    #Return the dictionary of file/folder name keys and number value pairs
    return child_dict


list_children()


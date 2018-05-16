## Purpose

This code is related to the challenge found at https://at.boc-group.com/wad/challenge/basic/

## Code

The code is composed of a single file main.py 

The ""getImage" function performs the get request of the image. If the request is successful, the "createImage" function
generates a .png file

After getting the code the post request is performed through the "sendCode"function


All the functions are accessible by running the file through "python main.py". An infinite loop waits for user input. By typing "1" the image is fetched and created. The person can then see the code and type it in the next input. This will lead to the submission of the answer. By typing "quit" the script ends.

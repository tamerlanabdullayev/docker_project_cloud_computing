1. docker run -v /path/on/my/local/machine:/home/data -it tamerlan python main.py

        -v: to map the local machine directory to the /home/data directory inside the docker image
        -it: to make the image interactive while running the python script, so it can receive inputs from the user

    When it is running it will print the contents of the /home/data directory:
        List of the files in /home/data: IF.txt, Limerick.txt, result.txt
    
    And it will ask you to enter the file name. You only need to enter the name of file, not full path.

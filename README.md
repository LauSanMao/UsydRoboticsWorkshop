# UsydRoboticsWorkshop

#Listed below are notes for self

## 1 Making Changes to Repo
Now, we'll make some changes to this very repository, and tell Git that we've done so.
1. Go back to your terminal window.
2. Open the folder by typing `explorer.exe .` (windows) or `nautilus .` (linux) or `finder .` (macosx)
3. Put your name on the end of `Completed.md` with your favourite text editor. I recommend getting [VSCode](https://code.visualstudio.com/) for all platforms.
4. Save your changes. 
5. Go back to your terminal window, and type in `git add .`. This tells git to look at all the changes you made, and prepare them for sharing. 
6. Now type in `git commit -m "Added my name"`. This tells git that you're sure you want to make these changes, and tells git to tell other people that these changes pertain to adding your name. (The `-m` stands for message. You must have a message with your changes, because git likes to **enforce** good coding practice.)
7. Now type `git push origin master`. This tells git to pass your changes to github. You may have to login using your github username and password (or your email and password).
8. `git pull` to add changes done on github onto local files
## 2 Introduction to Python 
  
-tbc
  
## 3 Introduction to OpenCV
  
-tbc

## Challenges and Proof of work
 Week 2 - 


Write a program called `sayMyName.py` that prints out your name N times, where N is the first 2 digits of your SID.


Week 3 -

Be able to open and read both an image and a video of your choosing (can be taken off the Internet)

Week 4 -

Take an image of your choice (could be from the Internet or your own) and perform the following operations in separate instances (so don't do everything at once to the poor image).

- Rescale it to be half the original size
- Draw a shape (circle, line or rectangle) at the center of the image
- Pass it through a greyscale, blur and then canny layer
- Rotate it by 45 degrees

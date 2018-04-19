# 1. create repository
$git init  

$git add readme.txt  
$git commit -m "message"  

$git commit -a -m "message"  



# 2. rollback to lastest version
//HEAD Point is current position  

$ git log  
commit 3628164fb26d48395383f8f31179f24e0882e1e0  
Author: Michael Liao <askxuefeng@gmail.com>  
Date:   Tue Aug 20 15:11:49 2013 +0800  

    append GPL  

commit ea34578d5496d7dd233c827ed32a8cd576c5ee85  
Author: Michael Liao <askxuefeng@gmail.com>  
Date:   Tue Aug 20 14:53:12 2013 +0800  

    add distributed  

commit cb926e7ea50ad11b8f9e909c05226233bf755030  
Author: Michael Liao <askxuefeng@gmail.com>  
Date:   Mon Aug 19 17:51:55 2013 +0800  

    wrote a readme file  
    
$ git log --pretty=oneline  
3628164fb26d48395383f8f31179f24e0882e1e0 append GPL  
ea34578d5496d7dd233c827ed32a8cd576c5ee85 add distributed  
cb926e7ea50ad11b8f9e909c05226233bf755030 wrote a readme file  

//To go back to a previous commit by **index**  
$ git reset --hard HEAD^    //HEAD^ is -1; HEAD^^ is -2; HEAD~n is -n  

//To go back to a previous commit by **commit id**  
$ git reset --hard 3628164  
HEAD is now at 3628164 append GPL  

//To go back to **future**, find future commit id by checking operation logs  
$ git reflog  
ea34578 HEAD@{0}: reset: moving to HEAD^  
3628164 HEAD@{1}: commit: append GPL  
ea34578 HEAD@{2}: commit: add distributed  
cb926e7 HEAD@{3}: commit (initial): wrote a readme file  

# 3. Work Directory and Stage  
//git add : from **Work Directory** to **Stage**  
//git commit : from **Stage** to **Current Branch**  

//git diff --staged will only show changes to files in the "staged" area  
//git diff HEAD will show all changes to tracked files. If you have all changes staged for commit, then both commands will output the same.  

# 4. Undo Changes  
$ git status  
// On branch master  
// Changes not staged for commit:  
//   (use "git add <file>..." to update what will be committed)  
//   (use *"git checkout -- <file>..."* to discard changes in working directory)  

//       modified:   readme.txt  

//no changes added to commit (use "git add" and/or "git commit -a")  

$ git checkout -- readme.txt  
//if the file is *not* added to stage, this will undo *changes in the file*  
//if the file is added to stage, this will undo *the add operation*  

$ git status  
// On branch master  
// Changes to be committed:  
//   (use "git reset HEAD <file>..." to unstage)  
//  
//       modified:   readme.txt  

// Alternatively,  
$ git reset HEAD readme.txt  
// same as *git checkout -- readme.txt* when undo staging  
// *HEAD* means the lastest commit  

# 5. Remove files  

$ rm test.txt  
$ git status  
// On branch master  
// Changes not staged for commit:  
//   (use *"git add/rm <file>..."* to update what will be committed)  
//   (use "git checkout -- <file>..." to discard changes in working directory)  
//  
//       deleted:    test.txt  
//  
no changes added to commit (use "git add" and/or "git commit -a")  

//Option 1, commit the remove  
$ git rm test.txt //this is similar to *git add*  
$ git commit -m "remove test.txt"  

//Option 2, Undo the remove  
$ git checkout -- test.txt  








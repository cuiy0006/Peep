# 1. create repository
$ git init  

$ git add readme.txt  
$ git commit -m "message"  

$ git commit -a -m "message"  



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


# 6. Remove Repository

$ git remote add origin https://github.com/cuiy0006/scrawler-grab-all.git  
// $git remote add origin git@github.com/cuiy0006/scrawler-grab-all.git  
$ git push -u origin master  
//origin is the alias name of remote repository  
// -u is for first push  

// Or  
$ git clone https://github.com/cuiy0006/scrawler-grab-all.git  
// $ git clone git@github.com/cuiy0006/scrawler-grab-all.git  
// git@ is ssh protocol, https is https protocol  
// ssh protocol does not need password everytime, https protocol is slow and widely supported

# 7. Branches
## create and merge branches
https://www.liaoxuefeng.com/wiki/0013739516305929606dd18361248578c67b8067c8c017b000/001375840038939c291467cc7c747b1810aab2fb8863508000  

// on master branch  
$ git checkout -b dev  
Switched to a new branch 'dev'  

// checkout -b equals to  
$ git branch dev  
$ git checkout dev  
Switched to branch 'dev'  

$ git branch  
* dev  
  master  

//here nano readme.txt, add something
$ git add readme.txt  
$ git commit -m "branch test"  
[dev fec145a] branch test  
 1 file changed, 1 insertion(+)  
 
$ git checkout master  
Switched to branch 'master'  

$ git merge dev  
Updating d17efd8..fec145a  
Fast-forward  
 readme.txt |    1 +  
 1 file changed, 1 insertion(+)  
 
// **Fast-forward** is a mode that let HEAD point at dev's current commit and then merge  

// remove dev branch after merge  
$ git branch -d dev  
Deleted branch dev (was fec145a).  

## conflits

//**switch to feature1**
$ git checkout -b feature1  
Switched to a new branch 'feature1'  
// Then changes sth in readme.txt  

$ git add readme.txt  
$ git commit -m "AND simple"  
[feature1 75a857c] AND simple  
 1 file changed, 1 insertion(+), 1 deletion(-)  
 
//**switch back to master**
$ git checkout master  
Switched to branch 'master'  
Your branch is ahead of 'origin/master' by 1 commit.  
// Then changes sth in readme.txt  

$ git add readme.txt  
$ git commit -m "& simple"  
[master 400b400] & simple  
 1 file changed, 1 insertion(+), 1 deletion(-)  
 
 // **now merge**  
 $ git merge feature1  
Auto-merging readme.txt  
**CONFLICT (content): Merge conflict in readme.txt**  
Automatic merge failed; fix conflicts and then commit the result.  

$ git status  
// On branch master  
// Your branch is ahead of 'origin/master' by 2 commits.  
//  
// Unmerged paths:  
//   (use "git add/rm <file>..." as appropriate to mark resolution)  
//  
//       both modified:      readme.txt  
//  
no changes added to commit (use "git add" and/or "git commit -a")  
    
// **Then resolve conflicts manually**  
<<<<<<< HEAD  
Creating a new branch is quick & simple.  
=======  
Creating a new branch is quick AND simple.  
>>>>>>> feature1  

// **after resolving conflicts**, add and commit
$ git add readme.txt  
$ git commit -m "conflict fixed"  
[master 59bc1cb] conflict fixed  

// **graphical**  
$ git log --graph --pretty=oneline --abbrev-commit  
*   59bc1cb conflict fixed  
|\  
| * 75a857c AND simple  
* | 400b400 & simple  
|/  
* fec145a branch test  
...  
// altnatively,  
$ git config alias.graph 'log --decorate --oneline --branches --graph'  
$ git graph  


// remove feature1 branch  
$ git branch -d feature1  
Deleted branch feature1 (was 75a857c).  

## branch management strategy






  
  





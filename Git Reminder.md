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
// <<<<<<< HEAD  
// Creating a new branch is quick & simple.  
// =======  
// Creating a new branch is quick AND simple.  
// >>>>>>> feature1  

// **after resolving conflicts**, add and commit
$ git add readme.txt  
$ git commit -m "conflict fixed"  
[master 59bc1cb] conflict fixed  

// **graphical**  
$ git log --graph --pretty=oneline --abbrev-commit  
// *   59bc1cb conflict fixed  
// |\  
// | * 75a857c AND simple  
// * | 400b400 & simple  
// |/  
// * fec145a branch test  
...  
// altnatively,  
$ git config alias.graph 'log --decorate --oneline --branches --graph'  
$ git graph  


// remove feature1 branch  
$ git branch -d feature1  
Deleted branch feature1 (was 75a857c).  

## branch management strategy  
// **Fast-forward** is a mode that let HEAD point at dev's current commit and then merge  
// **resolve conflict** is to create new commit, not let HEAD point to branch latest commit  
// **Forbid Fast-forward** --no-ff is to create new commit, even if there is no conflicts  

$ git merge --no-ff -m "merge with no-ff" dev  
Merge made by the 'recursive' strategy.  
 readme.txt |    1 +  
 1 file changed, 1 insertion(+)  
 
$ git log --graph --pretty=oneline --abbrev-commit  
// *   7825a50 merge with no-ff  
// |\  
// | * 6224937 add merge  
// |/  
// *   59bc1cb conflict fixed  
// ...  

**strategy**
----------------------------------master(stable)  
----------------------------------dev(unstable)  
----------------------------------Tom  
----------------------------------John  

Tom and John branches merge to dev.  
When new version it to be released, dev merge to master.  

## stash current uncompleted content, for example issue 101 to be fixed

// **working on branch dev, but cannot commit yet**
$ git status  
// On branch dev  
// Changes to be committed:  
//   (use "git reset HEAD <file>..." to unstage)  
//  
//       new file:   hello.py  
//  
// Changes not staged for commit:  
//   (use "git add <file>..." to update what will be committed)  
//   (use "git checkout -- <file>..." to discard changes in working directory)  
//  
//       modified:   readme.txt  
//  

// **files modified and added to stage** -> can be stashed (hello.py)  
// **files modified but not added to stage yet** -> can be stashed (readme.txt)  
// **new created files that not ever be added** -> not managed by git -> cannot be stashed  

// **if switch to master now, hello.py and readme.text will influence master branch**  
// So, do  
$ git stash  
Saved working directory and index state WIP on dev: 6224937 add merge  
HEAD is now at 6224937 add merge  

// Then,  
$ git checkout master  
Switched to branch 'master'  
Your branch is ahead of 'origin/master' by 6 commits.  
$ git checkout -b issue-101  
Switched to a new branch 'issue-101'  

// Then fix issues and commit on issue-101.  
// Then switch to master, and merge issue-101  

// Then switch back to dev  
$ git checkout dev  
Switched to branch 'dev'  
$ git status  
// On branch dev  
nothing to commit (working directory clean)  

$ git stash list  
stash@{0}: WIP on dev: 6224937 add merge  

// Then pop the stash or apply+drop  
$ git stash pop  

$ git stash apply stash@{0}  
$ git stash drop stash@{0}  

// remove a branch that is not merged before  
$ git branch -D branchname  

## multiplayer coop

// origin is the remote source  
> $ git remote  
> origin  

> $ git remote -v  
> origin  git@github.com:michaelliao/learngit.git (fetch)  
> origin  git@github.com:michaelliao/learngit.git (push)  

// **push branch to remote**  
// push to master  
> $ git push origin master  

// push to dev  
> $ git push origin dev  

// master分支是主分支，因此要时刻与远程同步；  

// dev分支是开发分支，团队所有成员都需要在上面工作，所以也需要与远程同步；  

// bug分支只用于在本地修复bug，就没必要推到远程了，除非老板要看看你每周到底修复了几个bug；  

// feature分支是否推到远程，取决于你是否和你的小伙伴合作在上面开发。  

// **fetch branch from remote**  
// **A do**
> $ git clone git@github.com:michaelliao/learngit.git  
> Cloning into 'learngit'...  
> remote: Counting objects: 46, done.  
> remote: Compressing objects: 100% (26/26), done.  
> remote: Total 46 (delta 16), reused 45 (delta 15)  
> Receiving objects: 100% (46/46), 15.69 KiB | 6 KiB/s, done.  
> Resolving deltas: 100% (16/16), done.  

// by default, only master branch is clone to local, So  

> $ git branch  
> * master  

// create remote dev to local dev  
> $ git checkout -b dev origin/dev  

// do some add and commit  
> $ git push origin dev  

// **B do**  
// do some add and commit  
> $ git push origin dev  
> To git@github.com:michaelliao/learngit.git  
>  ! [rejected]        dev -> dev (non-fast-forward)  
> error: failed to push some refs to 'git@github.com:michaelliao/learngit.git'  
> hint: Updates were rejected because the tip of your current branch is behind  
> hint: its remote counterpart. Merge the remote changes (e.g. 'git pull')  
> hint: before pushing again.  
> hint: See the 'Note about fast-forwards' in 'git push --help' for details.  

// Push failed, because there is some conflicts    
// So, pull(fetch + merge) is needed    
> $ git pull  
> remote: Counting objects: 5, done.  
> remote: Compressing objects: 100% (2/2), done.  
> remote: Total 3 (delta 0), reused 3 (delta 0)  
> Unpacking objects: 100% (3/3), done.  
> From github.com:michaelliao/learngit  
>    fc38031..291bea8  dev        -> origin/dev  
> There is no tracking information for the current branch.  
> Please specify which branch you want to merge with.  
> See git-pull(1) for details  

>    git pull <remote> <branch>  

> If you wish to set tracking information for this branch you can do so with:  

>    git branch --set-upstream dev origin/<branch>  

// Pull failed, becuase local dev is not linked with remote dev    
// So, as hinted, link is needed    
> $ git branch --set-upstream dev origin/dev  
> Branch dev set up to track remote branch dev from origin.  

// Then try pull again   
> $ git pull  
> Auto-merging hello.py  
> CONFLICT (content): Merge conflict in hello.py  
> Automatic merge failed; fix conflicts and then commit the result.  

// Then resolve conflicts manually    
// Then commit and push   
> $ git commit -m "merge & fix hello.py"  
> $ git push origin dev  


# 8. Tag Management

## create tag

// Switch to required branch  
> $ git branch  
> * dev  
>   master  
> $ git checkout master  
> Switched to branch 'master'  

//Then  
> $ git tag v1.0  

//Check tag  
> $ git tag  
> v1.0  

//create tag on a history commit  
> $ git log --pretty=oneline --abbrev-commit  
> 6a5819e merged bug fix 101  
> cc17032 fix bug 101  
> 7825a50 merge with no-ff  
> **6224937** add merge  
> 59bc1cb conflict fixed  
> 400b400 & simple  
> 75a857c AND simple  
> fec145a branch test  
> d17efd8 remove test.txt  
> ...  

> $ git tag v0.9 **6224937**  

// show tag in alphabetical order  
> $ git tag  
> v0.9  
> v1.0  

// show tag details  
> $ git show v0.9  
> commit 622493706ab447b6bb37e4e2a2f276a20fed2ab4  
> Author: Michael Liao <askxuefeng@gmail.com>  
> Date:   Thu Aug 22 11:22:08 2013 +0800  

>     add merge  
> ...  
   
  
// create tag with message  
> $ git tag -a v0.1 -m "version 0.1 released" 3628164

## operate tag

> $ git tag -d v0.1  
> Deleted tag 'v0.1' (was e078af9)  

//push a tag  
> $ git push origin v1.0  
> Total 0 (delta 0), reused 0 (delta 0)  
> To git@github.com:michaelliao/learngit.git  
>  * [new tag]         v1.0 -> v1.0  

//push all tags  
> $ git push origin --tags  
> Counting objects: 1, done.  
> Writing objects: 100% (1/1), 554 bytes, done.  
> Total 1 (delta 0), reused 0 (delta 0)  
> To git@github.com:michaelliao/learngit.git  
>  * [new tag]         v0.2 -> v0.2  
>  * [new tag]         v0.9 -> v0.9  

//remove tags pushed, first remove local, then remove remote  
> $ git tag -d v0.9  
> Deleted tag 'v0.9' (was 6224937)  

> $ git push origin :refs/tags/v0.9  
> To git@github.com:michaelliao/learngit.git  
>  - [deleted]         v0.9  

# Fork public projects
// 1. fork on github from public project to own github,   
// 2. clone from own remote repository to local,   
// 3. revise and push to own remote repository,   
// 4. pull a request to original public one.    









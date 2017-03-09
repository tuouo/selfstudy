git remote add other /path/to/XXX
git fetch other
git checkout -b ZZZ other/master
mkdir ZZZ
git mv stuff ZZZ/stuff             # repeat as necessary for each file/dir
git commit -m "Moved stuff to ZZZ"
git checkout master                
# git merge ZZZ                      # should add ZZZ/ to master
git merge ZZZ --allow-unrelated-histories
git commit
git remote rm other
git branch -d ZZZ                  # to get rid of the extra branch before pushing
git push                           # if you have a remote, that is

#　http://stackoverflow.com/questions/1683531/how-to-import-existing-git-repository-into-another
# https://github.com/deercoder/0-tech-notes/blob/master/Git/git_merge_local_repos.md
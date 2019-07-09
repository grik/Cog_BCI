

## Branching strategy

`master/` - Official released version of application.  

`development/ ` - Our integration branch. Tested features should be merged to this branch.  

   * `feature/ ` - our personal branch. If we develop a feature, we'd like this branch ;) After feature is done,   merge to development branch.  

   * `bug/` - same as above, but for bugfixes.  


## Workflow tutorial

Let's say we develop a new feature.
First - we checkout to the development branch and pull all newly made changes.  

`git checkout development && git pull`

Then we create our own branch, `git checkout -b feature/new-connector-module` and start working on it.
After feature is done, and we'd make all necessary tests (and unittests of course!). 

If everything works just fine, we can eventually merge our branch to the development branch `git merge development`. Solve all merge issues (if any) and once again test entire app. 

Then, you should make the pull request for merging your branch into development branch. 

Notice, before that, you pulled changes from `development` into your branch, to make sure, that if anyone works of their feature, you have up to date version on your branch. 

Ok, after that, you'd make the pull request for merging your branch into `development` branch. Just wait for code reviews, if at least two members approve your PR, marge your branch into. Done, voila!  


If some features stacks up, we'll make our first release!  

For git training visit [this git tutorial](https://learngitbranching.js.org/) and for branching strategies just google up some examples ;)

## Versioning 

So, what about versions of our app?
I'd use semantic versioning, as it is most friendly for both user and the developer.

### So what about it? 

We basicly have three numbers `X.Y.Z`

`X` stands for a major relase version. It contains such changes, that making it incompatibile with previous versions.  For our example, our refactoring would be such change. `1.0.0` should be version of completed project. After that, maybe some new refactoring or new features... But if about features...

`Y` stands for features. If you make a big new thingy, you can release it with new Y number. In our project, that would be bi-weekly release of not just one feature, but many.

`Z` zzz... like bugs. Z is regarding bugfixes. If somethings fail and we found out after release, we'd make a hotfix, adding one number to Z position.

Example: `1.2.12` - Major relase, 2 new features already and 12 small fixes. 

https://semver.org/ - page about sem versioning.

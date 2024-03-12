# Contributing to discohook

First off, thank you for considering contributing to Discohook. It's people like you that make Discohook such a great tool.

### Where do I go from here?

If you've noticed a bug or have a feature request, make sure to check our 
[Issues](https://github.com/jnsougata/discohook/issues) to see 
if someone else in the community has already created a ticket. 
If not, go ahead and [make one](https://github.com/jnsougata/discohook/issues/new)!

### Fork & create a branch

If this is something you think you can fix, then [fork discohook](https://help.github.com/articles/fork-a-repo) 
and create a branch with a descriptive name.

A good branch name would be (where issue #325 is the ticket you're working on):

```bash
git checkout -b 325-add-japanese-localization
```
### Get the test suite running
Make sure you're using a virtual environment of some sort (e.g. venv).  
Once you have your virtualenv set up and activated, enter the following command to install discohook's dependencies:

```bash
pip install -r requirements.txt
```
### Implement your fix or feature
At this point, you're ready to make your changes! Feel free to ask for help; everyone is a beginner at first.  

### Make a Pull Request
At this point, you should switch back to your main branch and make sure it's up-to-date with discohook's main branch:

```bash
git remote add upstream git@github.com:jnsougata/discohook.git
git checkout main
git pull upstream main
```
Then update your feature branch from your local copy of master, and push it!

```bash 
git checkout 325-add-japanese-localization
git rebase main
git push --set-upstream origin 325-add-japanese-localization
```
Finally, go to GitHub and make a [Pull Request](https://help.github.com/articles/creating-a-pull-request) 🎉

### Keeping your Pull Request updated
If a maintainer asks you to "rebase" your PR, they're saying that a lot of code has changed, and that you need to update your branch, so it's easier to merge.  
To learn more about rebasing in Git, there are a lot of good resources but here's the suggested workflow:
```bash
git checkout 325-add-japanese-localization
git pull --rebase upstream main
git push --force-with-lease 325-add-japanese-localization
```
### Merging a PR (maintainers only)
A PR can only be merged into main by a maintainer if:  
- It is passing CI.
- It has been approved by at least one maintainer. If it was a maintainer who opened the PR, only an additional maintainer can approve it.
- It has no requested changes.
- It is up-to-date with current main.

Any maintainer is allowed to merge a PR if all of these conditions are met.  

### Standards
In this project, we use:
- PEP8 for Python style

### Resources
- [How to Contribute to Open Source](https://opensource.guide/how-to-contribute/)
- [Using Pull Requests](https://help.github.com/articles/about-pull-requests/)
- [GitHub Help](https://help.github.com/)

> This is a general guide and may not cover all possible contributions.

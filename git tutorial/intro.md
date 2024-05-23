# Git

git is a distributed version control system that is used to track changes in the source code during the development of software. It is designed to coordinate work among programmers, but it can be used to track changes in any set of files. It is widely used in open-source projects and in the industry.

## Why use git?

- **Distributed**: Git is a distributed version control system, which means that every developer has a copy of the repository on their local machine. This allows developers to work offline and to commit changes to the repository without having to be connected to a central server.
- **Fast**: Git is fast because it is designed to be efficient with large projects and to handle thousands of commits.
- **Branching and merging**: Git makes it easy to create branches to work on new features or to fix bugs, and to merge changes back into the main branch when they are ready.
- **History**: Git keeps a complete history of all changes to the repository, so you can see who made a change, when it was made, and why it was made.
- **Collaboration**: Git makes it easy to collaborate with other developers by allowing you to share your changes with others and to merge their changes into your repository.
- **Open-source**: Git is open-source software, which means that it is free to use and that you can modify the source code to suit your needs.
- **Popular**: Git is widely used in the industry and in open-source projects, so it is a valuable skill to have as a developer.
- **Integration**: Git integrates with many other tools and services, such as GitHub, Bitbucket, and GitLab, which makes it easy to use git with other tools that you may already be using.
- **Security**: Git is secure because it uses cryptographic hashes to store data, which makes it difficult for someone to tamper with the repository.
- **Backup**: Git is a great way to back up your code because it stores a complete history of all changes to the repository, so you can always revert to a previous version if something goes wrong.
- **Versioning**: Git allows you to track changes to your code over time, so you can see how your code has evolved and revert to a previous version if necessary.

## How does git work?

Git works by creating a repository, which is a directory that contains all of the files and directories that make up your project, as well as a hidden directory called `.git` that contains all of the metadata that git needs to track changes to the repository. When you make changes to the files in your project, git tracks those changes by creating a new commit, which is a snapshot of the changes that you have made. You can then push those changes to a remote repository, such as GitHub, Bitbucket, or GitLab, to share them with others.

## Basic git commands

Here are some basic git commands that you will need to know to get started with git:

- `git init`: Initializes a new git repository in the current directory.
- `git clone <url>`: Clones a remote repository to your local machine.
- `git add <file>`: Adds a file to the staging area. Using `.` will add all files.
- `git commit -m "<message>"`: Commits the changes in the staging area to the repository.
- `git push`: Pushes the changes in the local repository to the remote repository.
- `git pull`: Pulls the changes from the remote repository to the local repository.
- `git status`: Shows the status of the working directory and the staging area.
- `git log`: Shows the commit history of the repository.
- `git branch`: Shows the branches in the repository.
- `git checkout <branch>`: Switches to the specified branch.
- `git merge <branch>`: Merges the specified branch into the current branch.
- `git remote -v`: Shows the remote repositories that are associated with the local repository.
- `git config --global user.name "<name>"`: Sets the name that will be associated with your commits.
- `git config --global user.email "<email>"`: Sets the email address that will be associated with your commits.
- `git help`: Shows the help documentation for git.

## Common git workflows
```bash
git init
git add .
git commit -m "Initial commit"

# Create a new repository on GitHub, then push the changes to the remote repository
git remote add origin <url>
git push -u origin main
# Next time you can just use `git push`
```

```bash

## Resources

Pro Git book: https://git-scm.com/book/en/v2

Git documentation: https://git-scm.com/doc

GitHub Guides: https://guides.github.com/
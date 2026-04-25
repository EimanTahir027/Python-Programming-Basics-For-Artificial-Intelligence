  # Contributing to Python Programming Basics for Artificial Inteligence  :

We love your input! We want to make contributing to this project as easy and transparent as possible, whether it's:

- Reporting a bug
- Discussing the current state of the code
- Submitting a fix
- Proposing new features
- Becoming a maintainer

## Steps to contribute

- Comment on the issue you want to work on. Make sure it's not assigned to someone else.

### Making a PR

> - Make sure you have been assigned the issue to which you are making a PR.
> - If you make PR before being assigned, It may be labeled `invalid` and closed without merging.

- Fork the repo and clone it on your machine.
- Add a upstream link to main branch in your cloned repo

    ```sh
    git remote add upstream https://github.com/EimanTahir027/Python-Programming-Basics-For-Artificial-Intelligence.git
    ```

- Keep your cloned repo upto date by pulling from upstream (this will also avoid any merge conflicts while committing new changes)

    ```sh
    git pull upstream dev
    ```

- Create your feature branch

    ```sh
    git checkout -b <feature-name>
    ```

- Include the changes you have made for commits

    ```sh
    git add <name-of-file>
    ```

- Commit all the changes

    ```sh
    git commit -m "Meaningful commit message"
    ```

- Push the changes for review

    ```sh
    git push origin <branch-name>
    ```

- Create a PR from our repo on Github.

### Additional Notes

- Any changes should be made in the `dev` branch.
- Changes should be logged in the `CHANGELOG.md` file.
- Code should be properly commented to ensure it's readability.
- If you've added code that should be tested, add tests as comments.
- Make sure your code properly formatted.
- Issue that pull request!

## Issue suggestions/Bug reporting

When you are creating an issue, make sure it's not already present. Furthermore, provide a proper description of the changes. If you are suggesting any code improvements, provide through details about the improvements.

**Great Issue suggestions** tend to have:

- A quick summary of the changes.
- In case of any bug provide steps to reproduce
  - Be specific!
  - Give sample code if you can.
  - What you expected would happen
  - What actually happens
  - Notes (possibly including why you think this might be happening, or stuff you tried that didn't work)


## License

By contributing, you agree that your contributions will be licensed under its  [MIT License](http://choosealicense.com/licenses/mit/).

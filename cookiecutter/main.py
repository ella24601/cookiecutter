#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
cookiecutter.main
-----------------

Main entry point for the `cookiecutter` command.

The code in this module is also a good example of how to use Cookiecutter as a
library rather than a script.
"""

import argparse
import os

from .find import find_template
from .generate import generate_context, generate_files
from .vcs import git_clone


def main():
    """ Entry point for the package, as defined in setup.py. """

    # Get command line input/output arguments
    parser = argparse.ArgumentParser(
        description='Create a project from a Cookiecutter project template.'
    )
    parser.add_argument(
        'input_dir',
        help='Cookiecutter project template dir, e.g. {{project.repo_name}}/'
    )
    args = parser.parse_args()
    
    # If it's a git repo, clone and prompt
    if args.input_dir.endswith('.git'):
        repo_dir = git_clone(args.input_dir)
        project_template = find_template(repo_dir)
        os.chdir(repo_dir)
    else:
        project_template = args.input_dir

    # Create project from local context and project template.
    context = generate_context()
    generate_files(
        input_dir=project_template,
        context=context
    )


if __name__ == '__main__':
    main()
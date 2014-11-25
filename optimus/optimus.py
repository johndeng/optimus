#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Optimus
    ~~~~~~~

    Optimus is Python project constructor.

    Now support create `Tornado` project.

    Usage::

        # Change the directory you want to create a project
        $ cd target_dir

        # Run command!
        $ optimus -p example
	# or
	$ optimus --project_name example

"""

import click

from utils.command import TemplateCommand


@click.command()
@click.option("-p", "--project_name", help="Name of project")
def main(project_name):
    """ Project constructor for Python popular web framework.

    Now only support `Tornado`
    """

    if not project_name:
	click.echo("Fail!!! project_name is required!")
	return

    template_name = "tornado"
    command = TemplateCommand(project_name, template_name)
    command.execute()
    click.echo("Create project success!")


if __name__ == "__main__":
    main()

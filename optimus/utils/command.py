# -*- coding: utf-8 -*-


import os
import jinja2
import os.path


class TemplateCommand(object):
    """ Using template to construct a project structure.
    """

    def __init__(self, project_name, template_name=None, target=None):

        self.project_name = project_name
        self.template_name = template_name
        self.target = target

    def template_path(self):

        template_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            'templates'
        )
        return os.path.join(template_dir, self.template_name)

    def execute(self):

        if self.target is None:
            top_dir = os.path.join(os.getcwd(), self.project_name)

        if not os.path.exists(top_dir):
            os.mkdir(top_dir)
        else:
            raise CommandError("'%s' already exists" % top_dir)

        base_name = 'project_name'
        template_path = self.template_path()
        prefix_length = len(template_path) + 1

        for root, dirs, files in os.walk(template_path):

            path_rest = root[prefix_length:]
            relative_dir = path_rest.replace(base_name, self.project_name)

            if relative_dir:
                target_dir = os.path.join(top_dir, relative_dir)

                if not os.path.exists(target_dir):
                    os.mkdir(target_dir)

            for file_name in files:

                if file_name.endswith(('.pyo', '.pyc')):
                    continue

                old_path = os.path.join(root, file_name)
                new_path = os.path.join(
                    top_dir,
                    relative_dir,
                    file_name.replace(base_name, self.project_name)
                )

                with open(old_path, 'rb') as template_file:
                    content = template_file.read()
                    content = content.decode('utf-8')
                    template = jinja2.Template(content)
                    content = template.render(project_name=self.project_name)
                    content = content.encode('utf-8')

                with open(new_path, 'wb') as new_file:
                    new_file.write(content)


class CommandError(Exception):
    """ Error handle for optimus
    """
    pass

from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        project_info = toml.loads(content)
        name= project_info['tool']['poetry']['name']
        description= project_info['tool']['poetry']['description']
        dependencies= project_info['tool']['poetry']['dependencies']
        dev_dependencies= project_info['tool']['poetry']['group']['dev']['dependencies']
        authors = project_info['tool']['poetry']['authors']
        license_here = project_info['tool']['poetry']['license']


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, license_here, authors)

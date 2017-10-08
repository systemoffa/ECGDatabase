from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

name = "ECGDatabase"
default_task = ["install_dependencies", "publish"]
version = "1.0"

@init
def set_properties(project):
    project.set_property("coverage_break_build", False)
    project.set_property("bucket_prefix", "lambda/commercial-listings-grouping/")
    project.depends_on("beautifulsoup4", "==4.6.0")
    project.depends_on("flask", "==0.12.2")
    project.depends_on("flask_script", "==2.0.5")
    project.depends_on("requests", "==2.18.4")
    project.depends_on("idna", "==2.6")
    project.depends_on("urllib3", "==1.22")
    project.depends_on("certifi", "==2017.7.27.1")
    project.depends_on("chardet", "==3.0.4")
    project.build_depends_on("mock")

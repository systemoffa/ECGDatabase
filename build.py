from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

name = "ECGDatabase"
default_task = ["install_dependencies", "package"]
version = "1.0"

@init
def set_properties(project):
    project.set_property("coverage_break_build", False)
    project.set_property("bucket_prefix", "lambda/commercial-listings-grouping/")
    project.depends_on("beautifulsoup4", "==4.6.0")
    project.depends_on("flask", "==0.12.2")
    project.depends_on("flask_script", "==2.0.5")
    project.build_depends_on("mock")

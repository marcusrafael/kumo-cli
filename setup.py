import setuptools
import kumo_cli


setuptools.setup(
    name="kumo",
    version=kumo_cli.__version__,
    author="Marcus Rafael Xavier",
    author_email="mrxl@cin.ufpe.br",
    description="Kumo Command Line Interface",
    url="https://github.com/marcusrafael/kumo-cli",
    license="MIT",
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': ['kumo = kumo_cli.kumo_cli:cli']}
)

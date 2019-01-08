import os
import urllib
import json
import configparser
import click
import yaml
import requests
import kumo_cli


welcome = click.style(
    r"""
     _  __
    | |/ / _   _  _ __ ___    ___
    | ' / | | | || '_ ` _ \  / _ \
    | . \ | |_| || | | | | || (_) |
    |_|\_\ \__,_||_| |_| |_| \___/

    Welcome to Kumo CLI!

    Use 'kumo --version' to display the current version.
    """,
    fg="white")


@click.group(invoke_without_command=True)
@click.version_option(version=kumo_cli.__version__)
@click.pass_context
def cli(ctx):
    if not ctx.invoked_subcommand:
        click.echo(welcome)


@cli.command(short_help="Migrate the virtual machine.")
@click.argument("file")
def migrate(file):
    with open(file) as template:
        yaml_file = yaml.safe_load(template.read())
        home = os.path.expanduser("~")
        filenames = os.path.join(home, ".kumo/kumo.conf")
        config = configparser.ConfigParser()
        config.read(filenames=filenames)
        migration = yaml_file.get("migration")
        source_account = dict(config[migration.get("source_account")])
        destination_account = dict(config[migration.get("destination_account")])
        migration = {"source_account": source_account,
                     "destination_account": destination_account,
                     "virtual_machine": migration.get("virtual_machine")}
        kumo_url = config["kumo"]["url"]
        url = urllib.parse.urljoin(kumo_url, "migrate")
        import pprint; pprint.pprint(migration)
        json_file = json.dumps(migration)
        requests.post(url=url, json=json_file)


@cli.command(short_help="Create the kumo config file.")
def configure():
    config = configparser.ConfigParser()
    config["kumo"] = {}
    config["kumo"]["url"] = "http://localhost:5000"
    config["red"] = {}
    config["red"]["cloud"] = "amazon"
    config["red"]["bucket"] = ""
    config["red"]["region"] = ""
    config["red"]["availability_zone"] = ""
    config["red"]["instance_type"] = ""
    config["red"]["aws_access_key_id"] = ""
    config["red"]["aws_secret_access_key"] = ""
    config["blue"] = {}
    config["blue"]["cloud"] = "amazon"
    config["blue"]["bucket"] = ""
    config["blue"]["region"] = ""
    config["blue"]["availability_zone"] = ""
    config["blue"]["instance_type"] = ""
    config["blue"]["aws_access_key_id"] = ""
    config["blue"]["aws_secret_access_key"] = ""
    config["white"] = {}
    config["white"]["cloud"] = "google"
    config["white"]["bucket"] = ""
    config["white"]["zone"] = ""
    config["white"]["system"] = ""
    config["white"]["machine_type"] = ""
    config["white"]["type"] = ""
    config["white"]["project_id"] = ""
    config["white"]["private_key_id"] = ""
    config["white"]["client_email"] = ""
    config["white"]["client_id"] = ""
    config["white"]["auth_uri"] = ""
    config["white"]["token_uri"] = ""
    config["white"]["auth_provider_x509_cert_url"] = ""
    config["white"]["client_x509_cert_url"] = ""
    config["white"]["private_key"] = ""
    config["black"] = {}
    config["black"]["cloud"] = "google"
    config["black"]["bucket"] = ""
    config["black"]["zone"] = ""
    config["black"]["system"] = ""
    config["black"]["machine_type"] = ""
    config["black"]["type"] = ""
    config["black"]["project_id"] = ""
    config["black"]["private_key_id"] = ""
    config["black"]["client_email"] = ""
    config["black"]["client_id"] = ""
    config["black"]["auth_uri"] = ""
    config["black"]["token_uri"] = ""
    config["black"]["auth_provider_x509_cert_url"] = ""
    config["black"]["client_x509_cert_url"] = ""
    config["black"]["private_key"] = ""
    config["green"] = {}
    config["green"]["cloud"] = "microsoft"
    config["green"]["container"] = ""
    config["green"]["location"] = ""
    config["green"]["zones"] = ""
    config["green"]["virtual_machine_size"] = ""
    config["green"]["network"] = ""
    config["green"]["subnet"] = ""
    config["green"]["resource_group_name"] = ""
    config["green"]["client_id"] = ""
    config["green"]["client_secret"] = ""
    config["green"]["subscription_id"] = ""
    config["green"]["tenant_id"] = ""
    config["green"]["active_directory_endpoint_url"] = ""
    config["green"]["resource_manager_endpoint_url"] = ""
    config["green"]["active_directory_graph_resource_id"] = ""
    config["green"]["sql_management_endpoint_url"] = ""
    config["green"]["gallery_endpoint_url"] = ""
    config["green"]["management_endpoint_url"] = ""
    config["green"]["storage_account_name"] = ""
    config["green"]["storage_account_key"] = ""
    config["yellow"] = {}
    config["yellow"]["cloud"] = "microsoft"
    config["yellow"]["container"] = ""
    config["yellow"]["location"] = ""
    config["yellow"]["zones"] = ""
    config["yellow"]["virtual_machine_size"] = ""
    config["yellow"]["resource_group_name"] = ""
    config["yellow"]["client_id"] = ""
    config["yellow"]["client_secret"] = ""
    config["yellow"]["subscription_id"] = ""
    config["yellow"]["tenant_id"] = ""
    config["yellow"]["active_directory_endpoint_url"] = ""
    config["yellow"]["resource_manager_endpoint_url"] = ""
    config["yellow"]["active_directory_graph_resource_id"] = ""
    config["yellow"]["sql_management_endpoint_url"] = ""
    config["yellow"]["gallery_endpoint_url"] = ""
    config["yellow"]["management_endpoint_url"] = ""
    config["yellow"]["storage_account_name"] = ""
    config["yellow"]["storage_account_key"] = ""
    home = os.path.expanduser("~")
    directory = os.path.join(home, ".kumo")
    if not os.path.exists(directory):
        os.makedirs(directory)
    filename = os.path.join(home, ".kumo/kumo.conf")
    with open(filename, "w") as configfile:
        config.write(configfile)
        message = "Configuration: {}".format(filename)
        click.echo(click.style(message, fg="green"))

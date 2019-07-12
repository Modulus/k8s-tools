from pyfiglet import Figlet
import logging
import click

import aws.route53.dns_zone as dns_zone

# Initializing loggers and requisites
FORMAT = "%(asctime)-15s - %(levelname)s:%(name)s:%(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger("Main")

logger.info("Creating route53 entry for kubernetes nginx ingress")


f = Figlet(font="graffiti")
logging.info("-----------------------------------------------------------------------")
click.echo("\n")
click.echo(f.renderText("kwl - k8s"))
click.echo("\n")
logging.info("Welcome: kwl - command line tool for kuberntes")
logging.info("-----------------------------------------------------------------------")


valid_verbs = ["get", "update", "add", "delete"]
valid_resources = ["dns.zone", "ingress"]


@click.command()
@click.argument("verb")
@click.argument("resource")
@click.option("--name", help="name of resource to handle")
@click.option("--provider", default="aws", help="Cloud provider to use")
def cmd(verb, resource, provider, name):
    """
    This script helps you manage k8s
    """
    click.echo("%s %s --provider %s" % (verb, resource, provider))
    if verb in valid_verbs and resource in valid_resources:
        if verb == "get":
            if resource == "dns.zone":
                click.echo(dns_zone.get_hosted_zone(name=name, private=False))
            if resource == "ingress":
                click.echo("Listing ingresses in all namespaces")
        if verb == "update":
           if resource == "ingress":
               click.echo("Updating kubernetes dns entries based on ingressed")
        if verb == "delete":
            click.echo("Not implemented yet!") 
        if verb == "add":
            click.echo("Not implemented yet!")
    else:
        click.echo("Unkown")            
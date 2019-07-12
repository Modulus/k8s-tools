from pyfiglet import Figlet
import logging
import click

import aws.route53.dns_zone as dns_zone
from kube import discovery

# Initializing loggers and requisites
FORMAT = "%(asctime)-15s - %(levelname)s:%(name)s:%(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger("Main")



f = Figlet(font="graffiti")
logging.info("-----------------------------------------------------------------------")
click.echo("\n")
click.echo(f.renderText("kwl - k8s"))
click.echo("\n")
logging.info("Welcome: kwl - command line tool for kuberntes")
logging.info("-----------------------------------------------------------------------")


valid_resources = ["dns.zone", "ingress", "service"]


@click.group()
def operation():
    click.echo("Running command")

@operation.command()
@click.argument("resource")
@click.option("--filter", "-f", required=False, type=str, help="filter on resource with name:value, the value if part of the whole actual value. Example: 'name:nginx' or 'name:nginx;owner:twoflower'")
@click.option("--label_selector", "-l", required=False, type=str, help="label selector for resource")
def get(resource, filter, label_selector):
    if resource in valid_resources:
        if "ingress" == resource:
            click.echo("Getting ingresses in all namespaces")
            click.echo(discovery.list_ing_name_by_labels(label_selector=label_selector, filter=filter))
        elif "service" == resource:
            click.echo("Getting service in all namespaces")
            click.echo(discovery.list_svc_by_labels(label_selector=label_selector, filter=filter))
        elif resource == "dns.zone":
            click.echo(dns_zone.get_hosted_zone(filter=filter, private=False))

@operation.command()
@click.argument("resource")
def add():
    click.echo("Not implemented yet!")


@operation.command()
@click.argument("resource")
@click.option("--dns", default=True)
@click.option("--zone", default="")
@click.option("--private", default=False)
@click.option("--ingress_filter", default="name:jenkins")
def update(resource, dns, zone, private, ingress_filter):
   if resource in valid_resources:
       if  "ingress" == resource:
           logger.info("Updating ingress based on nginx ingress controller")
           ingress_controller = discovery.list_svc_by_labels(label_selector="app=nginx-ingress", filter="name:nginx") 
           logger.info(f"Found {ingress_controller}")
           dns_data = dns_zone.get_hosted_zone(filter=f"name:{zone}", private=private)

           ingresses=discovery.list_ing_name_by_labels(label_selector=None, filter=ingress_filter, fields="name")

           logger.info(f"Found: {ingresses}")

           logger.info(f"Found dns {dns_data}")

           dns_names = [element["name"] for element in ingresses if element["name"] ]

           zone_id = dns_data.id

           logger.info(f"DNS names: {dns_names}")
           logger.info(f"DNS zone: {zone_id}")

            

        #    dns_zone.update_hosted_zone()

@operation.command()
@click.argument("resource")
def delete():
    click.echo("Not implemented yet!")

#cmd.add_command(get)

# @get_group.command()
# @click.argument("verb")
# @click.argument("resource")
# @click.option("--name", help="name of resource to handle")
# @click.option("--provider", default="aws", help="Cloud provider to use")
# def cmd(verb, resource, provider, name):
#     """
#     This script helps you manage k8s
#     """
#     click.echo("%s %s --provider %s" % (verb, resource, provider))
#     if verb in valid_verbs and resource in valid_resources:
#         if verb == "get":
#             if resource == "dns.zone":
#                 click.echo(dns_zone.get_hosted_zone(name=name, private=False))
#             if resource == "ingress":
#                 click.echo("Listing ingresses in all namespaces")
#                 click.echo(discovery.list_ing_by_labels())
#         if verb == "update":
#            if resource == "ingress":
#                click.echo("Updating kubernetes dns entries based on ingressed")
#         if verb == "delete":
#             click.echo("Not implemented yet!") 
#         if verb == "add":
#             click.echo("Not implemented yet!")
#     else:
#         click.echo("Unkown")            
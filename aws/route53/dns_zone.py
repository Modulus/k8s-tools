import boto3
import logging
import utils.helpers as helper

# Initializing loggers and requisites
FORMAT = "%(asctime)-15s - %(levelname)s:%(name)s:%(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger("Main")


# parser = argparse.ArgumentParser(description="Create iam user for eks clusters on aws")
# parser.add_argument("--profile", type=str,  dest="profile", help="name of the aws profile in ~/.aws/credentials",
#                     required=True)
# parser.add_argument("--dns", type=str, dest="dns", help="dns name entry", default=None)
# parser.add_argument("--target", type=str, dest="target", help="target dns name entry", default=None)

# args = parser.parse_args()

# logger.info(f"Using profile {args.profile}")
# logger.info(f"User will have the name: {args.dns}")

# profile = "aws5_john"

# boto3.setup_default_session(profile_name=profile)

class Zone(object):

    def __init__(self, id, name):
        self.id = id
        self.name = name






def get_hosted_zone(filter="", private=False) -> Zone:

    client = boto3.client("route53")

    filter_map = helper.create_filter_dict(filter)
    name = filter_map["name"]
    zones = client.list_hosted_zones()

    logger.info(zones)

    for zone in zones["HostedZones"]:
        if name in zone["Name"] and zone["Config"]["PrivateZone"] == private:
            logger.info("HIT")
            return Zone(zone["Id"], zone["Name"])
    logging.error(f"Did not find zone {name}")
    return None

def update_hosted_zone(dns_names:list=None, target:str=None, zone:Zone=None):
    for dns_name in dns_names:
        logging.info("Creating route53 entry")

        route53 = boto3.client("route53")

        print(
                HostedZoneId=f'{zone.id}',
            ChangeBatch={
                'Comment': f"DNS Entry for nginx ingress on kubernetes with name {dns_name}",
                'Changes': [
                    {
                        'Action': 'UPSERT', #'CREATE', #|'DELETE'|'UPSERT',
                        'ResourceRecordSet': {
                            'Name': f"{dns_name}",
                            'Type': 'CNAME',
                            'TTL': 300,
                            'ResourceRecords': [
                                { 'Value': f"{target}",}
                            ]

                        }
                    },
                ]
            }  )
        # response = route53.change_resource_record_sets(
        #     HostedZoneId=f'{zone.id}',
        #     ChangeBatch={
        #         'Comment': f"DNS Entry for nginx ingress on kubernetes with name {args.dns}",
        #         'Changes': [
        #             {
        #                 'Action': 'UPSERT', #'CREATE', #|'DELETE'|'UPSERT',
        #                 'ResourceRecordSet': {
        #                     'Name': f"{dns_name}",
        #                     'Type': 'CNAME',
        #                     'TTL': 300,
        #                     'ResourceRecords': [
        #                         { 'Value': f"{target}",}
        #                     ]

        #                 }
        #             },
        #         ]
        #     }  
        # )
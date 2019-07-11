import boto3
import logging

# Initializing loggers and requisites
FORMAT = "%(asctime)-15s - %(levelname)s:%(name)s:%(message)s"
logging.basicConfig(level=logging.INFO, format=FORMAT)
logger = logging.getLogger("Main")

logger.info("Creating route53 entry for kubernetes nginx ingress")

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






def get_hosted_zone(name, private=False) -> str:

    client = boto3.client("route53")


    zones = client.list_hosted_zones()

    logger.info(zones)

    for zone in zones["HostedZones"]:
        if name in zone["Name"] and zone["Config"]["PrivateZone"] == private:
            logger.info("HIT")
            return Zone(zone["Id"], zone["Name"])

    return None




zone = get_hosted_zone("aws5.tv2.no", private=False)

logger.info(zone)

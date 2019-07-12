import pytest

import aws.route53.dns_zone as aws

def test_get_dnz_zone():
    zone = aws.get_hosted_zone("aws5.tv2.no", private=False)

    assert zone != None
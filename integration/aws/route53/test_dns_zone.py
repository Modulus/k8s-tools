import pytest

import aws.route53.dns_zone as dns_zone

@pytest.mark.slow
def test_get_dnz_zone():
    zone = dns_zone.get_hosted_zone("aws5.tv2.no", private=False)

    assert zone != None
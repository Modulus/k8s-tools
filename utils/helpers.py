import logging

logger = logging.getLogger("Helper")

def create_filter_dict(filter):
	if not filter:
		return None

	filter_map = {}

	elements = []
	if ";" in filter:
		elements = filter.split(";")
	else:
		elements.append(filter)

	for element in elements:
		if(":" not in element):
			raise ValueError(f"Missing : for name:value filter. Current element was {element}")
		else:
			parts = element.split(":")
			if len(parts) > 1:
				filter_map[parts[0]] = parts[1]

	return filter_map


def  extract_zone_id(id:str=None) -> str:
	"""Hosted zone id has the format /hostedzone/Z40FIOTQIPYWL9"""
	keyword = "/hostedzone/"
	if keyword in id:
		logger.info(f"Found {keyword} in {id} stripping it down")
		return id[len(keyword):len(id)]
	logger.info(f"{keyword} not found returning {id}")
	return id
import logging

logger = logging.getLogger("Helper")

def  extract_zone_id(id:str=None) -> str:
	"""Hosted zone id has the format /hostedzone/Z40FIOTQIPYWL9"""
	keyword = "/hostedzone/"
	if keyword in id:
		logger.info(f"Found {keyword} in {id} stripping it down")
		return id[len(keyword):len(id)]
	logger.info(f"{keyword} not found returning {id}")
	return id
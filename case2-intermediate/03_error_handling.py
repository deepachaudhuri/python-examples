"""
try / except / else / finally, custom exceptions
Run: python 03_error_handling.py
"""

class MissingTagError(Exception):
    """Raised when a required tag is missing from a resource."""


def get_environment_tag(volume):
    try:
        return volume["Environment"]
    except KeyError:
        raise MissingTagError(f"volume {volume.get('VolumeId')} has no Environment tag")


# case: tag exists
try:
    env = get_environment_tag({"VolumeId": "vol-111", "Environment": "prod"})
except MissingTagError as e:
    print("caught error:", e)
else:
    print("environment tag found:", env)   # only runs if no exception happened
finally:
    print("finished checking vol-111")

# case: tag missing
try:
    get_environment_tag({"VolumeId": "vol-999"})
except MissingTagError as e:
    print("caught expected error:", e)
finally:
    print("finished checking vol-999")

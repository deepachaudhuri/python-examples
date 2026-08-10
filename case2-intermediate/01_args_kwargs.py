"""
*args and **kwargs - flexible function arguments
Run: python 01_args_kwargs.py
"""

def delete_volumes(*volume_ids, dry_run=True, **extra_options):
    """*volume_ids collects any number of positional args into a tuple.
    **extra_options collects any number of extra keyword args into a dict."""
    for vol_id in volume_ids:
        if dry_run:
            print(f"[DRY RUN] would delete {vol_id}")
        else:
            print(f"deleting {vol_id}")
    print("extra options:", extra_options)

delete_volumes("vol-111", "vol-222", dry_run=True, reason="stale", requested_by="cleanup-lambda")

import argparse
import os

# there are two ways to authorize:
# - using API token. only --token argument is required
# - using client-id, client-secret, and account-id. NOT IMPLEMENTED YET


def cmdline_setup(parser: argparse.ArgumentParser):
    parser.add_argument('--token', help="API Token. Can be set by API_TOKEN environment variable", required=False)


def cmdline_validate(parser: argparse.ArgumentParser, args):
    # check if api token is provided
    if args.token is None:
        # or try to take it from the environment
        args.token = os.getenv("TOKEN")
        if args.token is None:
            # give up
            parser.error("TOKEN is required")

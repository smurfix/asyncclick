import asyncclick as click
from complex.cli import pass_environment


@click.command("status", short_help="Shows file changes.")
@pass_environment
def cli(ctx):
    """Shows file changes in the current working directory."""
    ctx.log("Changed files: none")
    ctx.vlog("bla bla bla, debug info")

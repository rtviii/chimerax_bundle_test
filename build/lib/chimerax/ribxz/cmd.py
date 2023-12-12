from chimerax.core.commands import CmdDesc


def hello_world(session):
    session.logger.info("Hello world!")


hello_world_desc = CmdDesc()

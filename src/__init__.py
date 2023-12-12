from chimerax.core.toolshed import BundleAPI
from chimerax.core.commands import register
from chimerax.core.commands import CmdDesc  # Command description
from chimerax.atomic import AtomsArg  # Collection of atoms argument
from chimerax.core.commands import BoolArg, StringArg  # Boolean argument

class _MyAPI(BundleAPI):

    api_version = 1  
    @staticmethod
    def register_command(bi, ci, logger):
        from . import cmd

        if ci.name == "ribxz print":

            print_desc = CmdDesc( required=[("rcsb_id", StringArg)])
            func       = cmd.print_profile
            desc       = print_desc

        elif ci.name == "ribxz by_class":

            by_class_desc = CmdDesc(required=[("rcsb_id", StringArg)])
            func          = cmd.by_class
            desc          = by_class_desc
            register(ci.name, desc, func)

        else:
            raise ValueError("trying to register unknown command: %s" % ci.name)


bundle_api = _MyAPI()

class CustomCommandMixin:
    dryrun: bool

    def print_msg(self, msg: str) -> None:
        if self.dryrun:
            self.stdout.write(f"***DRYRUN*** {msg}")
        else:
            self.stdout.write(msg)

from _typeshed import Incomplete

from ..cmd import Command

class install_lib(Command):
    description: str
    user_options: Incomplete
    boolean_options: Incomplete
    negative_opt: Incomplete
    install_dir: Incomplete
    build_dir: Incomplete
    force: int
    compile: Incomplete
    optimize: Incomplete
    skip_build: Incomplete
    def initialize_options(self) -> None: ...
    def finalize_options(self) -> None: ...
    def run(self) -> None: ...
    def build(self) -> None: ...
    def install(self) -> list[str]: ...
    def byte_compile(self, files) -> None: ...
    def get_outputs(self): ...
    def get_inputs(self): ...

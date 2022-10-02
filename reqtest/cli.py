from typer import Argument, Option, Typer

main = Typer()


@main.command("run")
def run(
    file: str = Option(default="reqtest.yml", help="Name of ReqTest file to run."),
) -> None:
    print("Run")


@main.command("gen")
def gen(
    file: str = Option(default="reqtest.yml", help="Name of ReqTest file to generate."),
) -> None:
    print("Gen")

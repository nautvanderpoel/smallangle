import click
import numpy as np
from numpy import pi
import pandas as pd

@click.group()
def cmd_group():
    pass


@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=0,
    help = "value needs to be an integer, chosen by user"
)
def sin(number):
    """Calculates the tangent with arguments between [0,2pi] with 'number' as stepsize

    Args:
        number (integer): "Values within the range [0,2pi]"
    """

    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "sin (x)": np.sin(x)})
    print(df)
    return 

@cmd_group.command()
@click.option(
    "-n",
    "--number",
    default=0,
    help = "value needs to be an integer, chosen by user"
)
def tan(number):
    """Calculates the sine with arguments between [0,2pi] with 'number' as stepsize
    Args:
        number (integer): "Stepsize of domain [0,2pi]"
    """
    x = np.linspace(0, 2 * pi, number)
    df = pd.DataFrame({"x": x, "tan (x)": np.tan(x)})
    print(df)
    return


if __name__ == "__main__":
    cmd_group()




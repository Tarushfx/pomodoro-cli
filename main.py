from datetime import datetime
import typer
import time
import logging

logging.basicConfig(filename='app.csv', filemode='a',
                    format='%(asctime)s,%(levelname)s,%(message)s',
                    datefmt='%d/%b/%y %H:%M',
                    level=logging.DEBUG)

app = typer.Typer()

DEFAULT_BREAK = 1
DEFAULT_WORK = 1


def timer(duration: int):
    SECONDS_IN_A_MINUTE = 60
    total_seconds = SECONDS_IN_A_MINUTE*duration
    print(total_seconds)
    progress_bar_kwargs = {
        "label": "Time left",
        "bar_template": "%(label)s [%(bar)s] %(info)s",
        "color": True,
        "width": 40,
        "show_pos": True,
    }
    with typer.progressbar(range(total_seconds), **progress_bar_kwargs) as progress:
        # print(progress)
        for value in progress:
            # print(value, end=" ")
            time.sleep(0.1)
    # typer.echo(f"Processed {total_seconds} things.")


@app.command()
def pomo(duration: int = DEFAULT_WORK, pause: int = DEFAULT_BREAK):
    try:
        print(duration, pause)
        while True:
            completed = False
            # a = datetime.now()
            timer(duration)
            typer.echo(f"Work time completed:{duration} minutes")
            # b = datetime.now()
            # print(f"Time work:{b-a}")

            # a = datetime.now()
            timer(pause)
            typer.echo(f"Break time completed:{pause} minutes")
            # b = datetime.now()
            # print(f"Time pause:{b-a}")

            typer.secho("Do You want to repeat?[Y/n]", fg=typer.colors.BLUE)

            # logging
            logging.info(f"Work:{duration} minutes | Break:{pause} minutes")
            completed = True
            inp = input()
            if inp in ["y", "Y", ""]:
                continue
            print("Goodbye!")
            break
    except KeyboardInterrupt:
        if not completed:
            logging.warning(
                f"Keyboard Interrupted! Work:{duration} minutes | Break:{pause} minutes")
        print("Interrupted and logged")


@app.command()
def log():
    pass


@app.command()
def graphs():
    pass


if __name__ == "__main__":
    app()

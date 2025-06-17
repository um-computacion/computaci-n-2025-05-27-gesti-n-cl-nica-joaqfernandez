from src.cli.cli import CLI
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

if __name__ == "__main__":
    cli = CLI()
    cli.ejecutar()
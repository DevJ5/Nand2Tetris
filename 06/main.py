from hackparser import Parser
import sys


def main():
    p = Parser("foo.asm")

    while p.hasMoreCommands():
        p.advance()


if __name__ == "__main__":
    main()

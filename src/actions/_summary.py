import os
import warnings
from typing import List, Union


class Summary:
    def __call__(self, text: str, newline: bool = True):
        warnings.warn("Use core.summary.raw()", DeprecationWarning, stacklevel=2)
        self.add_raw(text, newline)

    # Methods

    @staticmethod
    def clear():
        with open(os.environ["GITHUB_STEP_SUMMARY"], "w") as f:
            f.truncate(0)

    @staticmethod
    def stringify():
        with open(os.environ["GITHUB_STEP_SUMMARY"], "r") as f:
            return f.read()

    # Adders

    @staticmethod
    def add_br():
        write_summary("\n<br>\n")

    @staticmethod
    # Has Context Manager
    def add_code(language: str, code: str):
        write_summary(f'\n<pre lang="{language}"><code>{code}</code></pre>\n')

    @staticmethod
    def add_eol():
        write_summary("")

    @staticmethod
    # Has Context Manager
    def add_details(summary: str, details: str):
        write_summary(f"\n<details><summary>{summary}</summary>{details}</details>\n")

    @staticmethod
    def add_heading(text: str, level: int = 1):
        write_summary(f"\n<h{level}>{text}</h{level}>\n")

    @staticmethod
    def add_hr():
        write_summary("\n<hr>\n")

    @staticmethod
    def add_image(src: str, alt: str, width: int = 100, height: Union[int, str] = "auto"):
        write_summary(f'\n<img src="{src}" alt="{alt}" width="{width}" height="{height}">\n')

    @staticmethod
    def add_link(text: str, href: str):
        write_summary(f'\n<a href="{href}">{text}</a>\n')

    @staticmethod
    # Has Context Manager
    def add_list(items: List[str], ordered: bool = False):
        tag = "ol" if ordered else "ul"
        text = "\n".join([f"<li>{i}</li>" for i in items])
        write_summary(f"\n<{tag}>{text}</{tag}>\n")

    @staticmethod
    def add_quote(text: str, cite: str):
        write_summary(f'\n<blockquote cite="{cite}">{text}</blockquote>\n')

    @staticmethod
    def add_raw(text: str, newline: bool = True):
        write_summary(text, newline)

    @staticmethod
    def add_table(table: List[List[str]]):
        header = "".join(f"<th>{cell}</th>" for cell in table[0])
        rows = "".join("<tr>" + "".join(f"<td>{cell}</td>" for cell in row) + "</tr>" for row in table[1:])
        write_summary(f"\n<table><thead><tr>{header}</tr></thead><tbody>{rows}</tbody></table>\n")

    # Context Managers

    @staticmethod
    def code(language: str = "text"):
        start = f'<pre lang="{language}"><code>'
        return ContextBlock(start, "</code></pre>")

    @staticmethod
    def details(summary: str):
        start = f"<details><summary>{summary}</summary>\n\n"
        return ContextBlock(start, "\n\n</details>")

    @staticmethod
    def list(ordered: bool = False):
        tag = "ol" if ordered else "ul"
        return ContextBlock(f"<{tag}>\n", f"\n</{tag}>", "<li>{0}</li>")


class ContextBlock:
    def __init__(self, start: str, end, fmt="{0}"):
        self.start = start
        self.end = end
        self.fmt = fmt
        self.items: List[str] = []

    def __enter__(self):
        return self.add_text

    def __exit__(self, exc_type, exc_value, traceback):
        # text = os.linesep.join([self.fmt.format(i) for i in self.items])
        text = "\n".join([self.fmt.format(i) for i in self.items])
        result = f"\n{self.start}{text}{self.end}\n"
        write_summary(result)

    def add_text(self, text: str):
        self.items.append(text)


def write_summary(text: str, newline: bool = True):
    # print(text)
    end = "\n" if newline else ""
    with open(os.environ["GITHUB_STEP_SUMMARY"], "a") as f:
        print(text, end=end, file=f)  # type: ignore

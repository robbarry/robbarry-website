import os
import datetime
import csv

import yaml

OLD_WORK_CSV = "/Users/rob/irepos/rob-barry.com/assets/csv/recent_work.csv"
NEW_WORK_PATH = "/Users/rob/repos/robbarry-website/content/work/"


def datify(s):
    # date is of the format 12/7/08
    # we want to convert it to 2008-12-07
    month, day, year = s.split("/")
    year = "20" + year
    return str(datetime.date(int(year), int(month), int(day)))


def slugify(s):
    # we want to replace every non-alphanumeric character with a dash,
    # including spaces.
    # we also want to replace every set of more than one dash with a single dash

    # first, replace spaces with dashes
    s = s.replace(" ", "-")

    # next, replace non-alphanumeric characters with dashes
    s = "".join([c if c.isalnum() else "-" for c in s])

    # finally, replace multiple dashes with a single dash
    while "--" in s:
        s = s.replace("--", "-")

    if s.startswith("-"):
        s = s[1:]

    if s.endswith("-"):
        s = s[:-1]

    return s.lower()


class Article:
    def __init__(self, row):
        self._row = row
        self.title = row["Title"]
        self.date = datify(row["Date"])
        self.slug = "{}-{}".format(self.date, slugify(self.title))
        self.url = row["URL"]
        self.summary = row["Summary"]
        self._categories = None
        self._tags = None

    def categories(self):
        if self._categories is None:
            if "wsj.com" in self.url:
                return ["WSJ"]
            elif "miamiherald.com" in self.url:
                return ["Miami Herald"]
        else:
            return self._categories

    def tags(self):
        return self._tags

    def metadata(self):
        return yaml.dump(
            {
                "title": self.title,
                "date": self.date,
                "categories": self.categories(),
                "tags": self.tags(),
            },
            sort_keys=False,
            indent=4,
        ).strip()

    def content(self):
        content = ["---", self.metadata(), "---", self.summary]
        content += ["", f"Read the full story [here]({self.url})."]
        return "\n".join(content)

    @property
    def filename(self):
        return os.path.join(NEW_WORK_PATH, "{}.md".format(self.slug))

    def load(self):
        if os.path.exists(self.filename):
            # get the yaml front matter
            with open(self.filename, "r") as f:
                lines = f.readlines()
            yaml_lines = []
            switch = 0
            for line in lines:
                if switch == 1:
                    if line.strip() != "---":
                        yaml_lines.append(line.strip())
                if line == "---\n":
                    switch += 1
                if switch == 2:
                    break
            y = "\n".join(yaml_lines)
            try:
                data = yaml.safe_load(y)
                self._categories = data.get("categories", [])
                self._tags = data.get("tags", [])
                self.title = data.get("title", self.title)
                self.date = data.get("date", self.date)
            except:
                pass


with open(OLD_WORK_CSV, "r") as f:
    r = csv.DictReader(f)
    for row in r:
        a = Article(row)
        a.load()
        with open(a.filename, "w") as f:
            f.write(a.content())

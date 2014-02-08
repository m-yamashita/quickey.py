import argparse
import subprocess
import re

# Main routine.
def main():
    args = get_args();
    titles = get_matched_window_titles(args.regexp, args.is_class)
    is_all = args.is_all
    is_reverse = args.is_reverse
    if (is_all and not is_reverse) or (not is_all and is_reverse): titles.reverse()
    if len(titles) <= 0:
        exec_command(args.command)
        return
    for title in titles:
        exec_command('wmctrl -a "%s"' % title.replace('"', '\\"'))
        if not is_all: return

# Get all arguments.
def get_args():
    parser = argparse.ArgumentParser(description="quickey.py is wmctrl's wrapper script.")
    parser.add_argument(
            'regexp',
            help="Regexp for search from all window titles(if '-c' option used, it's WM_CLASS).")
    parser.add_argument(
            'command',
            help="Run this command if nothing matches in window titles(or WM_CLASS) by 'regexp' argument.")
    parser.add_argument(
            '-c', action="store_true", dest="is_class", default=False,
            help="Change regexp target to WM_CLASS from title.")
    parser.add_argument(
            '-a', action="store_true", dest="is_all", default=False,
            help="Activate all windows in matched regexp.")
    parser.add_argument(
            '-r', action="store_true", dest="is_reverse", default=False,
            help="Reverse the order of activation of windows.")
    return parser.parse_args()

# Get window titles
def get_matched_window_titles(target_regexp, is_class):
    regexp_pattern = re.compile(target_regexp)
    wmctrl_option = "lx" if is_class else "l"
    wmctrl_list = exec_command("wmctrl -%s" % wmctrl_option).split('\n')
    titles = []
    for row in wmctrl_list:
        columns = split_columns_by_wmctrl_row(row)
        title = get_title_by_columns(columns, is_class)
        search_target = get_wm_class_by_columns(columns) if is_class else title
        if not regexp_pattern.search(search_target): continue
        titles.append(title)
    return titles;

# Split to column by the row of "wmctrl -l[x]" command result.
def split_columns_by_wmctrl_row(wmctrl_list_row):
    columns = wmctrl_list_row.split(" ")
    while "" in columns: columns.remove("")
    return columns


# Get window title by splitted columns info.
def get_title_by_columns(columns, is_class):
    title_column_index = 5 if is_class else 4
    title = " ".join(columns[title_column_index - 1:])
    return title

# If '-c' option used, get WM_CLASS's string.
def get_wm_class_by_columns(columns):
    target_column_index = 2
    return columns[target_column_index]

# Execute system command by argument.
def exec_command(command):
    return subprocess.Popen(
            command,
            shell=True,
            bufsize=-1,
            stdout=subprocess.PIPE
            ).stdout.read()[:-1]

# Call the main routine.
if __name__ == "__main__":
    main()

# Commands

This document contains all the commands used during the preparation and some additional commands that might be useful later.

## `man`

The most important command is `man`, which is used to display the manual pages for other commands. For example, to view the manual page for the `ls` command, you would run:

```bash
man ls
```

## `find`

`find` is a command-line utility that allows you to search for files and directories in a directory hierarchy based on various criteria such as name, type, size, modification time, and more.

Common usage examples:
- Find files by name:
  ```bash
  find /path/to/search -name "filename.txt"
  ```
- Find files by type (e.g., directories):
  ```bash
  find /path/to/search -type d
  ```
- Find files modified within the last 7 days:
  ```bash
    find /path/to/search -mtime -7
  ```
- Find files larger than 100MB:
  ```bash
  find /path/to/search -size +100M
  ```
- Find files that are bigger than 500 bytes and are not directories:
    ```bash
    find /path/to/search ! -type d -size +500c
    ```
  
### Output formatting options

There are two common options for overwrite the default formatting of the output of the `find` command:
- `printf`: This option allows you to specify a custom format for the output. For example, to display the file name and size in bytes, you can use:
  ```bash
  find /path/to/search -printf "%f %s\n"
  ```
- `ls`: This option allows you to use the `ls` command to format the output. For example, to display the file name and size in a long listing format, you can use:
  ```bash
  find /path/to/search -ls
  ```
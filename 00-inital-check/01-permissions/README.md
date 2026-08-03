# Permissions

In Linux each file has a set of 3 permissions that determine who can read, write, or execute the file.

* The first set is for the owner of the file.
* The second set is for the owner group.
* The third set is for all other users.

When executing `ls -l` there will be a string consisting of "r", "w", "x", and "-" chars.

* r: read permission
* w: write permission
* x: execute permission
* -: no permission

Also listed in `ls -l` is the owner and group of the file.   
The third column contains the name of the owner and the fourth column the name of the group.

### Changing permissions

Permissions can be changed using the `chmod` command.

Using `chmod` permissions can be changed in the symbolic way:

```bash
chmod u+x file.txt  # add execute permission for the owner
chmod g-w file.txt  # remove write permission for the group
chmod o+r file.txt  # add read permission for others
chmod +x file.txt   # add execute permission for all
```

Or more simply using the numeric way:

```bash
chmod 755 file.txt  # set permissions to rwxr-xr-x
chmod 644 file.txt  # set permissions to rw-r--r--
chmod 640 file.txt  # set permissions to rw-r-----
chmod 600 file.txt  # set permissions to rw-------
```
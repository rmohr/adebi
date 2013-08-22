adebi
=====

Automatic commandline debian package dependency installer.
This convenience wrapper allows the creation and installation of dummy
debian packages to satisfy their dependencies by name and version by
commandline. No control-files, etc. are necessary.
It uses and combines the functionalitiy of 'equivs' and 'gdebi' to achive this.

Dependencies
============

```bash
apt-get install equivs gdebi
```

Usage
=====

```bash
usage: adebi [-h] -n NAME -v VERSION -d DEPENDENCIES [DEPENDENCIES ...]
             [-m MAINTAINER] [-e EMAIL] [-s] [-p]

optional arguments:
  -h, --help            show this help message and exit
  -n NAME, --name NAME  package name
  -v VERSION, --version VERSION
                        package version
  -d DEPENDENCIES [DEPENDENCIES ...], --dependencies DEPENDENCIES [DEPENDENCIES ...]
                        package dependencies as comma separated list
  -m MAINTAINER, --maintainer MAINTAINER
                        package maintainer
  -e EMAIL, --email EMAIL
                        email of package maintainer
  -s, --simulate        simulate installation only
  -p, --package-only    creates a debian package and places it in the current
                        directory
```

Examples
=======
As the following examples show, dependencies can be specified in a quite
flexible way. The only import rule is to to put round brackets around version
strings.

```bash
adebi -a Roman -n my-project-build-deps -v 0.1.0 -d 'wget (>>1.2.3), make (<=5.0.0)'
adebi -a Roman -n my-project-build-deps -v 0.1.0 -d 'wget ; make (<=5.0.0)'
adebi -a Roman -n my-project-build-deps -v 0.1.0 -d wget make '(<=5.0.0)'
adebi -a Roman -n my-project-build-deps -v 0.1.0 -d wget 'make(<=5.0.0)'
```

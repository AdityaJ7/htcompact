# HTCompact

[![Build Status](https://travis-ci.org/psyinfra/htcompact.svg?branch=master)](https://travis-ci.org/psyinfra/htcompact)
[![codecov](https://codecov.io/gh/psyinfra/htcompact/branch/master/graph/badge.svg)](https://codecov.io/gh/psyinfra/htcompact)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/d8fff0409968467d855a0efbf2ab8f7d)](https://www.codacy.com/gh/psyinfra/htcompact?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=psyinfra/htcompact&amp;utm_campaign=Badge_Grade)

Search through HTCondor log files to extract information, identify patterns, and
even build graphs (such as resource utilization).

## Installation
**HTCompact** can be installed directly from GitHub using pip:
```
pip install git+https://github.com/psyinfra/htcompact.git
```
I recommend using a [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/),
(if you're not already); it makes life a lot tidier.
```
python3 -m venv ~/htcompact
source ~/htcompact/bin/activate
pip install git+https://github.com/psyinfra/htcompact.git
```

A config file (`setup.conf`) is also provided, to control the default behavior of
htcompact. This is especially useful when installing system-wide, or for
adjusting various warning/error thresholds. See
[CONFIG](https://github.com/psyinfra/htcompact/blob/master/config/README.md) for
more information
#### Notice:
- The script is using the python module htcondor 8.9.8, which is not working on MacOS devices.

## Getting Started
- *htcompact --help* for detailed description
- general use:
`htcompact \[files] \[directories] \[config_file] \[args]`

Let's assume that we have a directory called `logs/` containing these files:
```
logs >
    395_2.log

    job_5991_0.err
    job_5991_0.log
    job_5991_0.out

    job_5992_23.err
    job_5992_23.log
    job_5992_23.out

    ...
```

#### possible configurations:
```
htcompact -h (show a detailed description to all functionalities)

htcompact path_to_logs/job_5991_0.log

htcompact path_to_logs/job_5991_0 path_to_logs/job_5992_23.log

htcompact path_to_logs (run through all files inside the logs directory)

htcompact path_to_logs/job_5991_* -s  (summarize all files starting with: job_5991_)

htcompact path_to_logs/395_2.log --table-format=pretty
```

lets consider we also have a config file (see: [CONFIG](https://github.com/psyinfra/htcompact/blob/master/config/README.md)) \
a default setup.conf should already exist inside the project folder

possible configurations could be reduced to something like:
```
htcompact setup.conf
or
htcompact [files/directories] setup.conf (ignores files/directories set inside the config file)
```

### Testing:
you'll find the tests in: /tests \\
to simply run the tests:
- pytest tests 
More details see: [TESTS](https://github.com/psyinfra/htcompact/blob/master/tests/README.md)

where all arguments, files and directories can be set inside that config file \
see: [CONFIG](https://github.com/psyinfra/htcompact/blob/master/config/README.md)

Examples:

- default mode:
    ```
    The job procedure of : ../logs/job_5991_0.log
    +-------------------+--------------------+
    | Executing on Host |      cpu: 3        |
    |       Port        |       96186        |
    |      Runtime      |      0:00:04       |
    | Termination State | Normal termination |
    |   Return Value    |         0          |
    +-------------------+--------------------+
    +------------+-------+-----------+-----------+
    | Rescources | Usage | Requested | Allocated |
    +------------+-------+-----------+-----------+
    |    Cpu     |   0   |     1     |     1     |
    |    Disk    | 5000  |   5000    |  3770642  |
    |   Memory   |   0   |   6000    |   6016    |
    +------------+-------+-----------+-----------+
    ```
- summarizer mode:

    ![Example](https://github.com/psyinfra/htcompact/blob/master/examples/example_summary_mode.png)

- analyser mode:

    ![Example](https://github.com/psyinfra/htcompact/blob/master/examples/example_analyser_mode.png)

- analysed summary mode:

    ![Example](https://github.com/psyinfra/htcompact/blob/master/examples/example_analysed_summary_mode.png)

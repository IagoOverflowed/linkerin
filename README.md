# ![logo](https://github.com/IagoOverflowed/linkerin/blob/86c0d9c8d9ecab91ac98bef45ba824bc61f7eb97/logo50.png) LinkerIN

A simple yet useful link miner

# About

LinkerIN can detect links that use the `http` and `https` schema inside double quotation marks strings<br>
it also can do a deep dive meaning that it will also try to find links in the links that he finds

# Usage

> before you start make sure you have python 3.9 and the libs `requests` and `validators`installed.

to start simply run it. if you want to customize the behaivor run using the command line and use the following arguments

* `--limit [int]`          : defines the max of passes
* `--limit-per-pass [int]` : defines the max of links per pass
* `--delay [float]`        : determines the delay between each link
* `--deep-dive [1|0]`      : determines if the program should do a deep dive
* '--starting-at'          : determines the starting position. when set the `Starting position?` prompt will be skipped

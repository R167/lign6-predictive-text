#!/bin/sh

pandoc -s writeup/writeup.md --filter=pandoc-codeblock-include -o writeup.pdf

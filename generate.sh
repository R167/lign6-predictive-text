#!/bin/sh

pandoc -s WRITEUP.md --filter=pandoc-codeblock-include -o writeup.pdf

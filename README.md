txgetdns
========

getdnsapi bindings for twisted


Requirements
============
* https://github.com/getdnsapi/

Tests
=====
Install getdnsapi and if necessary specify its library and include paths so that CFFI can find the headers and .so files.

```
LIBRARY_PATH=${HOME}/.local/lib C_INCLUDE_PATH=${HOME}/.local/include trial  txgetdns
```

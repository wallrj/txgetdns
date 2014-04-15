# -*- test-case-name: txgetdns.test.test_bindings -*-
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

"""
"""

from cryptography.hazmat.bindings.utils import build_ffi

ffi, lib = build_ffi(
    module_prefix='txgetdns.',
    modules=['getdns'],
    pre_include="",
    post_include="",
    libraries=['getdns'])

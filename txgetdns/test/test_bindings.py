# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

from twisted.trial.unittest import SynchronousTestCase

from txgetdns.bindings import lib, ffi

@ffi.callback("""
void (*getdns_callback_t) (getdns_context *context,
    getdns_callback_type_t callback_type,
    getdns_dict * response,
    void *userarg, getdns_transaction_t transaction_id)
""")
def callback():
    pass

class BindingsTests(SynchronousTestCase):
    def test_address(self):
        """
        """
        context = ffi.new("getdns_context *")
        lib.getdns_context_create(context, 1)
        d = ffi.new("getdns_dict *")
        tid = ffi.new("getdns_transaction_t *")
        r = lib.getdns_address(context, 'example.com', d, "userarg", tid, callback)
        self.fail(r)

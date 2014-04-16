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
        context = ffi.new("getdns_context *[1]")
        ret = lib.getdns_context_create(context, 1)
        if ret != lib.GETDNS_RETURN_GOOD:
            self.fail("Trying to create the context failed")

        name = b"www.example.coms"
        request_type = lib.GETDNS_RRTYPE_A
        extensions = lib.getdns_dict_create()
        ret = lib.getdns_dict_set_int(extensions, "return_both_v4_and_v6", lib.GETDNS_EXTENSION_TRUE);
        if ret != lib.GETDNS_RETURN_GOOD:
            lib.getdns_dict_destroy(extensions);
            lib.getdns_context_destroy(context);
            self.fail("Trying to set an extension do both IPv4 and IPv6 failed: %d\n" % (ret,))

        response = lib.getdns_dict_create()

        ret = lib.getdns_general_sync(context[0], name, request_type, extensions[0], response);
        if ret == lib.GETDNS_RETURN_BAD_DOMAIN_NAME:
            lib.getdns_dict_destroy(response);
            lib.getdns_dict_destroy(extensions);
            lib.getdns_context_destroy(context);
            self.fail("A bad domain name was used: %s. Exiting.\n" % (name,))
        return
        # Be sure the search returned something
        error = ffi.new("uint32_t *")
        ret = lib.getdns_dict_get_int(response[0], "status", error)  # Ignore any error
        if error != lib.GETDNS_RESPSTATUS_GOOD:  # If the search didn't return "good"
            lib.getdns_dict_destroy(response);
            lib.getdns_dict_destroy(extensions);
            lib.getdns_context_destroy(context);
            self.fail("The search had no results, and a return value of %d. Exiting.\n" % (error,))
        return
        # getdns_list * just_the_addresses_ptr;
        # this_ret = getdns_dict_get_list(this_response, "just_address_answers", &just_the_addresses_ptr);  // Ignore any error
        # size_t num_addresses;
        # this_ret = getdns_list_get_length(just_the_addresses_ptr, &num_addresses);  // Ignore any error
        # /* Go through each record */
        # for ( size_t rec_count = 0; rec_count < num_addresses; ++rec_count )
        # {
        #     getdns_dict * this_address;
        #     this_ret = getdns_list_get_dict(just_the_addresses_ptr, rec_count, &this_address);  // Ignore any error
        #     /* Just print the address */
        #     getdns_bindata * this_address_data;
        #     this_ret = getdns_dict_get_bindata(this_address, "address_data", &this_address_data); // Ignore any error
        #     char *this_address_str = getdns_display_ip_address(this_address_data);
        #     printf("The address is %s\n", this_address_str);
        #     free(this_address_str);
        # }

        r = lib.getdns_address_sync(context[0], 'example.com', extensions[0], response)
        error = ffi.new("uint32_t *")
        lib.getdns_dict_get_int(response[0], "status", error);
        self.fail(error[0])

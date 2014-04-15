# -*- test-case-name: txgetdns.test.test_bindings -*-
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

INCLUDES = """
#include <getdns/getdns.h>
"""

TYPES = """
/* Callback Type Variables */
typedef enum getdns_callback_type_t {
        GETDNS_CALLBACK_COMPLETE = 700,
        GETDNS_CALLBACK_CANCEL = 701,
        GETDNS_CALLBACK_TIMEOUT = 702,
        GETDNS_CALLBACK_ERROR = 703
} getdns_callback_type_t;


/* Return values */
typedef enum getdns_return_t {
        GETDNS_RETURN_GOOD = 0,
        GETDNS_RETURN_GENERIC_ERROR = 1,
        GETDNS_RETURN_BAD_DOMAIN_NAME = 300,
        GETDNS_RETURN_BAD_CONTEXT = 301,
        GETDNS_RETURN_CONTEXT_UPDATE_FAIL = 302,
        GETDNS_RETURN_UNKNOWN_TRANSACTION = 303,
        GETDNS_RETURN_NO_SUCH_LIST_ITEM = 304,
        GETDNS_RETURN_NO_SUCH_DICT_NAME = 305,
        GETDNS_RETURN_WRONG_TYPE_REQUESTED = 306,
        GETDNS_RETURN_NO_SUCH_EXTENSION = 307,
        GETDNS_RETURN_EXTENSION_MISFORMAT = 308,
        GETDNS_RETURN_DNSSEC_WITH_STUB_DISALLOWED = 309,
        GETDNS_RETURN_MEMORY_ERROR = 310,
        GETDNS_RETURN_INVALID_PARAMETER = 311
} getdns_return_t;

typedef ... *getdns_context;
typedef uint64_t getdns_transaction_t;
typedef ... *getdns_dict;

typedef void (*getdns_callback_t) (getdns_context *context,
    getdns_callback_type_t callback_type,
    getdns_dict * response,
    void *userarg, getdns_transaction_t transaction_id);

"""

FUNCTIONS = """
getdns_return_t
getdns_address(
    getdns_context *context,
    const char *name,
    getdns_dict *extensions,
    void *userarg,
    getdns_transaction_t * transaction_id,
    getdns_callback_t callbackfn);

getdns_return_t
getdns_context_create(getdns_context ** context, int set_from_os);
"""

MACROS = """
"""

CUSTOMIZATIONS = """
"""

CONDITIONAL_NAMES = {}

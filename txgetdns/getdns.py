# -*- test-case-name: txgetdns.test.test_bindings -*-
# Copyright (c) Twisted Matrix Laboratories.
# See LICENSE for details.

INCLUDES = """
#include <getdns/getdns.h>
#include <getdns/getdns_extra.h>
#include <getdns/getdns_ext_libevent.h>
"""

TYPES = """

#define GETDNS_RRTYPE_A         ...
#define GETDNS_RRTYPE_NS        ...
#define GETDNS_RRTYPE_MD        ...
#define GETDNS_RRTYPE_MF        ...
#define GETDNS_RRTYPE_CNAME     ...
#define GETDNS_RRTYPE_SOA       ...
#define GETDNS_RRTYPE_MB        ...
#define GETDNS_RRTYPE_MG        ...
#define GETDNS_RRTYPE_MR        ...
#define GETDNS_RRTYPE_NULL      ...
#define GETDNS_RRTYPE_WKS       ...
#define GETDNS_RRTYPE_PTR       ...
#define GETDNS_RRTYPE_HINFO     ...
#define GETDNS_RRTYPE_MINFO     ...
#define GETDNS_RRTYPE_MX        ...
#define GETDNS_RRTYPE_TXT       ...
#define GETDNS_RRTYPE_RP        ...
#define GETDNS_RRTYPE_AFSDB     ...
#define GETDNS_RRTYPE_X25       ...
#define GETDNS_RRTYPE_ISDN      ...
#define GETDNS_RRTYPE_RT        ...
#define GETDNS_RRTYPE_NSAP      ...
#define GETDNS_RRTYPE_SIG       ...
#define GETDNS_RRTYPE_KEY       ...
#define GETDNS_RRTYPE_PX        ...
#define GETDNS_RRTYPE_GPOS      ...
#define GETDNS_RRTYPE_AAAA      ...
#define GETDNS_RRTYPE_LOC       ...
#define GETDNS_RRTYPE_NXT       ...
#define GETDNS_RRTYPE_EID       ...
#define GETDNS_RRTYPE_NIMLOC    ...
#define GETDNS_RRTYPE_SRV       ...
#define GETDNS_RRTYPE_ATMA      ...
#define GETDNS_RRTYPE_NAPTR     ...
#define GETDNS_RRTYPE_KX        ...
#define GETDNS_RRTYPE_CERT      ...
#define GETDNS_RRTYPE_A6        ...
#define GETDNS_RRTYPE_DNAME     ...
#define GETDNS_RRTYPE_SINK      ...
#define GETDNS_RRTYPE_OPT       ...
#define GETDNS_RRTYPE_APL       ...
#define GETDNS_RRTYPE_DS        ...
#define GETDNS_RRTYPE_SSHFP     ...
#define GETDNS_RRTYPE_IPSECKEY  ...
#define GETDNS_RRTYPE_RRSIG     ...
#define GETDNS_RRTYPE_NSEC      ...
#define GETDNS_RRTYPE_DNSKEY    ...
#define GETDNS_RRTYPE_DHCID     ...
#define GETDNS_RRTYPE_NSEC3     ...
#define GETDNS_RRTYPE_NSEC3PARAM ...
#define GETDNS_RRTYPE_TLSA      ...
#define GETDNS_RRTYPE_HIP       ...
#define GETDNS_RRTYPE_NINFO     ...
#define GETDNS_RRTYPE_RKEY      ...
#define GETDNS_RRTYPE_TALINK    ...
#define GETDNS_RRTYPE_CDS       ...
#define GETDNS_RRTYPE_SPF       ...
#define GETDNS_RRTYPE_UINFO     ...
#define GETDNS_RRTYPE_UID       ...
#define GETDNS_RRTYPE_GID       ...
#define GETDNS_RRTYPE_UNSPEC    ...
#define GETDNS_RRTYPE_NID       ...
#define GETDNS_RRTYPE_L32       ...
#define GETDNS_RRTYPE_L64       ...
#define GETDNS_RRTYPE_LP        ...
#define GETDNS_RRTYPE_EUI48     ...
#define GETDNS_RRTYPE_EUI64     ...
#define GETDNS_RRTYPE_TKEY      ...
#define GETDNS_RRTYPE_TSIG      ...
#define GETDNS_RRTYPE_IXFR      ...
#define GETDNS_RRTYPE_AXFR      ...
#define GETDNS_RRTYPE_MAILB     ...
#define GETDNS_RRTYPE_MAILA     ...
#define GETDNS_RRTYPE_ANY       ...
#define GETDNS_RRTYPE_URI       ...
#define GETDNS_RRTYPE_CAA       ...
#define GETDNS_RRTYPE_TA        ...
#define GETDNS_RRTYPE_DLV       ...

#define GETDNS_EXTENSION_TRUE  ...
#define GETDNS_EXTENSION_TRUE_TEXT ...
#define GETDNS_EXTENSION_FALSE ...
#define GETDNS_EXTENSION_FALSE_TEXT ...


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


/* Namespace types */
typedef enum getdns_namespace_t {
        GETDNS_NAMESPACE_DNS = 500,
        GETDNS_NAMESPACE_LOCALNAMES = 501,
        GETDNS_NAMESPACE_NETBIOS = 502,
        GETDNS_NAMESPACE_MDNS = 503,
        GETDNS_NAMESPACE_NIS = 504
} getdns_namespace_t;


/* Resolution types */
typedef ... getdns_resolution_t;

/* Redirect policies */
typedef enum getdns_redirects_t {
        GETDNS_REDIRECTS_FOLLOW = 530,
        GETDNS_REDIRECTS_DO_NOT_FOLLOW = 531
} getdns_redirects_t;


/* Transport arrangements */
typedef enum getdns_transport_t {
        GETDNS_TRANSPORT_UDP_FIRST_AND_FALL_BACK_TO_TCP = 540,
        GETDNS_TRANSPORT_UDP_ONLY = 541,
        GETDNS_TRANSPORT_TCP_ONLY = 542,
        GETDNS_TRANSPORT_TCP_ONLY_KEEP_CONNECTIONS_OPEN = 543
} getdns_transport_t;


/* Suffix appending methods */
typedef enum getdns_append_name_t {
        GETDNS_APPEND_NAME_ALWAYS = 550,
        GETDNS_APPEND_NAME_ONLY_TO_SINGLE_LABEL_AFTER_FAILURE = 551,
        GETDNS_APPEND_NAME_ONLY_TO_MULTIPLE_LABEL_NAME_AFTER_FAILURE = 552,
        GETDNS_APPEND_NAME_NEVER = 553
} getdns_append_name_t;


/* Context codes */
typedef enum getdns_context_code_t {
        GETDNS_CONTEXT_CODE_NAMESPACES = 600,
        GETDNS_CONTEXT_CODE_RESOLUTION_TYPE = 601,
        GETDNS_CONTEXT_CODE_FOLLOW_REDIRECTS = 602,
        GETDNS_CONTEXT_CODE_UPSTREAM_RECURSIVE_SERVERS = 603,
        GETDNS_CONTEXT_CODE_DNS_ROOT_SERVERS = 604,
        GETDNS_CONTEXT_CODE_DNS_TRANSPORT = 605,
        GETDNS_CONTEXT_CODE_LIMIT_OUTSTANDING_QUERIES = 606,
        GETDNS_CONTEXT_CODE_APPEND_NAME = 607,
        GETDNS_CONTEXT_CODE_SUFFIX = 608,
        GETDNS_CONTEXT_CODE_DNSSEC_TRUST_ANCHORS = 609,
        GETDNS_CONTEXT_CODE_EDNS_MAXIMUM_UDP_PAYLOAD_SIZE = 610,
        GETDNS_CONTEXT_CODE_EDNS_EXTENDED_RCODE = 611,
        GETDNS_CONTEXT_CODE_EDNS_VERSION = 612,
        GETDNS_CONTEXT_CODE_EDNS_DO_BIT = 613,
        GETDNS_CONTEXT_CODE_DNSSEC_ALLOWED_SKEW = 614,
        GETDNS_CONTEXT_CODE_MEMORY_FUNCTIONS = 615,
        GETDNS_CONTEXT_CODE_TIMEOUT = 616
} getdns_context_code_t;


/* Callback Type Variables */
typedef enum getdns_callback_type_t {
        GETDNS_CALLBACK_COMPLETE = 700,
        GETDNS_CALLBACK_CANCEL = 701,
        GETDNS_CALLBACK_TIMEOUT = 702,
        GETDNS_CALLBACK_ERROR = 703
} getdns_callback_type_t;




typedef struct getdns_context getdns_context;
typedef uint64_t getdns_transaction_t;
/**
 * used to check data types within complex types (dict, list)
 */
typedef enum getdns_data_type
{
        t_dict, t_list, t_int, t_bindata
} getdns_data_type;
typedef struct getdns_bindata
{
        size_t size;
        uint8_t *data;
} getdns_bindata;

/**
 * getdns dictionary data type
 * Use helper functions getdns_dict_* to manipulate and iterate dictionaries
 */
typedef struct getdns_dict getdns_dict;

/**
 * getdns list data type
 * Use helper functions getdns_list_* to manipulate and iterate lists
 * Indexes are 0 based.
 */
typedef struct getdns_list getdns_list;

/**
 * translate an error code to a string value, not in the original api description
 * but seems like a nice thing to have
 * @param err return code from GETDNS_RETURN_* defines
 * @param buf buffer to which to copy the error string
 * @param buflen length of buf
 * @return GETDNS_RETURN_GOOD on success
 */
getdns_return_t getdns_strerror(getdns_return_t err, char *buf, size_t buflen);

/**
 * get the length of the specified list (returned in *answer)
 * @param this_list list of any of the supported data types
 * @param answer number of valid items in the list
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_LIST_ITEM if list is not valid or params are NULL
 */
getdns_return_t getdns_list_get_length(const getdns_list *this_list,
    size_t * answer);
/**
 * get the enumerated data type of the indexed list item
 * @param this_list the list from which to fetch the data type
 * @param index the item in the list from which to fetch the data type
 * @param *answer assigned the value of the data type on success
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_LIST_ITEM if the index is out of range or the list is NULL
 */
getdns_return_t getdns_list_get_data_type(const getdns_list *this_list,
    size_t index, getdns_data_type * answer);
/**
 * retrieve the dictionary value of the specified list item, the caller must not free
 * storage associated with the return value.  When the list is destroyed this
 * dict data is also free()'d - keep this in mind when using this function.
 * @param this_list the list from which to fetch the value
 * @param index the item in the list from which to fetch the value
 * @param **answer assigned a pointer to the dict value of the indexed element
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_LIST_ITEM if the index is out of range or the list is NULL
 * @return GETDNS_RETURN_WRONG_TYPE_REQUESTED if the data type does not match the contents of the indexed item
 */
getdns_return_t getdns_list_get_dict(const getdns_list *this_list, size_t index,
    getdns_dict **answer);

/**
 * retrieve the list value of the specified list item, the caller must not free
 * storage associated with the return value.  When the list is destroyed any
 * list data is also free()'d - keep this in mind when using this function.
 * @param this_list the list from which to fetch the value
 * @param index the item in the list from which to fetch the value
 * @param **answer assigned a pointer to the list value of the indexed element
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_LIST_ITEM if the index is out of range or the list is NULL
 * @return GETDNS_RETURN_WRONG_TYPE_REQUESTED if the data type does not match the contents of the indexed item
 */
getdns_return_t getdns_list_get_list(const getdns_list *this_list, size_t index,
    getdns_list **answer);
/**
 * retrieve the binary data value of the specified list item, the caller must not
 * free storage associated with the return value.  When the list is destroyed any
 * bindata data is also free()'d - keep this in mind when using this function.
 * @param this_list the list from which to fetch the value
 * @param index the item in the list from which to fetch the value
 * @param **answer assigned a pointer to the list value of the indexed element
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_LIST_ITEM if the index is out of range or the list is NULL
 * @return GETDNS_RETURN_WRONG_TYPE_REQUESTED if the data type does not match the contents of the indexed item
 */
getdns_return_t getdns_list_get_bindata(const getdns_list *this_list, size_t index,
    getdns_bindata **answer);
/**
 * retrieve the integer value of the specified list item
 * @param this_list the list from which to fetch the item
 * @param index the index of the element in the list to fetch from
 * @param *answer assigned the integer value of the indexed element
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_LIST_ITEM if the index is out of range or the list is NULL
 * @return GETDNS_RETURN_WRONG_TYPE_REQUESTED if the data type does not match the contents of the indexed item
 */
getdns_return_t getdns_list_get_int(const getdns_list *this_list, size_t index,
    uint32_t * answer);

/**
 * fetch a list of names from the dictionary, this list must be freed by the caller
 * via a call to getdns_list_destroy
 * @param this_dict dictionary from which to produce the list of names
 * @param **answer a pointer to the new list will be assigned to *answer
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_DICT_NAME if dict is invalid or empty
 */
getdns_return_t getdns_dict_get_names(const getdns_dict *this_dict,
    getdns_list **answer);
/**
 * fetch the data type for the data associated with the specified name
 * @param this_dict dictionary from which to fetch the data type
 * @param name a name/key value to look up in the dictionary
 * @param *answer data type will be stored at this address
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_DICT_NAME if dict is invalid or name does not exist
 */
getdns_return_t getdns_dict_get_data_type(const getdns_dict *this_dict,
    const char *name, getdns_data_type * answer);
/**
 * fetch the dictionary associated with the specified name, the dictionary should
 * not be free()'d by the caller, it will be freed when the parent dictionary is
 * free()'d
 * @param this_dict dictionary from which to fetch the dictionary
 * @param name a name/key value to look up in the dictionary
 * @param **answer a copy of the dictionary will be stored at this address
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_DICT_NAME if dict is invalid or name does not exist
 */
getdns_return_t getdns_dict_get_dict(const getdns_dict *this_dict,
    const char *name, getdns_dict **answer);
/**
 * fetch the list associated with the specified name
 * the list should not be free()'d by the caller, when the dictionary is destroyed
 * the list will also be destroyed
 * @param this_dict dictionary from which to fetch the list
 * @param name a name/key value to look up in the dictionary
 * @param **answer a copy of the list will be stored at this address
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_DICT_NAME if dict is invalid or name does not exist
 */
getdns_return_t getdns_dict_get_list(const getdns_dict *this_dict,
    const char *name, getdns_list **answer);
/**
 * fetch the bindata associated with the specified name, the bindata should not be
 * free()'d by the caller
 * @param this_dict dictionary from which to fetch the bindata
 * @param name a name/key value to look up in the dictionary
 * @param **answer a copy of the bindata will be stored at this address
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_DICT_NAME if dict is invalid or name does not exist
 */
getdns_return_t getdns_dict_get_bindata(const getdns_dict *this_dict,
    const char *name, getdns_bindata **answer);
/**
 * fetch the integer value associated with the specified name
 * @param this_dict dictionary from which to fetch the integer
 * @param name a name/key value to look up in the dictionary
 * @param *answer the integer will be stored at this address
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_DICT_NAME if dict is invalid or name does not exist
 */
getdns_return_t getdns_dict_get_int(const getdns_dict *this_dict,
    const char *name, uint32_t * answer);

/**
 * create a new list with no items
 * @return pointer to an allocated list, NULL if insufficient memory
 */
getdns_list *getdns_list_create();
getdns_list *getdns_list_create_with_context(getdns_context *context);
getdns_list *getdns_list_create_with_memory_functions(
    void *(*malloc) (size_t),
    void *(*realloc) (void *, size_t),
    void (*free) (void *)
);
getdns_list *getdns_list_create_with_extended_memory_functions(
    void *userarg,
    void *(*malloc) (void *userarg, size_t),
    void *(*realloc) (void *userarg, void *, size_t),
    void (*free) (void *userarg, void *)
);

/**
 * free memory allocated to the list (also frees all children of the list)
 * note that lists and bindata retrieved from the list via the getdns_list_get_*
 * helper functions will be destroyed as well - if you fetched them previously
 * you MUST copy those instances BEFORE you destroy the list else
 * unpleasant things will happen at run-time
 */
void getdns_list_destroy(getdns_list *this_list);

/**
 * assign the child_dict to an item in a parent list, the parent list copies
 * the child dict and will free the copy when the list is destroyed
 * @param this_list list containing the item to which child_list is to be assigned
 * @param index index of the item within list to which child_list is to be assigned
 * @param *child_list list to assign to the item
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_LIST_ITEM if index is out of range, or list is NULL
 */
getdns_return_t getdns_list_set_dict(getdns_list *this_list, size_t index,
    const getdns_dict *child_dict);

/**
 * assign the child_list to an item in a parent list, the parent list copies
 * the child list and will free the copy when the list is destroyed
 * @param this_list list containing the item to which child_list is to be assigned
 * @param index index of the item within list to which child_list is to be assigned
 * @param *child_list list to assign to the item
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_LIST_ITEM if index is out of range, or list is NULL
 */
getdns_return_t getdns_list_set_list(getdns_list *this_list, size_t index,
    const getdns_list *child_list);
/**
 * assign the child_bindata to an item in a parent list, the parent list copies
 * the child data and will free the copy when the list is destroyed
 * @param this_list list contiaining the item to which child_list is to be assigned
 * @param index index of the item within list to which child_list is to be assigned
 * @param *child_bindata data to assign to the item
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_LIST_ITEM if index is out of range, or list is NULL
 */
getdns_return_t getdns_list_set_bindata(getdns_list *this_list, size_t index,
    const getdns_bindata *child_bindata);
/**
 * set the integer value of the indexed item (zero based index)
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_LIST_ITEM if index is out of range, or list is NULL
 */
getdns_return_t getdns_list_set_int(getdns_list *this_list, size_t index,
    uint32_t child_uint32);

/**
 * create a new dictionary with no items
 * @return pointer to an allocated dictionary, NULL if insufficient memory
 */
getdns_dict *getdns_dict_create();
getdns_dict *getdns_dict_create_with_context(getdns_context *context);
getdns_dict *getdns_dict_create_with_memory_functions(
    void *(*malloc) (size_t),
    void *(*realloc) (void *, size_t),
    void (*free) (void *)
);
getdns_dict *getdns_dict_create_with_extended_memory_functions(
    void *userarg,
    void *(*malloc) (void *userarg, size_t),
    void *(*realloc) (void *userarg, void *, size_t),
    void (*free) (void *userarg, void *)
);

/**
 * destroy a dictionary and all items within that dictionary
 * be aware that if you have fetched any data from the dictionary it will
 * no longer be available (you are likely to experience bad things if you try)
 */
void getdns_dict_destroy(getdns_dict *this_dict);

getdns_return_t getdns_dict_set_dict(getdns_dict *this_dict,
    const char *name, const getdns_dict *child_dict);
/**
 * create a new entry in the dictionary, or replace the value of an existing entry
 * this routine makes a copy of the child_list
 * @param this_dict dictionary in which to add or change the value
 * @param name key that identifies which item in the dictionary to add/change
 * @param child_list value to assign to the node identified by name
 * @return GETDNS_RETURN_GOOD on success
 */
getdns_return_t getdns_dict_set_list(getdns_dict *this_dict,
    const char *name, const getdns_list *child_list);
/**
 * create a new entry in the dictionary, or replace the value of an existing entry
 * this routine makes a copy of the child_bindata
 * @param this_dict dictionary in which to add or change the value
 * @param name key that identifies which item in the dictionary to add/change
 * @param child_bindata value to assign to the node identified by name
 * @return GETDNS_RETURN_GOOD on success
 */
getdns_return_t getdns_dict_set_bindata(getdns_dict *this_dict,
    const char *name, const getdns_bindata *child_bindata);
/**
 * create a new entry in the dictionary, or replace the value of an existing entry
 * @param this_dict dictionary in which to add or change the value
 * @param name key that identifies which item in the dictionary to add/change
 * @param child_uint32 value to assign to the node identified by name
 * @return GETDNS_RETURN_GOOD on success
 */
getdns_return_t getdns_dict_set_int(getdns_dict *this_dict, const char *name,
    uint32_t child_uint32);

/**
 * remove the value associated with the specified name
 * @param this_dict dictionary from which to fetch the integer
 * @param name a name/key value to look up in the dictionary
 * @return GETDNS_RETURN_GOOD on success
 * @return GETDNS_RETURN_NO_SUCH_DICT_NAME if dict is invalid or name does not exist
 */
getdns_return_t getdns_dict_remove_name(getdns_dict *this_dict, const char *name);

//
// getdns_extra.h
//
/* Enable the return_dnssec_status extension on every request.
   value is either GETDNS_EXTENSION_TRUE or GETDNS_EXTENSION_FALSE
   returns GETDNS_RETURN_GOOD on success or GETDNS_RETURN_INVALID_PARAMETER
   if context or value is invalid */
getdns_return_t getdns_context_set_return_dnssec_status(getdns_context* context, int enabled);

/* dict util */
/* set a string as bindata */
getdns_return_t getdns_dict_util_set_string(struct getdns_dict * dict, char *name,
    const char *value);

/* get a string from a dict.  the result must be freed if valid */
getdns_return_t getdns_dict_util_get_string(struct getdns_dict * dict, char *name,
    char **result);

/* Async support */
uint32_t getdns_context_get_num_pending_requests(getdns_context* context, struct timeval* next_timeout);

/* get the fd */
int getdns_context_fd(getdns_context* context);

/* process async reqs */
getdns_return_t getdns_context_process_async(getdns_context* context);

/* tells underlying unbound to use background threads or fork */
getdns_return_t getdns_context_set_use_threads(getdns_context* context, int use_threads);

/* extensions */
typedef getdns_return_t (*getdns_timeout_callback) (void* userarg);

/* context timeout data */
typedef ... getdns_timeout_data_t;

/* call the extension when the data needs to be cleaned up */
typedef getdns_return_t (*getdns_eventloop_cleanup_t)(struct getdns_context* context, void* eventloop_data);

/* call the extension to schedule a timer.  Any timer data that needs to be tracked should be
   stored in eventloop_timer */
typedef getdns_return_t (*getdns_eventloop_schedule_timeout_t)(struct getdns_context* context,
    void* eventloop_data, uint16_t timeout,
    getdns_timeout_data_t* timeout_data,
    void** eventloop_timer);

/* call the extension to free a timer.  The timer passed in is the same as that returned in
   the schedule timeout */
typedef getdns_return_t (*getdns_eventloop_clear_timeout_t)(struct getdns_context* context,
    void* eventloop_data, void* eventloop_timer);

/* call the extension to tell it that the number of outbound requests changed.  This is called
   when an async request is submitted or canceled by the user */
typedef getdns_return_t (*getdns_eventloop_request_count_changed_t)(struct getdns_context* context,
    uint32_t request_count, void* eventloop_data);

typedef struct getdns_eventloop_extension {
    getdns_eventloop_cleanup_t cleanup_data;
    getdns_eventloop_schedule_timeout_t schedule_timeout;
    getdns_eventloop_clear_timeout_t clear_timeout;
    getdns_eventloop_request_count_changed_t request_count_changed;
} getdns_eventloop_extension;

/* set an event loop extension on the context */
getdns_return_t
getdns_extension_set_eventloop(struct getdns_context* context,
    getdns_eventloop_extension* extension, void* extension_data);

void*
getdns_context_get_extension_data(struct getdns_context* context);

/* detach the eventloop from the context */
getdns_return_t
getdns_extension_detach_eventloop(struct getdns_context* context);

//
// context.h
//
/** function pointer typedefs */
typedef void (*getdns_update_callback) (struct getdns_context *,
    getdns_context_code_t);



/** internal functions **/
/**
 * Sets up the unbound contexts with stub or recursive behavior
 * if needed.
 * @param context previously initialized getdns_context
 * @param usenamespaces if 0 then only use the DNS, else use context namespace list
 * @return GETDNS_RETURN_GOOD on success
 */
getdns_return_t getdns_context_prepare_for_resolution(struct getdns_context *context,
 int usenamespaces);

/* track an outbound request */
getdns_return_t getdns_context_track_outbound_request(struct getdns_dns_req
    *req);
/* clear the outbound request from being tracked - does not cancel it */
getdns_return_t getdns_context_clear_outbound_request(struct getdns_dns_req
    *req);

getdns_return_t getdns_context_request_timed_out(struct getdns_dns_req
    *req);

/* cancel callback internal - flag to indicate if req should be freed and callback fired */
getdns_return_t getdns_context_cancel_request(struct getdns_context *context,
    getdns_transaction_t transaction_id, int fire_callback);

char *getdns_strdup(const struct mem_funcs *mfs, const char *str);

struct getdns_bindata *getdns_bindata_copy(
    struct mem_funcs *mfs,
    const struct getdns_bindata *src);

void getdns_bindata_destroy(
    struct mem_funcs *mfs,
    struct getdns_bindata *bindata);

/* timeout scheduling */
getdns_return_t getdns_context_schedule_timeout(struct getdns_context* context,
    getdns_transaction_t id, uint16_t timeout, getdns_timeout_callback callback,
    void* userarg);

getdns_return_t getdns_context_clear_timeout(struct getdns_context* context,
    getdns_transaction_t id);

int filechg_check(struct getdns_context *context, struct filechg *fchg);

/* Callback arguments */
typedef void (*getdns_callback_t) (getdns_context *context,
    getdns_callback_type_t callback_type,
    getdns_dict * response,
    void *userarg, getdns_transaction_t transaction_id);


"""

FUNCTIONS = """

/* Function definitions */

getdns_return_t
getdns_general(getdns_context *context,
    const char *name,
    uint16_t request_type,
    getdns_dict *extensions,
    void *userarg,
    getdns_transaction_t * transaction_id, getdns_callback_t callbackfn);
getdns_return_t
getdns_address(getdns_context *context,
    const char *name,
    getdns_dict *extensions,
    void *userarg,
    getdns_transaction_t * transaction_id, getdns_callback_t callbackfn);
getdns_return_t
getdns_hostname(getdns_context *context,
    getdns_dict *address,
    getdns_dict *extensions,
    void *userarg,
    getdns_transaction_t * transaction_id, getdns_callback_t callbackfn);
getdns_return_t
getdns_service(getdns_context *context,
    const char *name,
    getdns_dict *extensions,
    void *userarg,
    getdns_transaction_t * transaction_id, getdns_callback_t callbackfn);

getdns_return_t
getdns_context_create(getdns_context ** context, int set_from_os);

getdns_return_t
getdns_context_create_with_memory_functions(
    getdns_context ** context,
    int set_from_os,
    void *(*malloc) (size_t),
    void *(*realloc) (void *, size_t),
    void (*free) (void *)
);

getdns_return_t
getdns_context_create_with_extended_memory_functions(
    getdns_context **context,
    int set_from_os,
    void *userarg,
    void *(*malloc) (void *userarg, size_t),
    void *(*realloc) (void *userarg, void *, size_t),
    void (*free) (void *userarg, void *)
);

void getdns_context_destroy(getdns_context *context);

getdns_return_t
getdns_cancel_callback(getdns_context *context,
    getdns_transaction_t transaction_id);

/**
 * \defgroup syncfuns Synchronous API functions that do not use callbacks
 * These functions do not use callbacks, when the application calls one of these
 * functions the library retrieves all of the data before returning.  Return
 * values are exactly the same as if you had used a callback with the
 * asynchronous functions.
 * @{
 */

/**
 * retrieve general DNS data
 * @param context pointer to a previously created context to be used for this call
 * @param name the ASCII based domain name to lookup
 * @param request_type RR type for the query, e.g. GETDNS_RR_TYPE_NS
 * @param extensions dict data structures, NULL to use no extensions
 * @param response response
 * @return GETDNS_RETURN_GOOD on success
 */
getdns_return_t
getdns_general_sync(getdns_context *context,
    const char *name,
    uint16_t request_type,
    getdns_dict *extensions,
    getdns_dict **response);

/**
 * retrieve address assigned to a DNS name
 * @param context pointer to a previously created context to be used for this call
 * @param name the ASCII based domain name to lookup
 * @param extensions dict data structures, NULL to use no extensions
 * @param response response
 * @return GETDNS_RETURN_GOOD on success

 */
getdns_return_t
getdns_address_sync(getdns_context *context,
    const char *name,
    getdns_dict *extensions,
    getdns_dict **response);

/**
 * retrieve hostname assigned to an IP address
 * @param context pointer to a previously created context to be used for this call
 * @param address the address to look up
 * @param extensions dict data structures, NULL to use no extensions
 * @param response response
 * @return GETDNS_RETURN_GOOD on success
 */
getdns_return_t
getdns_hostname_sync(getdns_context *context,
    getdns_dict *address,
    getdns_dict *extensions,
    getdns_dict **response);

/**
 * retrieve a service assigned to a DNS name
 * @param context pointer to a previously created context to be used for this call
 * @param name the ASCII based domain name to lookup
 * @param extensions dict data structures, NULL to use no extensions
 * @param response response
 * @return GETDNS_RETURN_GOOD on success
 */
getdns_return_t
getdns_service_sync(getdns_context *context,
    const char *name,
    getdns_dict *extensions,
    getdns_dict **response);

/** @}
 */

getdns_return_t
getdns_convert_dns_name_to_fqdn(
    const getdns_bindata *dns_name_wire_fmt,
    char **fqdn_as_string);

getdns_return_t
getdns_convert_fqdn_to_dns_name(
    const char *fqdn_as_string,
    getdns_bindata **dns_name_wire_fmt);

char *getdns_convert_ulabel_to_alabel(const char *ulabel);

char *getdns_convert_alabel_to_ulabel(const char *alabel);

getdns_return_t
getdns_validate_dnssec(getdns_list *to_validate,
    getdns_list *support_records,
    getdns_list *trust_anchors);

/**
 * creates a string that describes the dictionary in a human readable form
 * one line per item in the dictionary
 * TODO: maybe this should be json or something machine readable too
 * @param this_dict dictionary to pretty print
 * @return character array (caller must free this) containing pretty string
 */
char *getdns_pretty_print_dict(const getdns_dict *some_dict);

char *getdns_display_ip_address(const getdns_bindata
    *bindata_of_ipv4_or_ipv6_address);

getdns_return_t
getdns_context_set_context_update_callback(
  getdns_context *context,
  void (*value)(getdns_context *context,
                getdns_context_code_t changed_item)
);

getdns_return_t
getdns_context_set_resolution_type(getdns_context *context,
    getdns_resolution_t value);

getdns_return_t
getdns_context_set_namespaces(getdns_context *context,
    size_t namespace_count, getdns_namespace_t *namespaces);

getdns_return_t
getdns_context_set_dns_transport(getdns_context *context,
    getdns_transport_t value);

getdns_return_t
getdns_context_set_limit_outstanding_queries(getdns_context *context,
    uint16_t limit);

getdns_return_t
getdns_context_set_timeout(getdns_context *context, uint64_t timeout);

getdns_return_t
getdns_context_set_follow_redirects(getdns_context *context,
    getdns_redirects_t value);

getdns_return_t
getdns_context_set_dns_root_servers(getdns_context *context,
    getdns_list *addresses);

getdns_return_t
getdns_context_set_append_name(getdns_context *context,
    getdns_append_name_t value);

getdns_return_t
getdns_context_set_suffix(getdns_context *context, getdns_list *value);

getdns_return_t
getdns_context_set_dnssec_trust_anchors(getdns_context *context,
    getdns_list *value);

getdns_return_t
getdns_context_set_dnssec_allowed_skew(getdns_context *context,
    uint32_t value);

getdns_return_t
getdns_context_set_upstream_recursive_servers(getdns_context *context,
    getdns_list *upstream_list);

getdns_return_t
getdns_context_set_edns_maximum_udp_payload_size(getdns_context *context,
    uint16_t value);

getdns_return_t
getdns_context_set_edns_extended_rcode(getdns_context *context,
    uint8_t value);

getdns_return_t
getdns_context_set_edns_version(getdns_context *context, uint8_t value);

getdns_return_t
getdns_context_set_edns_do_bit(getdns_context *context, uint8_t value);

getdns_return_t
getdns_context_set_memory_functions(getdns_context *context,
    void *(*malloc) (size_t),
    void *(*realloc) (void *, size_t),
    void (*free) (void *)
    );

getdns_return_t
getdns_context_set_extended_memory_functions(getdns_context *context,
    void *userarg,
    void *(*malloc) (void *userarg, size_t sz),
    void *(*realloc) (void *userarg, void *ptr, size_t sz),
    void (*free) (void *userarg, void *ptr)
    );
"""

MACROS = """
"""

CUSTOMIZATIONS = """
"""

CONDITIONAL_NAMES = {}

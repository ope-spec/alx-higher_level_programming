#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @string_obj: A PyObject string object.
 *
 * This function prints detailed information about a Python string object.
 * It checks if the object is a valid string object and then displays its type,
 * length, and value.
 *
 * Parameters:
 *   - string_obj: The PyObject string object to be inspected.
 */

void print_python_string(PyObject *string_obj)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	length = ((PyASCIIObject *)(p))->length;

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}

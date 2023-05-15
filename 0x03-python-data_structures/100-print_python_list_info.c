#include <Python.h>

void print_python_list_info(PyObject *p)
{
    int size = PyList_Size(p);
    int i;
    PyListObject *list = (PyListObject *)p;

    printf("[*] Size of the Python List = %d\n", size);
    printf("[*] Allocated = %d\n", (int)list->allocated);

    for (i = 0; i < size; i++)
    {
        printf("Element %d: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
    }
}

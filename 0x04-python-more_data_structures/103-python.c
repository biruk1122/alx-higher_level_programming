#include <Python.h>

void print_python_bytes(PyObject *p)
{
    printf("[.] bytes object info\n");
    if (PyBytes_Check(p))
    {
        printf("  size: %ld\n", PyBytes_Size(p));
        printf("  trying string: ");
        if (PyBytes_Size(p) >= 10)
        {
            for (int i = 0; i < 10; i++)
            {
                printf("%02x ", ((unsigned char *)PyBytes_AsString(p))[i]);
            }
        }
        else
        {
            for (Py_ssize_t i = 0; i < PyBytes_Size(p); i++)
            {
                printf("%02x ", ((unsigned char *)PyBytes_AsString(p))[i]);
            }
        }
        printf("\n");
    }
    else
    {
        printf("  [ERROR] Invalid Bytes Object\n");
    }
}

void print_python_list(PyObject *p)
{
    PyListObject *list = (PyListObject *)p;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", PyList_Size(p));
    printf("[*] Allocated = %ld\n", list->allocated);

    for (Py_ssize_t i = 0; i < PyList_Size(p); i++)
    {
        PyObject *elem = PyList_GetItem(p, i);
        printf("Element %ld: ", i);

        if (PyBytes_Check(elem))
        {
            print_python_bytes(elem);
        }
        else
        {
            printf("Not a bytes object\n");
        }
    }
}

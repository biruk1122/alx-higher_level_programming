#define PY_SSIZE_T_CLEAN
#include <Python.h>

void print_python_string(PyObject *p)
{
    if (PyUnicode_Check(p))
    {
        Py_UNICODE *wstr;
        Py_ssize_t size;

        size = PyUnicode_GET_SIZE(p);
        wstr = PyUnicode_AS_UNICODE(p);

        if (PyCompactUnicode_Check(p))
            printf("[.] string object info\n  type: compact unicode object\n  length: %ld\n  value: ", size);
        else
            printf("[.] string object info\n  type: compact ascii\n  length: %ld\n  value: ", size);

        for (Py_ssize_t i = 0; i < size; ++i)
            printf("%lc", wstr[i]);

        printf("\n");
    }
    else
    {
        printf("[.] string object info\n  [ERROR] Invalid String Object\n");
    }
}

#include "Python.h"
#include "sam.h"


static PyObject *py_gcd(PyObject *self, PyObject *args){
    int x, y, result;

    if (!PyArg_ParseTuple(args, "ii", &x, &y)){
        return NULL;
    }
    result = gcd(x, y);
    return Py_BuildValue("i", result);
} 


static PyObject *py_in_mandel(PyObject *self, PyObject *args){
    double x0, y0;
    int n;
    int result;

    if (!PyArg_ParseTuple(args, "ddi", &x0, &y0, &n)){
        return NULL;
    }
    result = in_mandel(x0, y0, n);
    return Py_BuildValue("i", result);
}


static PyObject *py_divide(PyObject *self, PyObject *args){
    int a, b, quotient, remainder;
    if (!PyArg_ParseTuple(args, "ii", &a, &b)){
        return NULL;
    }
    quotient = divide(a, b, &remainder);
    return Py_BuildValue("(ii)", quotient, remainder);
}


static PyMethodDef SampleMethods[] = {
    {"gcd", py_gcd, METH_VARARGS, "Greatest common divisor"},
    {"in_mandel", py_in_mandel, METH_VARARGS, "Mandelbrot test"},
    {"divide", py_divide, METH_VARARGS, "Integer division"},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef samplemodule = {
    PyModuleDef_HEAD_INIT,
    "sam",
    "A sample modeule",
    -1,
    SampleMethods
};


PyMODINIT_FUNC
PyInit_sam(void){
    return PyModule_Create(&samplemodule);
}
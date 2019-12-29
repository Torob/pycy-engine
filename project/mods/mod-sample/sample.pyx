# distutils: language=c++
# distutils: extra_compile_args = -std=c++14
# distutils: extra_link_args = -std=c++14 

from libcpp.string cimport string

cdef extern from "sample.h":
    cdef cppclass TestModule:
        TestModule() except +
        void initiate()
        string get_answer(string)

cdef class pMod1:
    cdef TestModule *thisptr

    def __cinit__(self):
        self.thisptr = new TestModule()

    def initiate(self):
        return self.thisptr.initiate()

    def get_answer(self, query):
        return self.thisptr.get_answer(query)

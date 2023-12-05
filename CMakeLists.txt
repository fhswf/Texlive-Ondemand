cmake_minimum_required(VERSION 3.22)
project(TextLiveOnDemand VERSION 0.1.0 LANGUAGES C)
set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})

option(BUILD_SHARED_LIBS "Build using shared libraries" ON)

set(SRCS "texliveondemand/texliveondemand.c")

add_library(texliveondemand SHARED ${SRCS})

set(Python_ADDITIONAL_VERSIONS 3.10)
find_package(PythonLibs REQUIRED)

add_library(libkpathsea STATIC IMPORTED)

set_target_properties(
    texliveondemand
    PROPERTIES
        PREFIX ""
        OUTPUT_NAME "texliveondemand"
        LINKER_LANGUAGE C
        LINK_LIBRARIES "${PYTHON_LIBRARIES}"
        INCLUDE_DIRECTORIES "/usr/include/python3.10;${PYTHON_INCLUDE_DIR}"
        # COMPILE_DEFINITIONS "Py_LIMITED_API=0x03090000" # (broke in default installation)
    )
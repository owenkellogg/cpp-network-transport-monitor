from conan import ConanFile

import logging

class MyProject(ConanFile):
    
    settings = "os", "compiler", "build_type", "arch"

    requires = (
        'boost/1.83.0'
    )

    generators= (
      'CMakeDeps',
      'CMakeToolchain',
    )


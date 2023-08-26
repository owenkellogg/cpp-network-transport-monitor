cmake_minimum_required(VERSION 3.20)
project(cpp-boost-cmake)

include(${CMAKE_BINARY_DIR}/conan_toolchain.cmake)


set(SOURCES
  ${CMAKE_CURRENT_SOURCE_DIR}/src/main.cpp
)

add_executable(cpp-boost-cmake ${SOURCES})

find_package(Boost REQUIRED)

target_link_libraries(cpp-boost-cmake PRIVATE boost::boost)
